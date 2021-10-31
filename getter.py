import requests
import json
import isbnlib
import re
from isbnlib.registry import bibformatters
from isbnlib import meta

# rint(isbnlib.cover(isbn))
def getData():
    finalValues = {}
    regex = r"[O][L][0-9][0-9][0-9][0-9][0-9][0-9][0-9][M][/]"
    regex1 = r"[O][L][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][M][/]"
    i = 0
    try:
        with open('c:/Users/Stan/Desktop/2810/isbn.csv', 'r+') as file:
            for ligne in file:
                temp = {}

                #Open Lib OK
                cleaned = ligne.rstrip()
                temp["ISBN"] = cleaned
                acc = {}
                url = "https://openlibrary.org/api/books?bibkeys=ISBN:"+cleaned+"&format=json"
                payload = {}
                headers = {}
                response = requests.request("GET", url, headers=headers, data=payload)
                x = json.loads(response.text)
                try:
                    x = x['ISBN:'+cleaned]['info_url'].replace("https://openlibrary.org/books/","")
                    x = re.sub(regex,'',x)
                    x = re.sub(regex1,'',x)
                    x = x.replace("_"," ")
                    x = x.replace(".","")
                    acc["title"] = x
                    temp["OpenLib"] = acc
                except KeyError:
                    print("void")

                #GoogleBooks OK
                query = 'isbn:'+cleaned
                acc = {}
                params = {"q": query}
                url = 'https://www.googleapis.com/books/v1/volumes'
                response = requests.get(url, params=params)
                x = json.loads(response.text)
                if x['totalItems'] != 0:
                    try: 
                        acc['title'] = x["items"][0]['volumeInfo']["title"]
                    except KeyError:
                        print('void')
                    try:
                        acc['authors'] = x["items"][0]['volumeInfo']["authors"]
                    except KeyError:
                        print('void')
                    temp["GoogleBooks"] = acc
                # #AltMetrics OK
                url = "https://api.altmetric.com/v1/isbn/"+cleaned
                payload = {'title' : 'json'}
                headers = {}
                acc = {}
                response = requests.request("GET", url, headers=headers, data=payload)
                if(response.text != "Not Found"):
                    if response.text[0] == '{':
                        res = json.loads(response.text)
                        acc['title'] = res['title']
                        acc ['authors'] = res['authors_or_editors']
                        temp["AltMetrics"] = acc
                
                #BNF OK
                SERVICE = "bnf"
                isbn = cleaned
                try:
                    acc = {}
                    bibtex = bibformatters["json"]
                    response = bibtex(meta(isbn, SERVICE))
                    response = json.loads(response)
                    acc["title"] = response["title"]
                    acc["authors"] = response["author"]
                    temp["BNF"] = acc
                    
                except AttributeError:
                    print("void")


                finalValues[i] = temp
                i+=1
            return finalValues

    except FileNotFoundError:
        print("Fichier introuvable")
    except IOError:
        print("erreur d’ouverture")

