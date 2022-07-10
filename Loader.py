import requests, shutil, os

class Loader:
	def __init__(self):
		self.doing = True
		self.folder = ""
	
	def loadStickers(self, firstid = 4500, lastid = 4510):
		self.folder = "Stickers"
		self.crntid = firstid
		
		while self.doing:
			r = requests.get(f"http://vk.com/sticker/1-{self.crntid}-512")
			print(f"[STICKERID-{self.crntid}]: {r.status_code}")
			if not lastid == self.crntid:
				with open(f"{os.getcwd()}/Downloads/{self.folder}/{self.crntid}.png", "wb") as f:
					r.raw.decode_content = True
					for chunk in r:
						f.write(chunk)
				
				self.crntid += 1
			else:
				self.doing = False
	
	def loadGift(self, id):
		self.folder = "Gifts"
		self.id = id
		
		while self.doing:
			r = requests.get(f"http://vk.com/sticker/4-{self.id}-512")
			print(f"[GIFTID-{self.id}]: {r.status_code}")
			if r.status_code == 200:
				with open(f"{os.getcwd()}/Downloads/{self.folder}/{self.id}.png", "wb") as f:
					r.raw.decode_content = True
					for chunk in r:
						f.write(chunk)
			self.doing = False