from os import altsep
import re

from getter import *


def sort():

    data = getData()
    i = 0
    payload = {}

    while i < len(data):
        key = 0
        try:
            OL_title = data[i]['OpenLib']['title']
        except KeyError:
            OL_title = ""
        try:
            GO_title = data[i]['GoogleBooks']['title']
        except KeyError:
            GO_title = ""
        try:
            ALT_title = data[i]['AltMetrics']['title']
        except KeyError:
            ALT_title = ""
        try:
            BNF_title = data[i]['BNF']['title']
        except KeyError:
            BNF_title = ""


        if OL_title == GO_title == ALT_title == BNF_title and GO_title == "":
            pass
        else:
            if data[i]["ISBN"] != "":
                ISBN = data[i]["ISBN"]

                if OL_title != "" and re.search(OL_title,GO_title):
                    key+=1
                if ALT_title != "" and re.search(ALT_title,GO_title):
                    key+=1
                if BNF_title != "" and re.search(BNF_title,GO_title):
                    key+=1
                if key<=2:
                    if GO_title != '':
                        TITLE = GO_title
                        AUTHORS = getauthors(data,i)
                    elif BNF_title != '':
                        TITLE = BNF_title
                        AUTHORS = getauthors(data,i)
                    elif ALT_title != '' :
                        TITLE = ALT_title
                        AUTHORS = getauthors(data,i)
                    elif OL_title != "":
                        TITLE = OL_title
                        AUTHORS = getauthors(data,i)
                
                payload[i]["ISBN"] = ISBN
                payload[i]["title"] = TITLE
                payload[i]["authors"] = AUTHORS
        i+=1
    return payload

def getauthors(data,i):

    try:
        GO_authors = data[i]['GoogleBooks']['authors']
        authors = GO_authors
    except KeyError:
        try:
            ALT_authors = data[i]['AltMetrics']['authors']
            authors = ALT_authors
        except KeyError:
            try:
                BNF_authors = data[i]['BNF']['authors']
                authors = BNF_authors
            except KeyError:
                authors = "none"
    return authors


print(sort())