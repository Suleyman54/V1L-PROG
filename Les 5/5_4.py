bestand = open("hardlopers.txt", "w")
naam = input("hoe heet de hardloper? ")
tijd = "Tue, 26. sep., 2017 14:32"
bestand.write(tijd + " " + naam + "\n")
bestand.close()

