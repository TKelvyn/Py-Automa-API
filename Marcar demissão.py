#Marcar demissão 

import pyautogui   

import pyperclip     

import time 

from openpyxl import Workbook 

import json 

import requests 

import pandas as pd 

from pandas.io.json import json_normalize 

import openpyxl 

 
 

url = "https://www.mdcomune.com.br/RestServiceApi/Dismiss/MarkDismiss" 

 
 

headers = {"Content-Type": "application/json", "key": "", "identifier":"", "Accept" :"*/*","Accept-Encoding":"gzip, deflate, br","User-Agent":"PostmanRuntime/7.30.0" } 

 
 

payload = json.dumps({ 

  "PESSOAID":20718, 

  "MOTIVO":"10-Rescisão com justa causa por iniciativa do empregador", 

  "DATA":"2022-11-28" 

}) 

 
 

response = requests.post(url, json=payload, headers=headers) 

 
 

print(response.text) 