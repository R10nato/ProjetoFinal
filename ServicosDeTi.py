from abc import ABC, abstractmethod

class SerticosDeTi(ABC):
	id: int

	def get_id(self):
		return id

	def set_id(self):
		input("")

	# @abstractmethod
	# def noofsides(self):
	# 	pass

class ServicoDeSoftware(ABC):

	# overriding abstract method
	def noofsides(self):
		print("Eu tenho 3 lados")