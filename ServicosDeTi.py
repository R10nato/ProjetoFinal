from abc import ABC, abstractmethod

class Polygon(ABC):

	@abstractmethod
	def noofsides(self):
		pass

class Triangle(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("Eu tenho 3 lados")