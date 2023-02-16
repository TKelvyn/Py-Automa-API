#coletar estruturas

import requests 

import json 

import pandas as pd 

from pandas.io.json import json_normalize 

from openpyxl import Workbook 

 
 

url = "https://www.mdcomune.com.br/RestServiceApi/OrganizationalStructure/SearchOrganizationalStructure" 

 
 

#df = pd.read_excel('C:/Users/Administrador/Desktop/api/estrutura.xlsx') 

 
 

#data = df.to_dict('records') 

 
 

headers = { 

"Content-Type": "application/json", 

"key": "", 

"identifier":"", 

"Accept" :"/", 

"Accept-Encoding":"gzip, deflate, br", 

"User-Agent":"PostmanRuntime/7.30.0" } 

 
 
 

payload = {'codigo': '0'}

 
 

response = requests.post(url, headers=headers, json=payload) 

  

if response.status_code == 200: 

    response_json = json.loads(response.content.decode())
    response_json = json.loads(response.json()['Obj'])
    response_json = response.json()
    data = pd.DataFrame.from_dict(response_json, orient='index')
    data = json_normalize(response_json)
    file_name = "ESTRUTURAS.xlsx"
    data = data[{'Obj'}]
    print(data)
    file_path = "C:/Users/tharl/OneDrive/Área de Trabalho/API/Demonstração/estruturas.xlsx" 
    data.to_excel(file_path)
    df = pd.read_excel(file_path, sheet_name='Sheet1')
    json_data = df.at[0, 'Obj']
    data = json.loads(json_data)
    data = json_normalize(data)
    data_subset = data[['Id', 'Codigo', 'Descricao']]
    data_subset.rename(columns={'Id':'id', 'Codigo':'Codigo', 'Descricao':'Descricao'}, inplace=True)
    data_subset.to_excel(file_path, sheet_name='Sheet2')

else: 

    None 