import random
from rich.console import Console
from rich.table import Table
import matplotlib.pyplot as mPlot


class ConcaveMirror:


	def __init__(self):
		self.table = Table(title = "for U and V")
		self.table.add_column('No of obs')
		self.table.add_column('x')
		self.table.add_column('y')
		self.table.add_column('z')
		self.table.add_column('u')
		self.table.add_column('v')
		self.table.add_column('1/u')
		self.table.add_column('1/v')
		self.table.add_column('f')

		self.console = Console()

		self.F = 15
		self.f = []
		self.u = [random.randrange(20,30)]
		self.v = []
		self.oneByU = []
		self.oneByV = []
		self.x = 10
		self.y = []
		self.z = []
		self.number_of_exp = 10


	def run(self):
		self.generateF()
		self.generateU()
		self.calculateV()
		self.calculateY()
		self.calculateZ()
		self.calculateOnebyU()
		self.calculateOnebyV()
		self.showTabulation()

		self.console.print("Mean Focal length from table : " , sum(self.f)/self.number_of_exp)
		self.plotUV()



	def generateF(self):
		for i in range(self.number_of_exp):
			self.f.append(self.F + random.randrange(10,20) / 100)

	def generateU(self):
		for i in range(self.number_of_exp - 1):
			self.u.append(self.u[i] + 1)

	def calculateV(self):
		for i in range(self.number_of_exp):
			self.v.append(round((self.f[i] * self.u[i])/(self.u[i] - self.f[i]),1))

	def calculateY(self):
		for i in range(self.number_of_exp):
			self.y.append(self.u[i] + self.x)

	def calculateZ(self):
		for i in range(self.number_of_exp):
			self.z.append(round(self.v[i] + self.x,1))

	def calculateOnebyU(self):
		for i in range(self.number_of_exp):
			self.oneByU.append(round(1/self.u[i],3))

	def calculateOnebyV(self):
		for i in range(self.number_of_exp):
			self.oneByV.append(round(1/self.v[i],3))


	def showTabulation(self):
		for i in range(self.number_of_exp):
			self.table.add_row(str(i + 1),
				str(self.x),
				str(self.y[i]),
				str(self.z[i]),
				str(self.u[i]),
				str(self.v[i]),
				str(self.oneByU[i]),
				str(self.oneByV[i]),
				str(self.f[i]))

		self.console.print(self.table)

	def plotUV(self):
		mPlot.plot(self.u,self.v)
		mPlot.show()

