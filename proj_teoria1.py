# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 21:12:02 2023

@author: thiag
"""

#projeto de teoria
#parte 1 : criar o estado
#o estado é uma classe referenciada com nome, as transições que são
#um vetor e uma condição atribuída de final, para indicar que aquele
#é o estado final

class Modelo_Estado():
    def __init__(self, nome, trans_molde = [], est_f=False):
        self.nome = nome
        self.trans_molde = trans_molde
        self.est_f= est_f
        
    #def string(self):
        #return self.nome
    
    def getTrans(self, s):
        for trans_molde in self.trans_molde:
            if trans_molde[0] is s:
                return trans_molde
        return None
    
    def getName(self):
        return self.nome
    
    
    
    