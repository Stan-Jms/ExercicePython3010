import re

from getter import *

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
            if OL_title != "" and re.search(OL_title,GO_title):
                key+=1
            if ALT_title != "" and re.search(ALT_title,GO_title):
                key+=1
            if BNF_title != "" and re.search(BNF_title,GO_title):
                key+=1
            if key<=2:
                print(GO_title) #send the data
            

    i+=1