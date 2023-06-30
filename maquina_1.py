# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 16:36:57 2023

@author: thiag
"""

#Maquina de maq_turing 1:
    #Para a linguagem {0^n1^n|n>=0}
from proj_teoria2 import *

DIR = True
ESQ = False

alf = ['0','1']
alf_aux = ['x', 'y']

q0 = [["#","#",DIR,"q0"],['0','x',DIR,"q1"],['y','y',DIR,"q3"],[' ',' ',DIR,"q4"]]
q1 = [['1','y',ESQ,"q2"],['0','0',DIR,"q1"],['y','y',DIR,"q1"]]
q2 = [['x','x',DIR,"q0"],['0','0',ESQ,"q2"],['y','y',ESQ,"q2"]]
q3 = [['y','y',DIR,"q3"],[' ',' ',DIR,"q4"]]
q4 = []

q0 = Modelo_Estado("q0",q0)
q1 = Modelo_Estado("q1",q1)
q2 = Modelo_Estado("q2",q2)
q3 = Modelo_Estado("q3",q3)
q4 = Modelo_Estado("q4",q4,est_f=True)

maq_turing = maq_turing(alf,[q0,q1,q2,q3,q4],"q0",alf_aux,'#',' ')
maq_turing.verificaPalavra("01")
maq_turing.verificaPalavra("011")