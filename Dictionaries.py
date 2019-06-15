#######################################################
# Working wiht List and Dictionaries                  #
#                                                     #
#######################################################
import json
#import yaml

dict = [
        {
            "Name":"Jorge",
            "LastName":"Rodriguez"
        },
        {
            "Name":"Daniela",
            "LastName":"Rodriguez-Chavez"
        },
        {
            "Name":"Susna",
            "LastName":"Chavez"
        }
        ]

print ("=" *80)
text = "Working wiht Dictionaries to Understand JSON and YAML"
print (text.upper())
print ("=" *80)
x = 0
while x < len(dict):
    print ("*" *50)
    if (dict[x].get('Name') == "Jorge"):
        print (".")
        dict[x]["Name"] = "Jorge E."
    print (dict[x]["Name"])
    print (dict[x]["LastName"])
    print (dict[x].items())
    print (dict[x].keys())
    keys = dict[x].keys()
    print (type(keys))
    print (dict[x].get('Name'))
    print ("*" *50)
    x += 1
print ("-" *50)
for key,val in dict[0].items():
    print (key, "=>", val)
print ("-" *50)
keys_list = []
for key in dict[0].keys():
    #print (key)
    keys_list.append(key)
print ("-" *50)
print ("Key Names:")
print (keys_list[0])
print (keys_list[1])
print ("Deleting Name Key....")
del dict[0]["Name"]
print (dict[0])


