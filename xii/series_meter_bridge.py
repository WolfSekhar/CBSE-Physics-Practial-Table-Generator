import random
from rich.table import Table
from rich.console import Console


class Series:

    def __init__(self):
        self.number_of_experiment = 6  # (multiple of 3)

        self.mean_resistance_of_wires = []
        self.series_combination_value = 0  # from r1 and r2
        self.series_value = 0  # experiment table while in series connection
        self.wire = 1
        self.console = Console()
        self.table = Table(title = "[bright_white on deep_sky_blue3]Unknown resistance of first wire")
        self.table2 = Table(title = '[bright_white on deep_sky_blue3]Unknown resistance of second wire')
        self.table3 = Table(title = '[bright_white on deep_sky_blue3]Unknown resistance of Series Combination')
        self.tables = [self.table,self.table2,self.table3]

        for t in self.tables:
            t.add_column('no of observations',style='red')
            t.add_column('R',style='green')
            t.add_column('l',style='yellow')
            t.add_column('100 - l',style = 'turquoise2')
            t.add_column('X',style='light_slate_blue')




    def run(self):
        self.console.print("[#00af87]To verify the law of combination (series) of resistance using a meter bridge)")
        self.console.print("---------------------------------------------------")

        def title():
            print("No.of Observation", end=" |")
            print("R (in ohm)", end=" |")
            print("l (in cm.)", end=" |")
            print("(100 -l) (in cm)", end=" |")
            print("X = R (l/(100 -l)) in ohms", end=" |")
            print("Mean X (in ohms)")

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
                upper_value = random.randint(45, 55)
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
            #print('-----------------------------------')
            for i in values:
                sum = sum + i[4]
            mean = round(sum / len(values), 2)
            self.console.print("mean : ","[#87d700]" +  str(mean)  + ' Ohm')
            self.mean_resistance_of_wires.append(mean)
            print('')

        for count in range(2):
            self.console.print("for wire : ","[#87d700]" + str(self.wire),style='u')
            self.console.print("")

            self.wire += 1

            # calculation of values

            observations()
            r()
            l()
            hundred_minus_l()
            x()

            # title()
            for v in values:
                self.tables[count].add_row(str(v[0]),str(v[1]),str(v[2]),str(v[3]),str(v[4]))
            self.console.print(self.tables[count])
            mean_x()  # printing mean value of each wire

        # table 3

        # -----------------------------------------------------------------#
        x_values_from_mean_x = []

        def meanX(mean):
            for i in range(6):
                step_value = (random.randrange(0, 3) * 0.1)
                step_value_choice_list = [-step_value, step_value]
                tempMean = mean + random.choice(step_value_choice_list)
                x_values_from_mean_x.append(round(tempMean, 2))

        def calculate_combination_series_from_r1_r2():
            r1 = self.mean_resistance_of_wires[0]
            r2 = self.mean_resistance_of_wires[1]
            return r1 + r2

        series_combination_value = calculate_combination_series_from_r1_r2()

        

        series_value = round(series_combination_value + 0.01, 2)

        # del values

        def observations():
            global rev_values
            rev_values = []
            for obs in range(1, 7):
                rev_values.append([obs])

        def reverseMean():
            meanX(series_combination_value)
            

        def reversel():
            X = x_values_from_mean_x
            counter = 0
            for i in range(2):
                for j in range(3):
                    R = j + 1
                    l = 100 / ((R / X[j]) + 1)
                    rev_values[counter].append(R)
                    rev_values[counter].append(round(l))
                    counter += 1

        def reverse_hundred_minus_l():
            for i in range(len(rev_values)):
                rev_values[i].append(100 - rev_values[i][2])

        def insert_meanx_values():
            for i in range(len(rev_values)):
                X = x_values_from_mean_x
                rev_values[i].append(X[i])

        observations()
        reverseMean()
        reversel()
        reverse_hundred_minus_l()
        insert_meanx_values()

        #print("****************3****************** ")

        for v in rev_values:
            self.table3.add_row(str(v[0]),str(v[1]),str(v[2]),str(v[3]),str(v[4]))
        self.console.print(self.table3)
        print("************* combined wires value ************")
        self.console.print("Mean X: ","[#87d700]" + str(series_value) + " ohms")

        print("****************************************")
        self.console.print("series comb value : ", "[#87d700]" + str(round(series_combination_value, 2)) + ' ohms')


#series = Series()
#series.run()
