import random
from rich.table import Table
from rich.console import Console


class GalvanometerHalfDeflection:

	def __init__(self):

		self.console = Console()
		self.table1 = Table(title = 'For resistance')
		self.table2 = Table(title = 'For figure of merit')

		self.table1.add_column('No of obs')
		self.table1.add_column('R')
		self.table1.add_column('Deflection in G (theta)')
		self.table1.add_column('shunt resistance (S)')
		self.table1.add_column('half deflection (theta/2)')
		self.table1.add_column('G = (RS)/(R + S)')

		self.table2.add_column('No of obs')
		self.table2.add_column('Emf of battery E')
		self.table2.add_column('R')
		self.table2.add_column('Deflection in theta')
		self.table2.add_column('Figue of merit K = E/((R + G)*theta)')

		self.number_of_experiment = 5
		self.R = []
		self.deflectionTheta = []
		self.S = 0
		self.halfDeflection = []
		self.G = []


	def generateResistances(self):
		RInitial = random.randrange(18,45) * 100;
		

		# set Shunt resistance value S depending on initial Resistance
		self.setShuntValue(RInitial)

		for r in range(self.number_of_experiment):
			self.R.append(RInitial)
			RInitial += 100

	def generateThetaAndHalf(self,theta = 30):
		for i in range(self.number_of_experiment):
			self.deflectionTheta.append(theta)
			self.halfDeflection.append(theta//2)
			theta -= 2

	def setShuntValue(self,inititalResistance):
		if inititalResistance >=3500:
			self.S = list(range(36,41))[random.randrange(5)]
		else:
			self.S = list(range(30,36))[random.randrange(5)]

	def calculateG(self):
		for i in range(self.number_of_experiment):
			self.G.append((self.R[i] * self.S)/(self.R[i] - self.S))
	
	def showTabulation(self):
		for i in range(self.number_of_experiment):
			self.table1.add_row(str(i + 1),
				str(self.R[i]),
				str(self.deflectionTheta[i]),
				str(self.S),
				str(self.halfDeflection[i]),
				str(round(self.G[i],2)))
		self.console.print(self.table1)


	def figureOfMerit(self):
		emf = 2
		R = []
		deflection = [26]
		K = []
		meanG = sum(self.G)/self.number_of_experiment

		def generateResistances():
			RInitial = random.randrange(16,20) * 100;
			RInitial = 1200
			for r in range(self.number_of_experiment):
				R.append(RInitial)
				RInitial += 500

		def calculateDeflection():
			
			for i in range(self.number_of_experiment-1):

				deflection.append(emf / ((R[i+1] + meanG) * K[i+1]))

		def addError(merit):
			# Ex - merit = 0.0005 , first_part=5, second part = 1/10000
			# merit separator
			count = 0
			while merit<1:
				count = count + 1
				merit = merit * 10

			# second part

			second_part = 1
			for i in range(count):
				second_part = second_part * 10


			# first part
			first_part =  merit

			# create slightest error
			error =(1 /(10 * second_part)) * random.randrange(1,6)

			return error



		def generateMerit():
			initialMerit = emf / ((R[0] + meanG) * deflection[0])
			K.append(initialMerit)
			for i in range(1,self.number_of_experiment):
				K.append(initialMerit + addError(initialMerit))

		def showTabulation():
			for i in range(self.number_of_experiment):
				k = format(round(K[i],7),'.8f')
				self.table2.add_row(str(i + 1),
					str(emf),
					str(R[i]),
					str(round(deflection[i])),
					str(k))
			self.console.print(self.table2)

		generateResistances()
		generateMerit()
		calculateDeflection()
		showTabulation()


	def run(self):
		self.generateResistances()
		self.generateThetaAndHalf()
		self.calculateG()
		self.showTabulation()


		self.figureOfMerit()
		
