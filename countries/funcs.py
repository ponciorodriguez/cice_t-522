import requests as req
import csv
import json
import os
from languages import languages
real_path = os.path.dirname(__file__)

def menu():
    print("COUNTRIES".center(50, "-"))
    print("1. COUNTRY")
    print("2. REGION")
    print("3. COUNTRIES BY LANGUAGE")
    print("4. DOWNLOAD FLAG")
    print("5. HISTORY")
    print("Q. QUIT")

def get_by_name(country_name):
    res = req.get(f"https://restcountries.eu/rest/v2/name/{country_name}").json()
    if type(res)== list:
        country = res[0]

        result = [country[0]["name"], country[0]["capital"],country[0]["region"], country[0]["population"], country[0]["area"],country[0]["languages"][0]["name"],country[0]["flag"]]
        return result
    elif type(res) == dict:
        return res["message"]  

def write_csv(country):
    if type(country) == list:
        with open(f"real_path/record.csv" , "a", encoding = "uth8", newline="") as file:
            csv_writer = csv.wirter(file, delimiiter=";")
            csv_writer.writrerow(country)




def get_by_region(region_name):
    
    res = req.get(f"https://restcountries.eu/rest/v2/region/{region_name}").json()
    
    return res
    
   
def write_json(data,  jason_name):
    if type(data) == list:
        with open(f"{real_path}/{json_name}.json", "w" , encoding="utf8" ) as file:
            json.dump({"data": data}, file, ensure_ascii = False, indent=4)

def read_json(json_name):
    with open(f"{real_path}/{json_name}.json", "r" , encoding="utf8" ) as file:
        return json.load(file["data"])
def get_total_region(region):
    result = 0
    for country in region:
        result += country["population"]
        return result




def get_iso(user_language):

    for tupla in languages:
        return tupla[1].lower().find(user_language) == 0
        return tupla[0]

def get_by_language(iso_language):
    if iso_language:
        res = req.get(f"https://restcountries.eu/rest/v2/lang/{iso_language}").json()
        return f"{len(res)} countries speaks {iso_language}"
    else:
        return f"No matches for your search"




def download_flag(country):
    res = req.get(f"https://restcountries.eu/rest/v2/name/{country_name}").json()
    if type(country)== list:
        res = req.get(country[-1]).content
        with open(f"{real_path}/img/"):
            pass
            




     