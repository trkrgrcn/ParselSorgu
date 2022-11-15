import json
import requests

class Services(object):
    
    def __init__(self) -> None:
       self.tkgm_service = 'https://cbsservis.tkgm.gov.tr/megsiswebapi.v3/api'
       self.il_service =  self.tkgm_service +'/idariYapi/ilListe'
       self.ilce_service = self.tkgm_service + '/idariYapi/ilceListe/'
       self.mahalle_service = self.tkgm_service + '/idariYapi/mahalleListe/'
       self.parsel_service = '/parsel/'


        
    def getData(self, id, region = 'ilce'):
        if region=='ilce':
            response = requests.get(self.ilce_service + str(id))

        elif region=='mahalle':
            response = requests.get(self.mahalle_service + str(id))
        else:
            response = requests.get(self.il_service)
        return response



    def getParsel(self, mahid, Ada=None, Parsel=None):
        if Ada ==None:
            api = self.tkgm_service+self.parsel_service +str(mahid)+'/'+str(Parsel)
        else:
            api = self.tkgm_service+self.parsel_service +str(mahid)+'/'+str(Ada)+ '/'+str(Parsel)

        response = requests.get(api)
        return response 

