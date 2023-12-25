from rich.console import Console
from rich.table import Table
import random as random
import matplotlib.pyplot as plt

class ResistanceOfWires:
	def __init__(self):
		pass
	def run(self):
		console = Console(record = True)

		table = Table(title = "[bold white on yellow]Resistance of Two wires",show_lines=True)

		table.add_column('No of Readings',style = "bold red",justify = 'center')
		table.add_column('Ammeter reading in A',style = 'cyan',justify = 'center')
		table.add_column('Voltmeter reading in V',style = 'green',justify = 'center')
		table.add_column('Resistance in Ohms',justify = 'center')

		experiment_number = []
		resistanceOne = 4.1
		resistanceTwo = 5.2
		currentValues = [] # have to repeat the values to match number of voltage
		volatageValues = []
		resistanceValues = []
		meanResistance = []
		lengthOfWire = 10

		# diameter table

		table2 = Table(title= '[bold white on yellow]Diameter of wire',show_lines = True)

		table2.add_column('[red]No of readings',style='red')
		table2.add_column('LSR')
		table2.add_column('NCR')
		table2.add_column('CSC')
		table2.add_column('CSR =  CSC x LC')
		table2.add_column('diameter')




		# random increment or decrement value
		def stepValue(value):
			tempValue = random.randrange(0,3)
			if(tempValue == 0):
				return value
			elif(tempValue == 1):
				return -value
			else:
				return 0

		def resistivity(resistance,diameter,length):
			return resistance * (3.14 * (diameter ** 2))/ (4 * length)


		for i in range(1,6):
			currentValues.append(round(i * 0.1,2))
			experiment_number.append(i)

		for i in currentValues:
			step  = stepValue(0.1)
			resistance = (resistanceOne + step)
			resistanceValues.append(round(resistance,2))
			volatageValues.append(round(i * resistance,1))

		for i in currentValues:
			step  = stepValue(0.1)
			resistance = (resistanceTwo + step)
			resistanceValues.append(round(resistance,2))
			volatageValues.append(round(i * resistance,1))

		currentValues = currentValues * 2
		experiment_number = experiment_number * 2


		for i in range(len(currentValues)):
			table.add_row(str(experiment_number[i]),str(currentValues[i]),str(volatageValues[i]),str(resistanceValues[i]))

		console.print(table)
		# mean resistance from table
		lengthOfResistanceValues = len(resistanceValues)
		first_wire_resistances = resistanceValues[0:lengthOfResistanceValues//2]
		second_wire_resistances = resistanceValues[lengthOfResistanceValues//2:lengthOfResistanceValues]

		first_wire_resistance = round(sum(first_wire_resistances)/5,2)
		second_wire_resistance = round(sum(second_wire_resistances)/5,2)

		console.print('Mean Resistance of first wire : ',first_wire_resistance, 'Ohms')
		console.print('Mean Resistance of second wire : ',second_wire_resistance, 'Ohms')

		console.print('R per unit length : ',first_wire_resistance/10, " ohm/cm")
		console.print('R per unit length : ',second_wire_resistance/10, " ohm/cm")
r = ResistanceOfWires()
r.run()