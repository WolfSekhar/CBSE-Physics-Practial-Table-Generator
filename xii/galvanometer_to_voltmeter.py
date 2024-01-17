import random
from rich.table import Table
from rich.console import Console

class GalvanometerToVoltmeter:
	

	def __init__(self):
		self.console = Console()
		self.table = Table(title = '[white on green]Verification')


		self.table.add_column('No of obs',style = "#ff87ff")
		self.table.add_column("Deflection in degree",style = "#ff8787")
		self.table.add_column("P.D V1 (Theta * LC)",style = "#d7d75f")
		self.table.add_column("V2",style = "#d75faf")
		self.table.add_column("V1 - v2",style = "#afd75f")
		self.number_of_experiment = 5


	def run(self):
		resistanceOriginal = 200
		resistanceOriginalModified = 200 + (random.randrange(-2,2))
		rangeOfConversionV = 1
		n = 100
		k = random.randrange(40,50)/ 1000000
		ig = n * k
		G = (rangeOfConversionV / ig) - resistanceOriginalModified

		standardVolt = random.randrange(15,26)/10

		v2 = [standardVolt] * self.number_of_experiment
		v1 = [standardVolt]
		deflection = []
		LC = 0.1
		vDifference = []

		def generateV1():
			step = random.randrange(1,4)/10
			for i in range(0,self.number_of_experiment-1):
				v1.append(v1[i] - step)

		def calculateDeflection():
			for i in range(self.number_of_experiment):
				deflection.append(round(v1[i]/LC))

		def calculateVDiff():
			for i in range(self.number_of_experiment):
				vDifference.append(v2[i] - v1[i])


		def showTabulation():
			for i in range(self.number_of_experiment):
				self.table.add_row(str(i + 1),
					str(deflection[i]),
					str(round(v1[i],2)),
					str(v2[i]),
					str(round(vDifference[i],2)))
			self.console.print(self.table)

		def check():
			mul = 1
			if G < 1:
				mul = -1

			newR = (rangeOfConversionV / ig) - (G * mul)
			self.console.print("Resistance Of Galvanometer", round(G,2) * mul," Ohm")
			self.console.print("Figure of merit: : ",k, " Div/A")
			self.console.print("No of Div in Galvanometer : ", n )
			self.console.print("Current of Galvanometer : ", round(ig,5) , " A")
			self.console.print("V : Range of Conversion : ", rangeOfConversionV, " V")
			self.console.print("R : ",newR, " Ohm")

		generateV1()
		calculateDeflection()
		calculateVDiff()
		showTabulation()
		check()