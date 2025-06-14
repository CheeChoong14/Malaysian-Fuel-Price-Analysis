
import requests
import time
import logging
import json

# Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

API_URL = "https://api.data.gov.my/data-catalogue"
PARAMS = {"id": "fuelprice"}

def fetch_fuel_prices(max_retries=3, backoff_sec=2):

    for attempt in range(1, max_retries + 1):
        try:
            logging.info(f"Attempt {attempt} → GET {API_URL}?id=fuelprice")
            resp = requests.get(API_URL, params=PARAMS, timeout=10)
            resp.raise_for_status()   # HTTP errors → raise
            data = resp.json()        # JSON decode → might raise ValueError
            # unwrap if needed
            records = data.get("data") if isinstance(data, dict) and "data" in data else data
            logging.info(f"Success on attempt {attempt}: retrieved {len(records)} records")
            return records

        except requests.RequestException as e:
            logging.error(f"Network/API error on attempt {attempt}: {e}")
        except ValueError as e:
            logging.error(f"Failed to decode JSON on attempt {attempt}: {e}")

        if attempt < max_retries:
            logging.info(f"Waiting {backoff_sec}s before retrying…")
            time.sleep(backoff_sec)

    raise RuntimeError("Failed to fetch fuel-price data after all retries")

if __name__ == "__main__":
    # —— Run extraction and print a sample to verify ——  
    records = fetch_fuel_prices()
    # Save to a local JSON file
    with open("fuel_prices_raw.json", "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
    print("Saved raw data to json file") # to double check is running
