import pyautogui   

import pyperclip     

import time 

from openpyxl import Workbook 

import json 

import requests 

import pandas as pd 

from pandas.io.json import json_normalize 

import openpyxl 

 
 

url = "https://www.mdcomune.com.br/RestServiceApi/Absence/GetAbsences" 

 
 

headers = {"Content-Type": "application/json", "key": "", "identifier":"", "Accept" :"*/*","Accept-Encoding":"gzip, deflate, br","User-Agent":"PostmanRuntime/7.30.0" } 

 
 

payload = json.dumps({ 

    "IdsPessoa": [20713], 

    "DataInicio":"01-09-2022", 

    "DataFim":"15-12-2022", 

    "ResponseType":"AS400V1" 

}) 

 
 

response = requests.post(url, json=payload, headers=headers) 

 
 
 
 

if response.status_code == 200: 

    print(response.json()) 

    response_json = response.json() 

    data = json_normalize(response_json["Obj"]) 

    file_path = "C:/Users/tharl/OneDrive/Área de Trabalho/API/ABS.xlsx" 

    data.to_excel(file_path) 

    df = pd.read_excel(file_path, sheet_name="Sheet1") 

    json_data = df.at[0, "Obj"] 

    data = json.loads(json_data) 

    data = json_normalize(data) 

    data_subset = data[["TipoRegisto","Numero","Dia","Mes", "Ano","QuantidadeTempo" ,"Aprovado"]] 

    data_subset.rename(columns={"TipoRegisto":"TipoRegisto", "Numero":"matricula", "Dia":"Dia", "Mes":"Mes", "Ano":"Ano","QuantidadeTempo":"Tempo em Minutos","Aprovado":"Aprovado"}, inplace=True) 

    data_subset.to_excel(file_path, sheet_name="Sheet2") 

 
 

    

else: 

    

    print("Error:", response.status_code) 