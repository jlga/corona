import dateutil.parser

#Spaltennamen:
IdBundesland = 0
Bundesland = 1
Landkreis = 2
Altersgruppe = 3
Geschlecht = 4
AnzahlFall = 5
AnzahlTodesfall = 6
ObjectId = 7
Meldedatum = 8
LandkreisID = 9


vdatum = dateutil.parser.parse("2020-03-24T00:00:00.000Z")

summe = 0
altersgruppen = dict()
with open("RKI_COVID19.csv") as f:
    spaltenüberschriften = next(f)
    for line in f:
        spalten = line.split(",")
        datum = dateutil.parser.parse(spalten[Meldedatum])
        if datum > vdatum:
            pass
        else:
            summe+= int(spalten[AnzahlFall])
            if spalten[Altersgruppe] in altersgruppen:
                altersgruppen[spalten[Altersgruppe]] += int(spalten[AnzahlFall])
            else:
                altersgruppen[spalten[Altersgruppe]] = int(spalten[AnzahlFall])
        
print("Summe der Infizierten:", summe)
for ag in sorted(altersgruppen.keys()):
    anzahl = altersgruppen[ag]
    print(f"{ag}: {anzahl}")

