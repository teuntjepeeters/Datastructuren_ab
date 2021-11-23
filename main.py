
def voorbeeld_dictionary():
    studenten_leeftijd = {"Laurie": {"leeftijd": 20, "vooropleiding": "VWO"},
                          "Sam": {"leeftijd": 20, "vooropleiding": "HAVO"},
                          "Gideon": [23, "Software engineering"],
                          "Lin": [17, "HAVO"],
                          "Arthur": [17, "HAVO"],
                          "Macha": [17, "HAVO"]}

    print(studenten_leeftijd["Arthur"][1])
    print(studenten_leeftijd["Gideon"][0])
    print(studenten_leeftijd["Laurie"]["vooropleiding"])

    # keys = list(studenten_leeftijd.keys())
    # values = list(studenten_leeftijd.values())

    # print(keys)
    # print(values)

    # teller = 0
    # for leeftijd in values:
    #     if leeftijd == 17:
    #         print(keys[teller])
    #     teller += 1


def read_fasta(bestandsnaam):
    """Lees fasta bestand in dictionary

    :param bestandsnaam: - str - naam van het bestand
    :return: fasta_dictionary = {header: seq, header: seq, n}
    """
    # Declareer een lege dictionary
    fasta_dictionary = {}
    # Lees het bestand in
    inFile = open(bestandsnaam, "r")
    for line in inFile:
        line=line.strip()
        # Als regel start met >: sla op in key
        if line.startswith(">"):
            key = line
        # Als hij niet start met >: sla op in 'value'/seq
        else:
            seq = line
            # Sla de key op met de value in de dictionary
            fasta_dictionary[key] = seq
        print(fasta_dictionary)


    # print de value van deze key: >NR_074491.2_Phycisphaerales
    print(fasta_dictionary[">NR_074491.2_Phycisphaerales"])
    inFile.close()


def voorbeeld_sets():
    """Voorbeelden met sets"""
    fastfood = ["pizza", "kapsalon", "kipburger", "leverworst",
                "kaas-ui-bollen", "pizza"]
    gezond_eten = ["maïs", "suiker appel", "rodebietensalade",
                   "wasabi"]
    lekker_eten = ["suiker appel", "rodebietensalade", "lasagna",
                   "wasabi"]

    fastfood = set(fastfood)
    gezond_eten = set(gezond_eten)
    lekker_eten = set(lekker_eten)

    # Union
    #print(gezond_eten.union(lekker_eten))

    # Intersection
    #print(gezond_eten.intersection(lekker_eten))

    #gezond_eten = ["maïs", "suiker appel", "rodebietensalade",
    #               "wasabi"]
    #lekker_eten = ["suiker appel", "rodebietensalade", "lasagna",
    #               "wasabi"]
    # Difference
    print(gezond_eten.difference(lekker_eten))
    print(lekker_eten.difference(gezond_eten))


def main():
    bestandsnaam = "Phycisphaerales.fasta"
    # read_fasta(bestandsnaam)
    voorbeeld_sets()


main()