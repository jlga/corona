import dateutil.parser
import urllib.request

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


urllib.request.urlretrieve("https://opendata.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0.csv", "RKI_COVID19.csv")

vdatum = dateutil.parser.parse("2020-04-24T00:00:00.000Z")

summe = 0
altersgruppen = dict()
lks = dict() #Landkreise
tage = dict()
with open("RKI_COVID19.csv") as f:
    spaltenüberschriften = next(f)
    for line in f:
        spalten = line.split(",")
        datum = dateutil.parser.parse(spalten[Meldedatum])
        if datum > vdatum:
            pass
        else:
            summe+= int(spalten[AnzahlFall])
            tag = spalten[Meldedatum]
            tage[tag] = 1
            try:
                lks[spalten[Landkreis]]
            except Exception as e:
                lks[spalten[Landkreis]] = dict()
            if tag in lks[spalten[Landkreis]]:
                lks[spalten[Landkreis]][tag] += int(spalten[AnzahlFall])
            else:
                lks[spalten[Landkreis]][tag] = int(spalten[AnzahlFall])
alleLKs = lks.keys()
LK_summen = dict.fromkeys(lks.keys(),0)
with open(".\\output\\covidLK_timeseries.csv", "w+") as f:
    f.write("Datum")
    for lk in alleLKs:
        f.write(";" + lk)
    f.write("\n")
    for tag in sorted(tage):
        for k_Landkreis in lks:
            LK_summen[k_Landkreis] += lks[k_Landkreis].get(tag, 0)
        dieses_datum = dateutil.parser.parse(tag)
        f.write(dieses_datum.strftime("%Y-%m-%d %H:%M:%S"))
        for lk in alleLKs:
            f.write(";" + str(LK_summen[lk]))
        f.write("\n")
        print(dieses_datum.strftime("%d.%m.%Y:"), sum(LK_summen.values()))
print("Gesamte Fälle:", sum(LK_summen.values()))
