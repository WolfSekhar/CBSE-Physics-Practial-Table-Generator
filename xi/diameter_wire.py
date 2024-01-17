from rich.console import Console
from rich.table import Table
import random as random
import matplotlib.pyplot as plt


class DiameterOfWire:
    def __init__(self):
        pass

    def run(self):
        console = Console(record=True)

        # diameter table

        table2 = Table(title='[bold white on yellow]Diameter of wire', show_lines=True)

        table2.add_column('[red]No of readings', style='red')
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
        meanDiameter = [0.081]
        experiment_number = []

        # random increment or decrement value
        def stepValue(value):
            tempValue = random.randrange(0, 3)
            if (tempValue == 0):
                return value
            elif (tempValue == 1):
                return -value
            else:
                return 0

        # diameter

        experiment_number.clear()

        for d in meanDiameter:
            for i in range(5):
                experiment_number.append(i + 1)
                tempDiameter = round(d + stepValue(0.001), 3)
                diameter.append(tempDiameter)
                CSR.append(tempDiameter)
                tempCSC = round(tempDiameter / LC)
                CSC.append(tempCSC)
                NCR.append(0)
                LSR.append(0)

        for i in range(5):
            table2.add_row(str(experiment_number[i]), str(LSR[i]), str(NCR[i]), str(CSC[i]), str(CSR[i]),
                           str(diameter[i]))

        print('\n')

        console.print(table2)

        lengthOfDiameters = len(diameter)
        first_wire_diameters = diameter[0:lengthOfDiameters // 2]

        meanDiameterOfFirstWire = round(sum(first_wire_diameters) / (lengthOfDiameters // 2), 3)

        console.print("Mean diameter of first wire : ", meanDiameterOfFirstWire, 'cm')


d = DiameterOfWire()
d.run()
