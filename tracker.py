import os
import requests
import time

# This library is only needed for local testing
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Config from Environment / .env
DUFFEL_TOKEN = os.getenv('DUFFEL_TOKEN')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

ORIGINS = ["WAW", "BER"]
DESTINATION = "KGL"
DEPART_DATES = ["2026-07-21", "2026-07-22", "2026-07-23", "2026-07-24", "2026-07-25", "2026-07-26", "2026-07-27"]
RETURN_DATES = ["2026-08-15", "2026-08-16", "2026-08-17", "2026-08-18", "2026-08-19", "2026-08-20", "2026-08-21"]

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": msg, "parse_mode": "HTML"}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Telegram error: {e}")

def run_tracker():
    print("🚀 Starting search (Audit Mode: Checking Currency)...")
    all_results = []
    
    headers = {
        "Authorization": f"Bearer {DUFFEL_TOKEN}",
        "Duffel-Version": "v2", 
        "Content-Type": "application/json"
    }

    for origin in ORIGINS:
        for d_date in DEPART_DATES:
            for r_date in RETURN_DATES:
                if r_date <= d_date:
                    continue

                try:
                    url = "https://api.duffel.com/air/offer_requests"
                    data = {
                        "data": {
                            "slices": [
                                {"origin": origin, "destination": DESTINATION, "departure_date": d_date},
                                {"origin": DESTINATION, "destination": origin, "departure_date": r_date}
                            ],
                            "passengers": [{"type": "adult"}],
                            "cabin_class": "economy",
                            "selected_offers_currency": "PLN"
                        }
                    }

                    response = requests.post(url, headers=headers, json=data)
                    res_data = response.json()

                    if response.status_code != 201:
                        continue

                    offers = res_data['data']['offers']
                    if not offers:
                        continue
                        
                    cheapest_offer = min(offers, key=lambda x: float(x['total_amount']))
                    
                    # --- CURRENCY GUARD ---
                    raw_price = float(cheapest_offer['total_amount'])
                    api_currency = cheapest_offer['total_currency']
                    airline = cheapest_offer['owner']['name']

                    # If the API ignores our "PLN" request and sends USD/EUR, convert it
                    if api_currency == "USD":
                        price_pln = round(raw_price * 4.0, 2) # Est. 4 PLN per 1 USD
                    elif api_currency == "EUR":
                        price_pln = round(raw_price * 4.3, 2) # Est. 4.3 PLN per 1 EUR
                    else:
                        price_pln = raw_price

                    if "Duffel" in airline:
                        continue

                    # Log exactly what the API is telling us
                    print(f"[{origin}] {d_date} to {r_date}: {raw_price} {api_currency} -> {price_pln} PLN ({airline})")

                    all_results.append({
                        "origin": origin,
                        "d_date": d_date,
                        "r_date": r_date,
                        "price": price_pln,
                        "original_price": f"{raw_price} {api_currency}",
                        "airline": airline
                    })
                    
                    time.sleep(1.2)
                    
                except Exception as e:
                    print(f"Error: {e}")

    if all_results:
        best_deal = min(all_results, key=lambda x: x['price'])
        
        # We only send a message if it's a realistic price (above 2000 PLN)
        if best_deal['price'] < 2000:
            print(f"⚠️ Warning: Found a price of {best_deal['price']} PLN. This is likely a 'Base Fare' error and will be ignored.")
            return

        google_url = f"https://www.google.com/travel/flights?q=Flights%20to%20{DESTINATION}%20from%20{best_deal['origin']}%20on%20{best_deal['d_date']}%20through%20{best_deal['r_date']}"
        
        msg = (f"🏆 <b>REAL DEAL FOUND</b>\n\n"
               f"<b>Route:</b> {best_deal['origin']} ➔ {DESTINATION}\n"
               f"<b>Airline:</b> {best_deal['airline']}\n"
               f"<b>Price:</b> 💰 <b>{best_deal['price']} PLN</b>\n"
               f"<i>API returned: {best_deal['original_price']}</i>\n\n"
               f"📅 <b>Away:</b> {best_deal['d_date']}\n"
               f"📅 <b>Back:</b> {best_deal['r_date']}\n\n"
               f"🔗 <a href='{google_url}'>Check on Google Flights</a>")
        
        send_telegram(msg)

if __name__ == "__main__":
    run_tracker()