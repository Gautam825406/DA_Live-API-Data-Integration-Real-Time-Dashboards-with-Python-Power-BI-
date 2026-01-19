import requests
import pandas as pd
import time

# -------------------------------
# Power BI Python Script
# -------------------------------

# Health Indicators (World Bank)
indicators = {
    "Life Expectancy": "SP.DYN.LE00.IN",
    "Health Expenditure (% GDP)": "SH.XPD.CHEX.GD.ZS",
    "Infant Mortality Rate": "SP.DYN.IMRT.IN",
    "Maternal Mortality Ratio": "SH.STA.MMRT",
    "Immunization (Measles %)": "SH.IMM.MEAS"
}

BASE_URL = "https://api.worldbank.org/v2/country/all/indicator/{}?format=json&per_page=1000&page={}"

all_data = []

for indicator_name, indicator_code in indicators.items():
    page = 1
    while True:
        url = BASE_URL.format(indicator_code, page)
        response = requests.get(url)

        if response.status_code != 200:
            break

        data = response.json()
        if len(data) < 2:
            break

        total_pages = data[0]["pages"]

        for record in data[1]:
            if record["value"] is not None and int(record["date"]) >= 2016:
                all_data.append({
                    "Country Code": record["country"]["id"],
                    "Country": record["country"]["value"],
                    "Year": int(record["date"]),
                    "Indicator": indicator_name,
                    "Value": record["value"]
                })

        if page >= total_pages:
            break

        page += 1
        time.sleep(0.2)

# Create DataFrame
df = pd.DataFrame(all_data)

# Pivot for Power BI model
dataset = df.pivot_table(
    index=["Country", "Year"],
    columns="Indicator",
    values="Value"
).reset_index()

dataset
