from django.shortcuts import render
from django.http import HttpResponse
from App.models import Familiar
from django.template import loader

def mostrar_familiares(self):
    
    familiar_uno = Familiar(idFamiliar= '1', nombre= 'Julia', apellido= 'Perez', fechaDeNacimiento= '10/05/1989', dni= '33234687', parentezco= 'Madre')
    familiar_dos = Familiar(idFamiliar= '2', nombre= 'Martín', apellido= 'Lopez', fechaDeNacimiento= '12/10/1988', dni= '32659784', parentezco= 'Padre')
    familiar_tres = Familiar(idFamiliar= '3', nombre= 'María', apellido= 'Lopez', fechaDeNacimiento= '20/07/2005', dni= '38256741', parentezco= 'Hija')
    
    familiar_uno.save()
    familiar_dos.save()
    familiar_tres.save()
    
    familiares = {'madre': familiar_uno}
    familiares = {'padre': familiar_dos}
    familiares= {'hija': familiar_tres}
    
    plantilla = loader.get_template('templateFamiliar.html')
    documento = plantilla.render(familiares)
        
    return HttpResponse(documento)