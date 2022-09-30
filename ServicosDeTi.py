from abc import ABC, abstractmethod

class SerticosDeTi(ABC):

	id: int

	def get_id(self):
		return self.id

	def set_id(self, novoId):
		if not isinstance(self, int):
			return False
		else:
			self.id = novoId
			return True