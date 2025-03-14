import requests
import json

# URL of the API
url = "https://www.hsi.com.hk/data/chi/rt/index-series/hsi/constituents.do?1538"

top10_stockIn_HSI = 'https://www.hsi.com.hk/api/wsit-hsil-hiip-ea-public-proxy/v1/dataretrieval/e/constituents/v1?language=chi&indexCode=00001.00'

# Fetch data from the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    stock_dict ={}
    stock_dict["恒生指數"]="^HSI"
    # Extract the relevant information
    for item in data["indexSeriesList"][0]["indexList"][0]["subIndexList"]:
        for data in item["constituentContent"]:
            code = data["code"]
            stock_ID = f"{code.zfill(4)}.HK"
            stock_dict[data["constituentName"].replace(" - ", "-")]=stock_ID
    stock_dict.pop("香港中華煤氣")
    stock_dict.pop("中國平安")
    stock_dict.pop("領展房產基金")
    stock_dict.pop("華潤萬象生活")
    stock_dict.pop("九龍倉置業")
    stock_dict.pop("東方海外國際")
    stock_dict.pop("中國石油化工股份")
    stock_dict.pop("信義光能")
    stock_dict.pop("恒安國際")
    stock_dict.pop("中國神華")
    stock_dict.pop("國藥控股")
    stock_dict.pop("中國生物製藥")
    stock_dict.pop("比亞迪股份")
    stock_dict.pop("中國宏橋")
    stock_dict.pop("百威亞太")
    stock_dict.pop("金沙中國有限公司")
    stock_dict.pop("周大福")
    stock_dict.pop("理想汽車-W")
    stock_dict.pop("安踏體育")
    stock_dict.pop("申洲國際")
    stock_dict.pop("翰森製藥")
    stock_dict.pop("海爾智家")
    stock_dict.pop("海底撈")
    stock_dict.pop("農夫山泉")
    stock_dict.pop("新東方-S")
    stock_dict.pop("攜程集團-S")
  




    # Save the data in the desired JSON format
    with open('../utils/stocks_ID.json', 'w', encoding='utf-8') as json_file:
        json.dump(stock_dict, json_file, ensure_ascii=False, indent=4)
    
    print("Data saved to stocks.json")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")