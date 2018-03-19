from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.db import connection

from .forms import *

import time

# Create your views here.
# import pdb; pdb.set_trace()

# Homepage
def index(request):
    context = {}
    return render(request, 'index.html', context)

def execq(query):
    cursor = connection.cursor()
    cursor.execute(query)

    cols = [col[0] for col in cursor.description]
    res = []

    for row in cursor.fetchall():
        res.append(list(row))

    return res, cols



# First query
def First(request):
    if (request.method == 'GET'):

        #query stuff
        res, cols = execq("SELECT * FROM Fornitore")

        #form stuff
        form = OPuno()

        context = {'table' : res, 'tableh' : cols, 'form':form}
        return render(request, 'op1.html', context)

    elif (request.method == 'POST'):
        form = OPuno(request.POST)

        if (form.is_valid()):
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Fornitore(CodPar, Costo, QuantitaMerce, NomeRagioneSociale,TipoRagioneSociale,CodiceMerce) VALUES({}, {}, {}, \"{}\", \"{}\", {})".format(request.POST['CodPar'], request.POST['Costo'], request.POST['QuantitaMerce'],request.POST['NomeRagioneSociale'],request.POST['TipoRagioneSociale'],request.POST['CodiceMerce']))
            return HttpResponseRedirect('#')

# Second query
def Second(request):
    if (request.method == 'GET'):

        #query stuff
        res, cols = execq("SELECT * FROM DatiAnagrafici DA, DatiLavorativi DL WHERE  DA.CodFiscale = DL.DatiAnagrafici")

        #form stuff
        form = OPdue()

        context = {'table' : res, 'tableh' : cols, 'form':form}
        return render(request, 'op2.html', context)

    elif (request.method == 'POST'):
        form = OPdue(request.POST)

        if (form.is_valid()):
            cursor = connection.cursor()
            cursor.execute("INSERT INTO DatiAnagrafici(CodFiscale, Nome, Cognome) VALUES(\"{}\", \"{}\", \"{}\")".format(request.POST['CodFiscale'], request.POST['Nome'], request.POST['Cognome']))
            cursor.execute("INSERT INTO DatiLavorativi(DatiAnagrafici, ScadenzaContratto, Stipendio, Ruolo) VALUES(\"{}\", \"{}\", {}, \"{}\")".format(request.POST['CodFiscale'], request.POST['ScadenzaContratto'], request.POST['Stipendio'], request.POST['Ruolo']))
            return HttpResponseRedirect('#')

# Third query
def Third(request):
    if (request.method == 'GET'):

        #query stuff
        res, cols = execq("SELECT * FROM DatiNutrizionaliAlimento DN, DatiMagazzinoAlimento DM WHERE  DN.Nome = DM.Nome")

        #form stuff
        form = OPtre()

        context = {'table' : res, 'tableh' : cols, 'form':form}
        return render(request, 'op3.html', context)

    elif (request.method == 'POST'):
        form = OPtre(request.POST)

        if (form.is_valid()):
            cursor = connection.cursor()
            cursor.execute("INSERT INTO DatiMagazzinoAlimento(Codice, Quantita, Nome, DataScadenza) VALUES({}, {}, \"{}\", \"{}\")".format(request.POST['Codice'], request.POST['Quantita'], request.POST['Nome'], request.POST['DataScadenza']))
            cursor.execute("INSERT INTO DatiNutrizionaliAlimento(Nome, Kcal) VALUES(\"{}\", {})".format(request.POST['Nome'], request.POST['Kcal']))
            return HttpResponseRedirect('#')

# Fourth query
def Fourth(request):
    if (request.method == 'GET'):

        #query stuff
        res1, cols1 = execq("SELECT CC.ID AS \"IDconCarta\", CC.Nome AS \"NomeconCarta\", CC.Cognome AS \"CognomeConCarta\" FROM ClienteConCarta CC")

        res2, cols2 = execq("SELECT CS.ID AS \"IDsenzaCarta\", CS.Nome AS \"NomesenzaCarta\", CS.Cognome AS \"CognomeSenzaCarta\" FROM ClienteSenzaCarta CS")

        #form stuff
        form = OPquattro()

        context = {'table1' : res1, 'tableh1' : cols1, 'table2':res2, 'tableh2':cols2, 'form':form}
        return render(request, 'op4.html', context)

    elif (request.method == 'POST'):
        form = OPquattro(request.POST)

        if (form.is_valid()):
            cursor = connection.cursor()
            if ('ConCarta' in request.POST):
                cursor.execute("INSERT INTO ClienteConCarta(ID, Nome, Cognome) VALUES({}, \"{}\", \"{}\")".format(request.POST['ID'], request.POST['Nome'], request.POST['Cognome']))
            else:
                cursor.execute("INSERT INTO ClienteSenzaCarta(ID, Nome, Cognome) VALUES({}, \"{}\", \"{}\")".format(request.POST['ID'], request.POST['Nome'], request.POST['Cognome']))

            return HttpResponseRedirect('#')

# Fifth query
def Fifth(request):
    if (request.method == 'GET'):

        #query stuff
        res1, cols1 = execq("SELECT * FROM PrenotazioneOnline")
        res2, cols2 = execq("SELECT * FROM Fruizione1 F, ClienteSenzaCarta C WHERE F.ClienteSenzaCarta = C.ID")
        res3, cols3 = execq("SELECT * FROM Fruizione2 F, ClienteConCarta C WHERE F.ClienteConCarta = C.ID")

        #form stuff
        form = OPcinque()

        context = {'table1' : res1, 'tableh1' : cols1,
                   'table2' : res2, 'tableh2' : cols2,
                   'table3' : res3, 'tableh3' : cols3,
                   'form':form}

        return render(request, 'op5.html', context)

    elif (request.method == 'POST'):
        form = OPcinque(request.POST)

        if (form.is_valid()):
            cursor = connection.cursor()

            if ('ConCarta' in request.POST):
                cursor.execute("INSERT INTO PrenotazioneOnline(CodicePrenotazione, Tavolo, Ora, Data, MetodoPagamento, NumPersone) VALUES({}, {}, \"{}\", \"{}\", \"{}\", {})".format(request.POST['CodicePrenotazione'], request.POST['Tavolo'], request.POST['Ora'], request.POST['Data'], request.POST['MetodoPagamento'], request.POST['NumeroPersone']))
                cursor.execute("INSERT INTO Fruizione2(PrenotazioneOnline, ClienteConCarta) VALUES({}, {})".format(request.POST['CodicePrenotazione'], request.POST['CodiceCliente']))
            else:
                cursor.execute("INSERT INTO PrenotazioneOnline(CodicePrenotazione, Tavolo, Ora, Data, MetodoPagamento, NumPersone) VALUES({}, {}, \"{}\", \"{}\", \"{}\", {})".format(request.POST['CodicePrenotazione'], request.POST['Tavolo'], request.POST['Ora'], request.POST['Data'], request.POST['MetodoPagamento'], request.POST['NumeroPersone']))
                cursor.execute("INSERT INTO Fruizione1(PrenotazioneOnline, ClienteSenzaCarta) VALUES({}, {})".format(request.POST['CodicePrenotazione'], request.POST['CodiceCliente']))

            return HttpResponseRedirect('#')

def sixsupport(nomecibo, request, cursor):
    # nomecibo = "Primo"
    cursor.execute("SELECT {} FROM PastoCompleto WHERE CodicePasto = {}".format(nomecibo, request.POST['CodicePasto']))
    time.sleep(0.2)
    for r in cursor.fetchall():
        cibo = list(r) #cibo = ['Bistecca']
    cursor.execute("UPDATE PastoCompleto SET Kcal = Kcal - (SELECT Kcal FROM DatiNutrizionaliAlimento WHERE \"{}\" = DatiNutrizionaliAlimento.Nome) WHERE PastoCompleto.CodicePasto = {} ".format(cibo[0], request.POST['CodicePasto']))
    time.sleep(0.2)
    cursor.execute("UPDATE PastoCompleto SET {} = \"{}\" WHERE PastoCompleto.CodicePasto = {} ".format(nomecibo, request.POST['NomeNuovoAlimento'], request.POST['CodicePasto']))
    time.sleep(0.2)
    cursor.execute("UPDATE PastoCompleto SET Kcal = Kcal + (SELECT Kcal FROM DatiNutrizionaliAlimento WHERE \"{}\" = DatiNutrizionaliAlimento.Nome) WHERE PastoCompleto.CodicePasto = {} ".format(request.POST["NomeNuovoAlimento"],request.POST['CodicePasto']))
    time.sleep(0.2)

# Sixth query
def Sixth(request):
    if (request.method == 'GET'):

        #query stuff
        res, cols = execq("SELECT * FROM PastoCompleto")
        res2, cols2 = execq("SELECT * FROM DatiMagazzinoAlimento, DatiNutrizionaliAlimento WHERE DatiMagazzinoAlimento.Nome = DatiNutrizionaliAlimento.Nome")

        #form stuff
        form = OPsei()

        context = {'table' : res, 'tableh' : cols,
                   'table2': res2, 'tableh2' : cols2,
                   'form':form}
        return render(request, 'op6.html', context)

    elif (request.method == 'POST'):
        form = OPsei(request.POST)

        cursor = connection.cursor()
        if (request.POST["Piatto"] == 'primo'):
            sixsupport("Primo", request, cursor)

        if (request.POST["Piatto"] == 'secondo'):
            sixsupport("Secondo", request, cursor)

        if (request.POST["Piatto"] == 'contorno'):
            sixsupport("Contorno", request, cursor)

        if (request.POST["Piatto"] == 'dolce'):
            sixsupport("Dolce", request, cursor)

        if (request.POST["Piatto"] == 'bevanda'):
            sixsupport("Bevanda", request, cursor)

        return HttpResponseRedirect('#')

def Seventh(request):
        res1, cols1 = execq("SELECT * FROM Pagamento1")
        res2, cols2 = execq("SELECT * FROM Pagamento2")
        res3, cols3 = execq("SELECT SUM(Prezzo) AS EntrateMese FROM (SELECT * FROM Pagamento1 AS P1 WHERE MONTH(P1.Data)=MONTH(CURDATE()) UNION SELECT * FROM Pagamento2 AS P2 WHERE MONTH(P2.Data)=MONTH(CURDATE())) AS EntrateCorrenti JOIN PastoCompleto ON CodicePasto=PastoCompleto")

        context = {'table1' : res1, 'tableh1' : cols1, 'table2':res2, 'tableh2':cols2, 'table3':res3, 'tableh3':cols3}

        return render(request, 'op7.html', context)

def Eigth(request):
    if (request.method == 'GET'):

        #form stuff
        form = OPotto()

        context = {'form':form}
        return render(request, 'op8.html', context)

    elif (request.method == 'POST'):
        form = OPotto(request.POST)

        if (form.is_valid()):
            cursor = connection.cursor()
            res, cols= execq("SELECT * FROM Consegna JOIN  DatiMagazzinoAlimento ON  Consegna.DatiMagazzinoAlimento = DatiMagazzinoAlimento.Codice  WHERE Data = \"{}\" " .format(request.POST['Data']))
            form2 = OPotto()
            context = {'table': res, 'tableh':cols, 'form':form2}
            return render(request, 'op8.html', context)

def Nineth(request):
    if (request.method == 'GET'):

        #form stuff
        form = OPnove()

        context = {'form':form}
        return render(request, 'op9.html', context)

    elif (request.method == 'POST'):
        form = OPnove(request.POST)

        if (form.is_valid()):
            cursor = connection.cursor()
            res, cols= execq("SELECT * FROM PastoCompleto WHERE CodicePasto = {}".format(request.POST['CodicePasto']))
            form2 = OPnove()
            context = {'table': res, 'tableh':cols, 'form':form2}
            return render(request, 'op9.html', context)

def Tenth(request):
    if (request.method == 'GET'):

        #form stuff
        form = OPdieci()

        context = {'form':form}
        return render(request, 'op10.html', context)

    elif (request.method == 'POST'):
        form = OPdieci(request.POST)

        if (form.is_valid()):
            cursor = connection.cursor()
            res, cols= execq("SELECT Quantita FROM DatiMagazzinoAlimento WHERE Nome = \"{}\"".format(request.POST['Nome']))
            form2 = OPdieci()
            context = {'table': res, 'tableh':cols, 'form':form2}
            return render(request, 'op10.html', context)


def Eleventh(request):
            res, cols= execq("SELECT Nome, DataScadenza FROM DatiMagazzinoAlimento WHERE DataScadenza <= DATE_ADD(CURDATE(), INTERVAL 3 DAY) AND DataScadenza >= CURDATE()")
            context = {'table': res, 'tableh':cols}
            return render(request, 'op11.html', context)


def Twelveth(request):
            res, cols= execq("SELECT AVG(Punti) FROM CartaFedelta")
            context = {'table': res, 'tableh':cols}
            return render(request, 'op12.html', context)

def Thirteenth(request):
            res, cols= execq("SELECT DL.ScadenzaContratto, DL.Ruolo, DA.Nome, DA.Cognome FROM DatiLavorativi AS DL, DatiAnagrafici AS DA WHERE DL.ScadenzaContratto <= DATE_ADD(CURDATE(), INTERVAL 30 DAY) AND DA.CodFiscale = DL.DatiAnagrafici")
            context = {'table': res, 'tableh':cols}
            return render(request, 'op13.html', context)







