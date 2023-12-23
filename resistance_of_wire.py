import random
from rich.table import Table
from rich.console import Console

class ResistanceOfWire:

    def __init__(self):
        self.number_of_experiment = 6  # (multiple of 3)

        self.mean_resistance_of_wires = []
        self.parallel_combination_value = 0  # from r1 and r2
        self.parallel_value = 0  # experiment table while in parallel connection
        self.wire = 1
        self.console = Console()
        self.table = Table(title = 'Resistance of Wire')


        self.table.add_column('SL no')
        self.table.add_column('Resistance')
        self.table.add_column('l in cm')
        self.table.add_column('100 - l')
        self.table.add_column('unknown resistance')

    def run(self):
        print("Find unknown resistance using a meter bridge)")
        print("---------------------------------------------------")


        # Table 1 and 2

        def observations():
            global values
            values = []
            for obs in range(1, self.number_of_experiment + 1):
                values.append([obs])

        def r():
            counter = 0
            for i in range(2):
                for j in range(1, 4):
                    values[counter].append(j)
                    counter = counter + 1

        def l():
            counter = 0
            for i in range(2):
                upper_value = random.randint(45, 60)
                upper_reducer = random.randint(10, 15)
                for j in range(3):
                    values[counter].append(upper_value)
                    upper_value = upper_value - upper_reducer
                    upper_reducer = random.randint(2, 9)

                    counter = counter + 1

        def hundred_minus_l():
            for i in range(len(values)):
                values[i].append(100 - values[i][2])

        def x():
            for i in range(len(values)):
                r_value = values[i][1]
                l_value = values[i][2]
                hundred_minus_l_value = values[i][3]
                x_value = ((r_value * l_value) / hundred_minus_l_value)
                values[i].append(round(x_value, 2))

        def mean_x():
            sum = 0
            mean = 0
            print('-----------------------------------')
            for i in values:
                sum = sum + i[4]
            mean = round(sum / len(values), 2)
            print("Mean Resistance : ", mean)
            self.mean_resistance_of_wires.append(mean)
            print('-----------------------------------')

        for count in range(1):
            # calculation of values

            observations()
            r()
            l()
            hundred_minus_l()
            x()

            # title()
            for value in values:
                self.table.add_row(str(value[0]),str(value[1]),str(value[2]),str(value[3]),str(value[4]))
            self.console.print(self.table)
            mean_x()  # printing mean value of each wire

#resistance = ResistanceOfWire()
#resistance.run()