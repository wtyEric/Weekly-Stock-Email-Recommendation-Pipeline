import requests
import json

# URL of the API
url = "https://www.hsi.com.hk/data/chi/rt/index-series/hsi/constituents.do?1538"

# Fetch data from the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    stock_dict ={}
    # Extract the relevant information
    for item in data["indexSeriesList"][0]["indexList"][0]["subIndexList"]:
        for data in item["constituentContent"]:
            code = data["code"]
            stock_ID = f"{code.zfill(4)}.HK"
            stock_dict[data["constituentName"].replace(" - ", "-")]=stock_ID
   



    
    # Save the data in the desired JSON format
    with open('../model_training/stocks_ID.json', 'w', encoding='utf-8') as json_file:
        json.dump(stock_dict, json_file, ensure_ascii=False, indent=4)
    
    print("Data saved to stocks.json")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")