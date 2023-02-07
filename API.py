import requests
import pandas as pd

api_key = "b2534a6482828132c3baa9e6ae2231c0"
series_ids = ["GNPCA"]

df_dict = {}
for series_id in series_ids:
    
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={api_key}&file_type=json"
    response = requests.get(url)

    if response.status_code == 200:
        
        data = response.json()
        data_dict = {"date": [observation["date"] for observation in data["observations"]],
                     "value": [observation["value"] for observation in data["observations"]]}
        df = pd.DataFrame(data_dict)
        df_dict[series_id] = df
    else:
        break
