from django.shortcuts import render
from django.http import HttpResponse
from App.models import Familiar
from django.template import loader

def mostrar_familiares(self):
        
    familiares = dict
    familiares = {"familiar1": Familiar(idFamiliar= '1', nombre= 'Julia', apellido= 'Perez', fechaDeNacimiento= '1989-05-10', dni= '33234687', parentezco= 'Madre'),
                  "familiar2": Familiar(idFamiliar= '2', nombre= 'Martín', apellido= 'Lopez', fechaDeNacimiento= '1988-10-12', dni= '32659784', parentezco= 'Padre'),
                  "familiar3": Familiar(idFamiliar= '3', nombre= 'María', apellido= 'Lopez', fechaDeNacimiento= '2005-07-20', dni= '38256741', parentezco= 'Hija')}
    
    plantilla = loader.get_template('templateFamiliar.html')
    documento = plantilla.render(familiares)
        
    return HttpResponse(documento)