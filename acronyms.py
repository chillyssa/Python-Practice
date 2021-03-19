acronyms = ["LOL", "IDK", "SMH", "TBH", "OMG", "AFK"]

for acronym in acronyms:
    print(acronym)

#lists are great, but dictionaires with key-value-pairs are more robust

acronyms= { 
    "LOL": "laugh out loud", 
    "IDK": "I don't know", 
    "SMH": "shaking my head",
    "TBH": "to be honest", 
    "OMG": "oh my god", 
    "AFK": "away from keyboard" 
}

sentence = "IDK " + "what happened " + "TBH"
translation = acronyms.get("IDK")+ " what happened " + acronyms.get("TBH")
print("sentence:", sentence)
print("translation:", translation)