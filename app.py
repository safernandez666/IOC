import requests
import json
import os
from pprint import pprint 
from datetime import datetime
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

dia = datetime.now()
dia_hoy = dia.strftime("%Y/%m/%d")

### FUNCTIONS ###

def scrape_iocdb_domains(choice=""):
    url = "https://labs.inquest.net/api/iocdb/list"
    response = requests.request("GET", url, verify=False)
    res = json.loads(response.text)
    results=[]
    dia = datetime.now()
    dia_hoy = dia.strftime("%Y/%m/%d")
    for item in res["data"]:
        dia = item["created_date"]
        dia_creado = datetime.strptime(dia, '%a, %d %b %Y %H:%M:%S %Z')
        if((item["artifact_type"] == choice) and (dia_hoy == dia_creado.strftime("%Y/%m/%d"))):
            results.append(item)
    return results

def print_select(var):
    '''
    InQuest Lab's | Indicadores de Compromiso de Twitter Github & Blogs
    Parametro para la Eleccion = "ipaddress", "url", "domain", "hash".
    '''
    results = scrape_iocdb_domains(choice=var);
    x=0

    for item in results:
        x+=1
        print("{0}/{1}: {2}".format(x,len(results),item["artifact"]))

def display_title_bar():

    os.system('clear')
              
    print("\t**********************************************")
    print("\t***         IoC API InQuest Lab's          ***")
    print("\t**  De que se habla en Github Twitter Blogs **")
    print("\t**          el dia de hoy: %s       ** " % dia_hoy) 
    print("\t**********************************************")
    
def get_user_choice():
    # ¿Que queres Obterner?.
    print("\n[1] Hash")
    print("[2] IP Address")
    print("[3] URL")
    print("[4] Domain")
    print("[q] Quit.")
    
    return input("¿Que queres Obterner? ")
    

### MAIN PROGRAM ###

choice = ''
display_title_bar()
while choice != 'q':    
    
    choice = get_user_choice()
    
    display_title_bar()
    if choice == '1':
        print_select("hash")
    elif choice == '2':
        print_select("ipaddress")
    elif choice == '3':
        print_select("url")
    elif choice == '4':
        print_select("domain")
    elif choice == 'q':
        print("\nGracias por revisar los IoC. Saludos.")
    else:
        print("\nNo comprendi la eleccion.\n")