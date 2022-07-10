from Loader import Loader

class OpenObedLoader:
	def __init__(self):
		self.l = Loader()
	
	def loadStickers(self, firstid = 4500, lastid = 4510):
		self.l.loadStickers(firstid, lastid)
	
	def loadGift(self, id = 1):
		self.l.loadGift(id)

if __name__ == "__main__":
	app = OpenObedLoader()
	app.loadStickers(4630, 4640)