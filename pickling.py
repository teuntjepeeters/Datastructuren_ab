import pickle


def voorbeeld_pickle():
    studenten = {"Laurie": "Kubussen",
                 "Hans": "Tekenen",
                 "Ryan": "Jiu jitsu",
                 "Jeremaih": "Krachttraining",
                 "Franck": "Gitaar + varianten"}

    wegschrijven = open("studenten", "wb")
    pickle.dump(studenten, wegschrijven)
    wegschrijven.close()

    openen = open("studenten", "rb")
    stud = pickle.load(openen)
    print(stud)
    print(studenten)


def main():
    voorbeeld_pickle()


main()