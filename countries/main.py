import requests as req
import funcs



# res = req.get("https://restcountries.eu/rest/v2/all").json()
# print(res[0])




 

user = 0
while user != "Q":
    funcs.menu()
    user = input("Select: ")


    if user == "1": #by countries
        user = input("Country: ")
        print(funcs.get_by_name(user))
        result = funcs.get_by_name(user)
        funcs.write_csv(result)
    elif user == "2": #by region
        user = input("Region: ")
        result = funcs.get_population(funcs.read_json(f"{user}.json"))
      
        print(result)
    elif user == "3":
        language = input("Language: ")
        iso_language = (funcs.get_iso(language))
        print(funcs.get_by_language(iso_language))
    elif user == "4":
        country_name = input("Country: ")
        coutnry_name = funcs.get_by_name(country_name)
        funcs.get_flag(country_name)
        flag = funcs.get_flag(country_name)
        print(flag)
        



    elif user =="q" or user == "Q":  
        quit  
      

        