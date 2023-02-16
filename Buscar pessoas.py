#salvar pessoas

import requests 

import pandas as pd 

from pandas.io.json import json_normalize 

import time 

import json 

import openpyxl 

 
 
 

headers = {"Content-Type": "application/json", 

 "key": "78d2375d-53ef-44f0-a756-30eb9653c542", 

 "identifier":"28.481.233/0001-72", 

 "Accept" :"/", 

 "Accept-Encoding":"gzip, deflate, br", 

 "User-Agent":"PostmanRuntime/7.30.0" } 

 
 

url = "https://www.mdcomune.com.br/RestServiceApi/People/SearchPeople" 

 
 

 
 

page = 1 

 
 

file_path = f"C:/Users/tharl/OneDrive/Área de Trabalho/API/Demonstração/pessoas_{page}.xlsx" 

 
 

while True: 

  payload = { 

  "Matricula": 0, #*"Id, "Matricula", "Modificado" or "Excluido"*/ 

  "PaginaAtual": page 

} 

 
 

  response = requests.post( url, headers=headers, json=payload) 

 
 

  #print(response.text) 

 
 

  if response.status_code != 200: 

    break 

    #print(response.json())         #Em caso de erro tire o primeiro Hashtag 

  response_json = response.json() 

  data = json_normalize(response_json["Obj"]) 

  sheet_name = f"Sheet{page}" 

  data.to_excel(file_path, sheet_name=sheet_name, engine='openpyxl') 

  if int(response_json["TotalPagina"]) > page: 

     page += 1 

  else: 

    break 