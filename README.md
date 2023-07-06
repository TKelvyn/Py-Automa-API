# Py-Automa-API
Projeto de uma serie de automações usando rest API 

Este projeto foi desenvolvido com o objetivo de permitir a interação com uma API REST por meio da linguagem Python. Ele possui as seguintes funcionalidades:

Busca de itens na API e conversão do JSON para planilhas em formato XLSX ou CSV.
Envio de planilhas, arquivos de texto e outros valores para a API, convertendo-os para o formato JSON.
Como usar
Para utilizar este projeto, é necessário ter Python 3 instalado na sua máquina, bem como as bibliotecas pandas, requests e openpyxl.

Após instalar as bibliotecas necessárias, é possível executar os arquivos api_to_excel.py e excel_to_api.py para realizar a interação com a API.

O arquivo api_to_excel.py possui a função de buscar os itens da API e convertê-los em planilhas, que são salvas em um diretório local. Já o arquivo excel_to_api.py realiza a leitura de planilhas e outros arquivos, convertendo-os para o formato JSON e enviando para a API.

Ambos os arquivos possuem um código comentado, o que permite uma fácil compreensão do seu funcionamento e possibilita a sua personalização de acordo com as necessidades do usuário.

Personalização
Este projeto foi desenvolvido em Python e possui um código fonte de fácil compreensão, o que permite a sua personalização de acordo com as necessidades do usuário. É possível editar os arquivos api_to_excel.py e excel_to_api.py para incluir novas funcionalidades ou modificar as existentes. Além disso, também é possível personalizar a estrutura da API utilizada, adaptando-a para a sua própria aplicação.

PS: Realizei alguas atualizações para ganho de desempenho e economia de recursos, utilizando multitrheads.
