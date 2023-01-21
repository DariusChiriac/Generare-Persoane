from xml.dom import minidom
FILE_BARBATI = "C:\\Users\\raoul\\PycharmProjects\\File_project\\PrenumeBaieti.txt"
FILE_FEMEI = "C:\\Users\\raoul\\PycharmProjects\\File_project\\PrenumeFete.txt"
FILE_NUME_FAMILIE = "C:\\Users\\raoul\\PycharmProjects\\File_project\\NumeFamilieF.txt"
criteriu_lungime = lambda nume:len(nume)
def nrVocale(s):
    s=s.lower()
    kV = 0
    vocale =['a','e','i','o','u','ă','â','î','y']
    for litera in s:
        if litera in vocale:
            kV = kV + 1
    return kV

def nrConsoane(s):
    s = s.lower()
    kV = 0
    consoane = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','ș','t','ț','v','w','x','z']
    for litera in s:
        if litera in consoane:
            kV = kV + 1
    return kV

def nrDiacritice(s):
    s=s.lower()
    kV = 0
    diacritice = ['ă','â','î','ș','ț']
    for litera in s:
        if litera in diacritice:
            kV = kV + 1
    return kV

def prenumeXMLGenerator():
    f1 = open(FILE_BARBATI,"r",encoding="utf-8-sig")
    f2 = open(FILE_FEMEI,"r",encoding="utf-8-sig")
    if f1 == None or f2 == None:
        raise Exception("Fisierul nu a putut fi deschis!")
    else:
        listaBarbati=[]
        for line in f1:
            listaBarbati.append(line.strip())
        f1.close()
        listaBarbati=sorted(listaBarbati,key=criteriu_lungime)
        print(listaBarbati)
        listaBarbati=sorted(listaBarbati,key=lambda s:nrDiacritice(s),reverse=True)
        print(listaBarbati)
        listaBarbati=sorted(listaBarbati,key=lambda s:nrVocale(s),reverse=True)
        print(listaBarbati)
        listaBarbati=sorted(listaBarbati,key=lambda s:nrConsoane(s),reverse=True)
        print(listaBarbati)
        listaFemei=[]
        for line in f2:
            listaFemei.append(line.strip())
        f2.close()
        listaFemei = sorted(listaFemei, key=criteriu_lungime)
        print(listaFemei)
        listaFemei = sorted(listaFemei, key=lambda s: nrDiacritice(s), reverse=True)
        print(listaFemei)
        listaFemei = sorted(listaFemei, key=lambda s: nrVocale(s), reverse=True)
        print(listaBarbati)
        listaFemei = sorted(listaFemei, key=lambda s: nrConsoane(s), reverse=True)
        print(listaFemei)
        root = minidom.Document()
        listaPrenume = root.createElement("listaPrenume")
        root.appendChild(listaPrenume)
        for p in listaBarbati:
            e = root.createElement("prenume")
            e.setAttribute("lungime",str(len(p)))
            e.setAttribute("sex","M")
            e.setAttribute("consoane",str(nrConsoane(p)))
            e.setAttribute("vocale",str(nrVocale(p)))
            e.setAttribute("diacritice",str(nrDiacritice(p)))
            nodText=root.createTextNode(p)
            e.appendChild(nodText)
            listaPrenume.appendChild(e)
        for p in listaFemei:
            e = root.createElement("prenume")
            e.setAttribute("lungime,",str(len(p)))
            e.setAttribute("sex","F")
            e.setAttribute("consoane",str(nrConsoane(p)))
            e.setAttribute("vocale" ,str(nrVocale(p)))
            e.setAttribute("diacritice",str(nrDiacritice(p)))
            nodText=root.createTextNode(p)
            e.appendChild(nodText)
            listaPrenume.appendChild(e)
        xml_sr  = root.toprettyxml(indent="\t")
        file = "premume.xml"
        with open(file,"w",encoding="utf-8-sig") as f:
            f.write(xml_sr)
            f.close()

def numeFamilieXMLGenerator():
    f3 = open(FILE_NUME_FAMILIE, "r", encoding="utf-8-sig")
    if f3 == None:
        raise Exception("Fisierul nu a putut fi deschis!")
    else:
        listaNumeFamilie=[]
        for line in f3:
            listaNumeFamilie.append(line.strip())
        f3.close()
        root=minidom.Document()
        listaFamilie=root.createElement("lista nume familie")
    root.appendChild(listaFamilie)
    for n in listaNumeFamilie:
        e = root.createElement("nume familie")
        e.setAttribute("lungime,", str(len(n)))
        e.setAttribute("consoane", str(nrConsoane(n)))
        e.setAttribute("vocale", str(nrVocale(n)))
        e.setAttribute("diacritice", str(nrDiacritice(n)))
        nodText = root.createTextNode(n)
        e.appendChild(nodText)
        listaFamilie.appendChild(e)
    xml_sr = root.toprettyxml(indent="\t")
    file = "numeFamilie.xml"
    with open(file, "w", encoding="utf-8-sig") as f:
        f.write(xml_sr)
        f.close()


prenumeXMLGenerator()
numeFamilieXMLGenerator()





