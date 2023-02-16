#Cadastro de Pessoas

import requests 

import json 

import pandas as pd 

from pandas.io.json import json_normalize 

 
 

url = "https://www.mdcomune.com.br/RestServiceApi/People/SavePerson" 

 
 

df = pd.read_excel('C:/Users/tharl/OneDrive/Área de Trabalho/API/Demonstração/pessoas.xlsx') 

 
 

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

    payload ={ 

 
 

 "Matricula": item["Matricula"], 

  

 "Nome": item["Nome"], 

  

  "Cracha": item["Cracha"], 

  

   "DataAdmissao":  item["DataAdmissao"], 

  

     "BaseHoras": item["BaseHoras"], 

        

      "Estrutura": { 

        "Id": item["Estrutura.Id"], 

        "Codigo": item["Estrutura.Codigo"], 

        "CentroCusto": None, 

        "Descricao": None, 

        "DescricaoEstruturaPai": None, 

        "Extra1": None, 

        "Extra2": None}, 

          

         "TipoFuncionario": {     

          "IdTipoFuncionario": item["TipoFuncionario.IdTipoFuncionario"],     

          "CarteiraTrabalho": None  }, 

            

         "TipoSalario": {     

          "Id": item["TipoSalario.Id"],     

          "Nome": None  }, 

              

        "Horarios": [    {      "Id": 0,      "Horario": {       "Id": item["Horarios"]     },"Inicio": "0001-01-01T00:00:00","Fim": "0001-01-01T00:00:00"    }  ], 

 
 
 

         "MaisDeUmVinculoEmpregaticio":"false",   

                      

         "RegrasCalculo": [    {      "Id": 0, 

         "Regra": {        "Id": item["RegrasCalculo"]    }, 

         "Inicio": "0001-01-01T00:00:00",       

         "Fim": "0001-01-01T00:00:00"    }  ],   

                              

         "CodigoPis": item["CodigoPis"],   

          

         "CodigoPisNumerico": 0,   

          

         "Sexo": item["Sexo"],   

          

         "AmbienteTrabalhoPessoa": [    {"Id": 0, 

         "Inicio": "0001-01-01T00:00:00", 

         "Fim": "0001-01-01T00:00:00", 

         "TipoAmbienteTrabalho": 6  }  ]} 

 
 

    payloads.append(payload) 

 
 

for payload in payloads: 

    json_data = json.dumps(payload, ensure_ascii=False) 

    print(json_data) 

    response = requests.post(url, headers=headers, json=payload) 

    print(response.text) 