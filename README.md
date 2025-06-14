# Malaysian-Fuel-Price-Analysis
This project analyzes Malaysia's weekly fuel prices using official data from [data.gov.my](https://data.gov.my), with a focus on the RON95, RON97, and Diesel price trends before and after subsidy policy changes in 2024.

## Dataset Source

- **API Endpoint**: [https://api.data.gov.my/data-catalogue?id=fuelprice](https://api.data.gov.my/data-catalogue?id=fuelprice)
- **Fields**:
  - `date`: Date of update (weekly)
  - `ron95`, `ron97`, `diesel`, `diesel_eastmsia`: Price per litre (RM)
  - `series_type`: Level or change


## Project Structure

- `data_extraction.py`  
  → Python script to fetch fuel prices from the API, with built-in logging, retries, and exception handling.

- `fuel_prices_raw.json`  
  → Cached raw API data in JSON format.

- `fuel.ipynb`  
  → Main analysis notebook:
  - Data wrangling & transformation
  - Rolling average & weekly change computation
  - Time-series trend analysis
  - Insights on policy impacts


## Visualisation

- Weekly and monthly trend plots
- 4-week rolling average charts
- Difference plots highlighting price volatility
- Annotated spikes for policy impact awareness


## How to Run

1. Clone this repo  
   `git clone https://github.com/yourusername/fuel-price-analysis.git`

2. Install requirements  
   *(If needed: pandas, matplotlib, seaborn, requests)*

3. Run data extraction  
   `python data_extraction.py`

4. Open and run `fuel.ipynb` for full analysis.
