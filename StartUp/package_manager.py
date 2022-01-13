import json
import os 
import sys 

def loadData():
    with open("requiredPackages.json", 'r') as s:
        data = json.load(s)
    return data;

print(loadData())