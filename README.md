
````markdown
# ✈️ Rwanda Flight Price Tracker
![Flight Tracker Status](https://github.com/Byadiso/kigali_flight/actions/workflows/main.yml/badge.svg)

An automated flight price monitor that scans for the cheapest travel deals between **Poland/Germany** and **Kigali, Rwanda (KGL)**. The bot performs calculations to find the absolute cheapest date combinations and sends alerts directly to Telegram.

---

## 🚀 How It Works

1. **Scans Multiple Dates** – Checks a range of departure and return dates for **July/August 2026**.
2. **Optimizes Prices** – Compares all possible date combinations to find the **cheapest option**.
3. **Currency Guard** – Forces prices into **PLN** and filters out simulated or test data.
4. **Automated Execution** – Runs every **30 minutes via GitHub Actions (24/7)**.
5. **Instant Alerts** – Sends a **Telegram notification** with a direct **Google Flights booking link**.

---

## 🛠️ Tech Stack

- **Python 3.10** – Core logic and API interaction  
- **Duffel API** – Live flight data source  
- **GitHub Actions** – Automation and scheduling  
- **Telegram Bot API** – Instant notifications  

---

## ⚙️ Setup & Installation

### 1. Secrets Configuration

Add the following **Secrets** to your GitHub repository:

**Settings → Secrets and variables → Actions**

| Secret | Description |
|------|-------------|
| `DUFFEL_TOKEN` | Your Duffel Live Access Token (`duffel_live_...`) |
| `TELEGRAM_TOKEN` | Your Telegram Bot API token from **@BotFather** |
| `CHAT_ID` | Your numeric Telegram Chat ID |

---

### 2. Local Testing

Create a `.env` file (this file should be ignored by Git) for local development:

```env
DUFFEL_TOKEN=your_token_here
TELEGRAM_TOKEN=your_bot_token
CHAT_ID=your_id
````

---

## 📅 Tracking Schedule

The tracker runs automatically:

* **Every 30 minutes** via Cron in GitHub Actions
* **On every push** to the `master` branch
* **Manually** via the **Run workflow** button in the GitHub Actions tab

---

## ⚠️ Important Note on Costs

* **Searching is Free:** The Duffel API does not charge for searching flight offers.
* **GitHub Actions:** The workflow stays within the **2,000 free minutes per month** available for GitHub Free accounts.

---

## 👤 Author

**BYAMUNGU Desire**
Flight Search Automation Project – 2026
