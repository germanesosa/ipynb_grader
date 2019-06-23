from __future__ import print_function
from notebook import notebookapp
from ipywidgets import *
from IPython.display import display, HTML
import urllib
import json
import os
import ipykernel
import pandas as pd

def notebook_path():
    connection_file = os.path.basename(ipykernel.get_connection_file())
    kernel_id = connection_file.split('-', 1)[1].split('.')[0]
    for srv in notebookapp.list_running_servers():
        try:
            if srv['token']=='' and not srv['password']:  # No token and no password, ahem...
                req = urllib.request.urlopen(srv['url']+'api/sessions')
            else:
                req = urllib.request.urlopen(srv['url']+'api/sessions?token='+srv['token'])
            sessions = json.load(req)
            for sess in sessions:
                if sess['kernel']['id'] == kernel_id:
                    return os.path.join(srv['notebook_dir'],sess['notebook']['path'])
        except:
            pass
    return None   
        
class Calificacion:
  
    def __init__(self,grupos):
        self.criterios, self.puntos, self.puntosMax, self.rubricas, self.col1, self.col2= [], [], [], [], [], []
        self.grupos = grupos
        self.puntajeMax, self.puntaje, self.nota = 0,0,0
        NOTEBOOK_FULL_PATH = notebook_path()
        k = NOTEBOOK_FULL_PATH.rfind("/")
        self.nombre = NOTEBOOK_FULL_PATH[k+1:-6]+'_rubrica.csv'
        for grupo,criterios in grupos.items():
            for criterio, rubrica in criterios.items():
                self.criterios.append(criterio)
                self.puntos.append(0)
                self.puntosMax.append(rubrica[-1][1])
                self.rubricas.append(rubrica)
                self.puntajeMax += rubrica[-1][1]
                self.col1.append(grupo)
                self.col2.append(criterio)
    
    def Actualizar(self,indice,nota):
        self.puntos[indice] = nota
        self.Puntuar()
        
    def DataFrame(self):
        self.df = pd.DataFrame({'Grupo': self.col1, 'Criterio': self.col2, 'Puntos': self.puntos, 'Sobre': self.puntosMax})      
    
    def Exportar(self):    
        self.df.to_csv(self.nombre, sep=',', encoding='utf-8')    

    def Importar(self):    
        try:
            puntos = pd.read_csv(self.nombre, sep=',', encoding='utf-8', engine='python', usecols=['Puntos']) 
            self.puntos = list(puntos.iloc[:,0])
            self.Puntuar()               

        except FileNotFoundError: 
            pass
    
        
    def Puntuar(self):
        self.puntaje = 0
        for puntos in self.puntos:
            self.puntaje += puntos
        self.nota = 10*self.puntaje/self.puntajeMax   