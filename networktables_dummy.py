class NetworkTables:
	@staticmethod
	def initialize(server='localhost'):
		print('NetworkTables initialized with server ' + server)
	
	@staticmethod
	def getTable(table):
		print('Getting table ' + table)
		return SmartDashboard(table)

class SmartDashboard:
	def __init__(self, name):
		self.table = name
		self.values = dict()
	# Put data
	def putData(self, key, val):
		self.values[key] = val
	def putNumber(self, key, val):
		self.putData(key, val)
	def putBoolean(self, key, val):
		self.putData(key, val)
	def putString(self, key, val):
		self.putData(key, val)
	
	# Get data
	def getData(self, key, default):
		if key in self.values:
			return self.values[key]
		else:
			return default
	def getNumber(self, key, default):
		return self.getData(key, default)
	def getBoolean(self, key, default):
		return self.getData(key, default)
	def getString(self, key, default):
		return self.getData(key, default)