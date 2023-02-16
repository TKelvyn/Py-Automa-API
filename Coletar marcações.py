
import pyperclip 

import time 

from openpyxl import Workbook 

import json 

import requests 

import pandas as pd 

from pandas.io.json import json_normalize 

import openpyxl 


url = "https://www.mdcomune.com.br/RestServiceApi/Mark/GetMarks"   

 
 

headers = {"Content-Type": "application/json", 

"key": "", 

"identifier":"", 

"Accept" :"/", 

"Accept-Encoding":"gzip, deflate, br", 

"User-Agent":"PostmanRuntime/7.30.0" } 

  

payload = {"MatriculaPessoa": [4340],"DataInicio": "01/01/2019", "DataFim": "25/01/2023","ResponseType": "AS400V1"} 

 
 

response = requests.post(url, json=payload, headers=headers) 

 
 

if response.status_code == 200: 

    #print(response.json())         #Em caso de erro tire o primeiro Hashtag 

    response_json = response.json() 

    data = json_normalize(response_json["Obj"]) 

    print(data) 

    file_path = "C:/Users/tharl/OneDrive/Área de Trabalho/API/Demonstração/marcações.xlsx" 

    data.to_excel(file_path) 

    df = pd.read_excel(file_path, sheet_name='Sheet1') 

    json_data = df.at[0, 'Obj'] 

    data = json.loads(json_data) 

    data = json_normalize(data) 

    data_subset = data[['Matricula', 'Dia', 'Mes', 'Ano','Hora','Minuto' ]] 

    data_subset.rename(columns={'Matricula':'Matricula', 'Dia':'Dia', 'Mes':'Mes', 'Ano':'Ano', 'Hora':'Hora', 'Minuto':'Minuto'}, inplace=True) 

    data_subset.reindex(columns=['Matricula', 'Dia', 'Mes', 'Ano','Hora','Minuto']) 

    data_subset.to_excel(file_path, sheet_name='Sheet2') 

 
 

else: 

    print("Error:", response.status_code) 