class Event():
	"""docstring for Event"""
	events = {}

def __init__(self):
	self.name = ""
	self.category = ""
	self.location = ""
	self.dateTime = ""

	self.events = {self.name: {'category' : self.category, 'location' : self.location, 'dateTime' : self.dateTime}}


def createEvent(self, name, cate, locat, dt):
	if name != "" and cate != "" and locat != "" and dt != "" :
		self.events = {name : {'category' : cate, 'location' : locat, 'dateTime' : dt }}
	else:
		print ("sorry the event exist")
def deleteEvent(self, name):
	if name in self.events.key():
		self.events.pop(name)
	else:
		print ("sorry the event dont exist")

def modifyEvent(self, name, cate, locat, dt):
	if name != "" and cate != "" and locat != "" and dt != "" :
		if name in self.events.key():
			self.events = {name : {'category' : cate, 'location' : locat, 'dateTime' : dt }}
	else:
		return "sorry the event dont exist"

def viewEvent(self):
	return self.event.item()

def filterEvents(self, locat):
	for i in self.event.keys():

		return self.event[i][location]