from rich.console import Console
from rich.table import Table
import random as random


class ResistivityOfWires:
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


		# diameter table

		table2 = Table(title= '[bold white on yellow]Diameter of wire',show_lines = True)

		table2.add_column('[red]No of readings',style='red')
		table2.add_column('LSR')
		table2.add_column('NCR')
		table2.add_column('CSC')
		table2.add_column('CSR =  CSC x LC')
		table2.add_column('diameter')

		pitch = 0.1
		LC = 0.001
		LSR = []
		NCR = []
		CSC = []
		CSR = []
		diameter = []
		meanDiameter = [0.081,0.089]




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
			#step  = stepValue(0.1)
			step = stepValue(0.1) # use step = stepValue(0.1) to get authentic error
			resistance = (resistanceOne + step)
			resistanceValues.append(round(resistance,2))
			volatageValues.append(round(i * resistance,table2))

		for i in currentValues:
			#step  = stepValue(0.1)
			step  = stepValue(0.1) # use step = stepValue(0.1) to get authentic error
			resistance = (resistanceTwo + step)
			resistanceValues.append(round(resistance,2))
			volatageValues.append(round(i * resistance,2))

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


		# diameter

		experiment_number.clear()

		for d in meanDiameter:
			for i in range(3):
				experiment_number.append(i + 1)
				tempDiameter = round(d + stepValue(0.001),3)
				diameter.append(tempDiameter)
				CSR.append(tempDiameter)
				tempCSC = round(tempDiameter / LC)
				CSC.append(tempCSC)
				NCR.append(0)
				LSR.append(0)


		for i in range(6):
			table2.add_row(str(experiment_number[i]),str(LSR[i]),str(NCR[i]),str(CSC[i]),str(CSR[i]),str(diameter[i]))

		print('\n')

		console.print(table2)

		lengthOfDiameters = len(diameter)
		first_wire_diameters = diameter[0:lengthOfDiameters//2]
		second_wire_diameters = diameter[lengthOfDiameters//2:lengthOfDiameters]

		meanDiameterOfFirstWire = round(sum(first_wire_diameters)/(lengthOfDiameters//2),3)
		meanDiameterOfSecondWire = round(sum(second_wire_diameters)/(lengthOfDiameters//2),3)

		console.print("Mean diameter of first wire : ", meanDiameterOfFirstWire, 'cm')
		console.print('Mean diameter of second wire : ', meanDiameterOfSecondWire, 'cm')


		lengthOfFirstWire = 50;
		lengthOfSecondWire = 50;

		console.print('Resistivity of first wire : ', str(resistivity(first_wire_resistance,meanDiameterOfFirstWire,lengthOfFirstWire)))
		console.print('Resistivity of second wire : ', str(resistivity(second_wire_resistance,meanDiameterOfSecondWire,lengthOfSecondWire)))
