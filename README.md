# ✈️ Rwanda Flight Price Tracker

An automated flight price monitor that scans for the cheapest travel deals between **Poland/Germany** and **Kigali, Rwanda** (KGL). The bot performs calculations to find the absolute cheapest date combinations and sends alerts directly to Telegram.

## 🚀 How it Works
1. **Scans Multiple Dates:** Checks a range of departure and return dates for July/August 2026.
2. **Optimizes Prices:** Compares all possible date combinations to find the #1 cheapest option.
3. **Currency Guard:** Forces prices into **PLN** and filters out simulated "test" data.
4. **Automated:** Runs every 30 minutes via **GitHub Actions** (24/7).
5. **Alerts:** Sends a Telegram notification with a direct **Google Flights** booking link.

## 🛠️ Tech Stack
* **Python 3.10**: The core logic and API interaction.
* **Duffel API**: Live flight data source.
* **GitHub Actions**: Automation and scheduling.
* **Telegram Bot API**: Instant notifications.

## ⚙️ Setup & Installation

### 1. Secrets Configuration
To run this project, you must add the following **Secrets** to your GitHub Repository (**Settings > Secrets and variables > Actions**):

| Secret | Description |
| :--- | :--- |
| `DUFFEL_TOKEN` | Your Duffel Live Access Token (`duffel_live_...`) |
| `TELEGRAM_TOKEN` | Your Telegram Bot API Token from @BotFather |
| `CHAT_ID` | Your numeric Telegram Chat ID |

### 2. Local Testing
If you want to run it locally, create a `.env` file (which is ignored by Git):
```env
DUFFEL_TOKEN=your_token_here
TELEGRAM_TOKEN=your_bot_token
CHAT_ID=your_id

