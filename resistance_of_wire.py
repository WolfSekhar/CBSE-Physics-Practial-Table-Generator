import random


class ResistanceOfWire:

    def __init__(self):
        self.number_of_experiment = 6  # (multiple of 3)

        self.mean_resistance_of_wires = []
        self.parallel_combination_value = 0  # from r1 and r2
        self.parallel_value = 0  # experiment table while in parallel connection
        self.wire = 1

    def run(self):
        print("Find unknown resistance using a meter bridge)")
        print("---------------------------------------------------")

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
                print(value)  # printing all the values one by one
            mean_x()  # printing mean value of each wire


resistance = ResistanceOfWire()
resistance.run()