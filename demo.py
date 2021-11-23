# Dictionary eigenschappen:

# Ongeordend
# Keys zijn gelinkt aan values --> zoals een telefoonboek
# Keys binnen een dictionary zijn uniek --> values hoeft niet
# Ze kunnen als value veel verschillende datastructuren aan
# Keys en values kunnen beiden geconverteerd worden naar een lijst
# Dictionaries zijn te herkennen aan de {}

studenten_leeftijd = {"Laurie": {"leeftijd": 20, "vooropleiding": "VWO"},
                          "Sam": {"leeftijd": 20, "vooropleiding": "HAVO"},
                          "Gideon": [23, "Software engineering"],
                          "Lin": [17, "HAVO"],
                          "Arthur": [17, "HAVO"],
                          "Macha": [17, "HAVO"]}

# Sets eigenschappen

# Ongeordend
# Gemakkelijk met elkaar te vergelijken
# Alleen maar unieke waarden in sets
# Manieren van vergelijken:
#   Union - Inhoud van beiden sets wordt geretourneerd (unieke waarden!)
#   Intersection - Overlap tussen beiden sets
#   Difference - Verschillen --> alles wat niet overeenkomt