import requests
import json
import pandas as pd
from pandas.io.json import json_normalize 
from openpyxl import Workbook

url = "https://www.mdcomune.com.br/RestServiceApi/Mark/SetMarks"

df = pd.read_excel('C:/Users/tharl/OneDrive/Área de Trabalho/API/Demonstração/marcações 2021.xlsx')

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
    payload = {
	"Matricula": item["Matricula"],
	"DataHoraApontamento": "{:02d}/{:02d}/{} {:02d}:{:02d}".format(item["Dia"], item["Mes"], item["Ano"], item["Hora"], item["Minuto"]),
	"ResponseType": "AS400V1"
}
    print (payload)

    payloads.append(payload)

for payload in payloads: 

    json.dumps(payload, ensure_ascii=False) 

    #print(json_data) 

    response = requests.post(url, headers=headers, json=payload) 

    print(response.text) 
