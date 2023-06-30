# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 21:48:29 2023

@author: thiag
"""

#Maquina de maq_turing 2:
    #Para a linguagem {0^m1^n0|m,n>=1}
from proj_teoria2 import *

DIR = True
ESQ = False

alf = ['0','1']
alf_aux = ['x', 'y']

q0 = [["#","#",DIR,"q0"],['0','x',DIR,"q1"], ['y', 'y', DIR, "q3"]]
q1 = [['1','y',DIR,"q2"],['0','x',DIR,"q1"]]
q2 = [['0','x',ESQ,"q0"],['1','y',DIR,"q2"]]
q3 = [['y','y',DIR,"q3"],[' ',' ',DIR,"q4"], ['x', 'x', DIR, "q3"]]
q4 = []

q0 = Modelo_Estado("q0",q0)
q1 = Modelo_Estado("q1",q1)
q2 = Modelo_Estado("q2",q2)
q3 = Modelo_Estado("q3",q3)
q4 = Modelo_Estado("q4",q4,est_f=True)


maq_turing = maq_turing(alf,[q0,q1,q2,q3,q4],"q0",alf_aux,'#',' ')
maq_turing.verificaPalavra("01")
maq_turing.verificaPalavra("010")
maq_turing.verificaPalavra("0011")
maq_turing.verificaPalavra("00110")
maq_turing.verificaPalavra("00000111110")
maq_turing.verificaPalavra("0010")
maq_turing.verificaPalavra("0110")
maq_turing.verificaPalavra("00")
maq_turing.verificaPalavra("")

