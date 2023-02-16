import requests 

import json 

import pandas as pd 

from pandas.io.json import json_normalize 

 
 

url = "https://www.mdcomune.com.br/RestServiceApi/OrganizationalStructure/DeleteOrganizationalStructure" 

 
 

df = pd.read_excel('C:/Users/tharl/OneDrive/Área de Trabalho/API/Demonstração/estruturas.xlsx') 

 
 

data = df.to_dict('records') 

 
 

headers = { 

"Content-Type": "application/json", 

"key": "", 

"identifier":"", 

"Accept" :"/", 

"Accept-Encoding":"gzip, deflate, br", 

"User-Agent":"PostmanRuntime/7.30.0" } 
 
 

payloads = [] 

 
 

for item in data: 

    payload =json.dumps({ 

        "Id": item['id'] 

    })

    payloads.append(payload) 

 
 

for payload in payloads: 

    json_data = json.dumps(payload, ensure_ascii=False) 

    print(json_data) 

    response = requests.post(url, headers=headers, json=payload) 

    print(response.text) 