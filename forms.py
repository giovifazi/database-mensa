from django import forms
import datetime
from time import gmtime, strftime

class OPuno(forms.Form):
    CodPar = forms.CharField(label="CodPar", max_length=100)
    Costo = forms.CharField(label="Costo", max_length=100)
    QuantitaMerce = forms.CharField(label="QuantitaMerce", max_length=100)
    NomeRagioneSociale = forms.CharField(label="NomeRagioneSociale", max_length=100)
    TipoRagioneSociale = forms.CharField(label="TipoRagioneSociale", max_length=100)
    CodiceMerce = forms.CharField(label="CodiceMerce", max_length=100)

class OPdue(forms.Form):
    CodFiscale = forms.CharField(label="CodFiscale", max_length=100)
    Nome = forms.CharField(label="Nome", max_length=100)
    Cognome = forms.CharField(label="Cognome", max_length=100)
    ScadenzaContratto = forms.DateField(label="ScadenzaContratto", initial=datetime.date.today)
    Stipendio = forms.CharField(label="Stipendio", max_length=100)
    Ruolo = forms.CharField(label="Ruolo", max_length=100)

class OPtre(forms.Form):
    Nome = forms.CharField(label="Nome", max_length=100)
    Kcal = forms.CharField(label="Kcal", max_length=100)
    Codice = forms.CharField(label="Codice", max_length=100)
    Quantita = forms.CharField(label="Quantita", max_length=100)
    DataScadenza = forms.DateField(label="DataScadenza", initial=datetime.date.today)

class OPquattro(forms.Form):
    ID = forms.CharField(label="ID", max_length=100)
    Nome = forms.CharField(label="Nome", max_length=100)
    Cognome = forms.CharField(label="Cognome", max_length=100)
    ConCarta = forms.BooleanField(label="Carta Fedelta", required=False)

class OPcinque(forms.Form):
    CodiceCliente = forms.CharField(label="CodiceCliente", max_length=100)
    CodicePrenotazione = forms.CharField(label="CodicePrenotazione", max_length=100)
    Tavolo = forms.CharField(label="Tavolo", max_length=100)
    Ora = forms.TimeField(label="Ora", initial=strftime("%H:%M:%S", gmtime()))
    Data = forms.DateField(label="Data", initial=datetime.date.today)
    MetodoPagamento = forms.CharField(label="MetodoPagamento", max_length=100)
    NumeroPersone = forms.CharField(label="NumeroPersone", max_length=100)
    ConCarta = forms.BooleanField(label="ConCarta", required=False)

class OPsei(forms.Form):
    CodicePasto = forms.CharField(label="CodicePasto", max_length=100, required=False)
    NomeNuovoAlimento = forms.CharField(label="NomeNuovoAlimento", max_length=100, required=False)
    OPTIONS = (
            ("primo", "primo"),
            ("secondo", "secondo"),
            ("contorno", "contorno"),
            ("dolce", "dolce"),
            ("bevanda", "bevanda"),
    )
    Piatto = forms.MultipleChoiceField(label="Alimento da cambiare", widget=forms.RadioSelect, choices=OPTIONS)




class OPotto(forms.Form):
    Data = forms.DateField(label="Data", initial=datetime.date.today)

class OPnove(forms.Form):
    CodicePasto = forms.CharField(label="CodicePasto (da 1 a 3)", max_length=100)

class OPdieci(forms.Form):
    Nome  = forms.CharField(label="Nome", max_length=100)

class OPundici(forms.Form):
    Data = forms.DateField(label="Data", initial=datetime.date.today)
