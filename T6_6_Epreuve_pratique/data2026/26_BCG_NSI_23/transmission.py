class Transmission:

	def __init__(self, trame):
		self._id = None
		self._temperature = None
		self._humidite = None
		self._trame = trame
		
		self.decoder()
		
	def __repr__(self):
		""" Méthode magique pour affichage """
		return f"ID : {self._id} / Temp. : {self._temperature}°C / Hum. : {self._humidite}%"
		
	def decoder(self):
		self.decoder_id()
		self.decoder_temperature()
		self.decoder_humidite()
		
	def decoder_id(self):
		self._id = int(self._trame[0:8], 2) # int(s, 2) : conversion binaire -> décimal
		
	def decoder_temperature(self):
		pass # À compléter
		
	def decoder_humidite(self):
		pass # À compléter
		
	def get_id(self):
		return self._id
		
	def get_temperature(self):
		return self._temperature
		
	def get_humidite(self):
		return self._humidite
		
	def est_valide(self):
		return False # À compléter
