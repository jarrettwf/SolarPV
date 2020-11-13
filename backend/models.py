from django.db import models

class Client(models.Model):
	clientID = models.CharField(max_length=20)
	clientName = models.CharField(max_length=20)
	clientType = models.CharField(max_length=20)

class testStandard(models.Model):
	standardID = models.CharField(max_length=20)
	standardName = models.CharField(max_length=20)
	description = models.CharField(max_length=20)
	publishedDate = models.CharField(max_length=20)

class Product(models.Model):
	modelNumber = models.CharField(max_length=20)
	productName = models.CharField(max_length=20)
	cellTechnology = models.CharField(max_length=20)
	cellManufacturer = models.CharField(max_length=20)
	numberOfCells = models.CharField(max_length=20)
	cellsInSeries = models.CharField(max_length=20)
	seriesStrings = models.CharField(max_length=20)
	numberOfDiodes = models.CharField(max_length=20)
	productLength = models.CharField(max_length=20)
	productWidth = models.CharField(max_length=20)
	productWeight = models.CharField(max_length=20)
	superstateType = models.CharField(max_length=20)
	superstateManufacturer = models.CharField(max_length=20)
	substrateType = models.CharField(max_length=20)
	substrateManufacturer = models.CharField(max_length=20)
	frameType = models.CharField(max_length=20)
	frameAdhesive = models.CharField(max_length=20)
	encapsulateType = models.CharField(max_length=20)
	encapsulantManufacturer = models.CharField(max_length=20)
	junctionType = models.CharField(max_length=20)
	junctionManufacturer = models.CharField(max_length=20)

class testSequence(models.Model):
	sequenceID = models.CharField(max_length=20)
	sequenceName = models.CharField(max_length=20)

class User(models.Model):
	userID = models.CharField(max_length=20)
	firstName = models.CharField(max_length=20)
	lastName = models.CharField(max_length=20)
	middleName = models.CharField(max_length=20)
	jobTitle = models.CharField(max_length=20)
	email = models.CharField(max_length=50)
	officePhone = models.CharField(max_length=20)
	cellPhone = models.CharField(max_length=20)
	prefix = models.CharField(max_length=20)
	clientID = models.ForeignKey(Client, on_delete=models.CASCADE, default=1)

class Location(models.Model):
	locationID = models.CharField(max_length=20)
	address1 = models.CharField(max_length=20)
	address2 = models.CharField(max_length=20)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=20)
	postalCode = models.CharField(max_length=20)
	country = models.CharField(max_length=20)
	phoneNumber = models.CharField(max_length=20)
	faxNumber = models.CharField(max_length=20)
	client = models.ForeignKey(Client, on_delete=models.CASCADE, default=1)

class Certificate(models.Model):
	certNumber = models.CharField(max_length=20)
	ID = models.CharField(max_length=20)
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	reportNumber = models.CharField(max_length=20)
	issueDate = models.CharField(max_length=20)
	standard = models.ForeignKey(testStandard, on_delete=models.CASCADE, default=1)
	location = models.ForeignKey(Location, on_delete=models.CASCADE, default=1)
	model = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)

class performanceData(models.Model):
	model = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
	sequence = models.ForeignKey(testSequence, on_delete=models.CASCADE, default=1)
	maxVoltage = models.CharField(max_length=20)
	voc = models.CharField(max_length=20)
	isc = models.CharField(max_length=20)
	vmp = models.CharField(max_length=20)
	imp = models.CharField(max_length=20)
	pmp = models.CharField(max_length=20)
	ff = models.CharField(max_length=20)

class Service(models.Model):
	serviceID = models.CharField(max_length=20)
	serviceName = models.CharField(max_length=20)
	description = models.CharField(max_length=20)
	fiRequired = models.CharField(max_length=20)
	fiFrequency = models.CharField(max_length=20)
	standard = models.ForeignKey(testStandard, on_delete=models.CASCADE, default=1)
