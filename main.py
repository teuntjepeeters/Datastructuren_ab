

def main():
    studenten_leeftijd = {"Laurie": {"leeftijd":20,"vooropleiding": "VWO"},
                          "Sam": {"leeftijd":20, "vooropleiding": "HAVO"},
                          "Gideon": [23, "Software engineering"],
                          "Lin": [17, "HAVO"],
                          "Arthur": [17, "HAVO"],
                          "Macha": [17, "HAVO"]}

    print(studenten_leeftijd["Arthur"][1])
    print(studenten_leeftijd["Gideon"][0])
    print(studenten_leeftijd["Laurie"]["vooropleiding"])

    # keys = list(studenten_leeftijd.keys())
    # values = list(studenten_leeftijd.values())

    #print(keys)
    #print(values)

    # teller = 0
    # for leeftijd in values:
    #     if leeftijd == 17:
    #         print(keys[teller])
    #     teller += 1


main()