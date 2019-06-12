#!/bin/python
#################################################################################################

#importe aqui os pacotes necessários
import numpy as np

#################################################################################################

#defina aqui as funções que serão utilizadas no código

#exibe os valores do dicionario de parametros
def read_params(a,j=''):
  if j=='':
    print "### Printing GUI parameters ###"
  for i in a:
    if (type(a[i])!=type({'a':1})):
      print j+"['"+str(i)+"']="+str(a[i])+" type: "+str(type(a[i]))
    else:
      read_params(a[i],j+"['"+str(i)+"']")

#################################################################################################

class template: #aqui vai o nome do plugin
	def __init__(self):
		pass

#################################################################################################

	def initialize(self, params):
		self.params = params
		#executando a função exibe os valores do dicionario de parametros
		read_params(params) #para não printar comente essa linha
		return True

#################################################################################################

	def execute(self):
		#aqui vai o código
		print("Eu funciono") #apague essa linha
		return True

#################################################################################################
	
	def finalize(self):
		return True

	def name(self):
		return "template" #aqui vai o nome do plugin

#################################################################################################

def get_plugins():
	return ["template"] #aqui vai o nome do plugin
