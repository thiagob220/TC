# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 21:18:36 2023

@author: thiag
"""
#a estrutura básica da máquina de turing: 
    #alfabeto alf, que a máquina irá receber
    #estados_q, que são os estados que a máquina irá receber
    #est_inicial, que é o estado por onde começar
    #alfabeto auxiliar ou alf_auxiliar, para as transições
    #o símbolo inicial
    #o símbolo vazio
    #a fita
    #a posição da cabeça
    #o estado atual de atuação
    
from proj_teoria1 import *

class maq_turing():
    
    def __init__(self, alf, estados_q, est_inicial, alf_aux, s_inic, s_vazio):
        self.alf = alf
        self.estados_q = estados_q
        self.est_inicial = est_inicial
        self.alf_aux = alf_aux
        self.s_inic = s_inic
        self.s_vazio = s_vazio
        self.fita = []
        self.cabeca = 0
        self.e_at = self.est_inicial
        
        self.estados_q.append(Modelo_Estado('X'))
        
        #para a função que verifica a palavra, fornece a palavra
        #e também um verificador de permissão de continuidade
        #(delimitador de parada)
        
    def verificaPalavra(self, palavra, step=True):
        self.cabeca = 0
        self.fita = self.s_inic + palavra + self.s_vazio
        self.e_at = self.est_inicial
        
        if step:
            print("Palavra: "+palavra)
        
        while 0 <= self.cabeca < len(self.fita):
            output = self.executaTransicao()
            if step:
                print(output)
            
        if step:
            if self.recebeEstado(self.e_at).est_f:
                print("palavra aceita\n\n")
            else:
                print("palavra rejeitada\n\n")
            
            return self.fita[-1:1]
    
    def executaTransicao(self):
        output = "Programa: ("+self.e_at+","+self.fita[self.cabeca]+") = "
        trans = self.recebeEstado(self.e_at).getTrans(self.fita[self.cabeca])
        if not self.verificaSimbolo(self.alf,self.fita[self.cabeca]):
            print(self.fita[self.cabeca]+" nao pertence ao alf!")
            self.cabeca = len(self.fita)
        if trans is not None:
            if trans[1] is not None: 
                if not self.verificaSimbolo(self.alf_aux,trans[1]):
                    print(self.fita[self.cabeca]+" nao pertence ao alf!")
                    self.cabeca = len(self.fita)
                
                aux = list(self.fita)
                aux.pop(self.cabeca)
                aux.insert(self.cabeca,trans[1])
                self.fita = ''.join(aux)
            if trans[2]:
                self.cabeca += 1
            else:
                self.cabeca -= 1
   
            if trans[3] is not None:
                self.e_at = trans[3]
            else:
                self.e_at = 'X'
        else:
            self.cabeca = len(self.fita)
            self.e_at = 'X'
            
        output += self.e_at
        
        return output
        
    def recebeEstado(self,name):
        for state in self.estados_q:
            if state.getName() is name:
                return state
                break
        return None
    def verificaSimbolo(self,alf,s):
        if s is self.s_inic or self.s_vazio:
            return True 
        for i in alf:
            if i is s:
                return True   
        return False
    
    
    

                
    
    
        
        