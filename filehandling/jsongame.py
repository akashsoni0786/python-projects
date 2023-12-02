import json

contracts = {
    'Anil':{'DOB':'11/11/1001','Favourite':'Igloo'},
    'Akash': {'DOB': '12/11/1001', 'Favourite':'Tambu'},
    'Dipu': {'DOB': '11/31/1001', 'Favourite': 'Lko'},

}
f = open("data","w+")
json.dump(contracts,f)
f.seek(0)
incontact = json.load(f)
print(incontact)
f.close()
