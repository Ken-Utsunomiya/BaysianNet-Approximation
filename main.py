
import sys
import math
import csv
import matplotlib.pyplot as plt

if __name__ == '__main__':
    question = sys.argv[1]

    if question == '2':
        # Question 2.a
        file = open('rs_1.csv')
        csv_reader = csv.reader(file)

        rows = []
        for row in csv_reader:
            rows.append(row[0])

        result = []
        rain = no_rain = 0.0
        temp = 0

        for i in range(1, len(rows)):
            if rows[i] == '1':
                rain += 1.0
                temp = (rain / (rain + no_rain))
            elif rows[i] == '2':
                no_rain += 1.0
                temp = (rain / (rain + no_rain))
            result.append(temp)

        print('P(r | s,w) = {0}'.format(result[-1]))
        print('rain: {0}'.format(rain))
        print('no rain: {0}'.format(no_rain))
        print('total: {0}'.format(rain+no_rain))
        plt.plot(result)
        plt.xlabel('Number of Samples')
        plt.ylabel('P(r | s,w)')
        plt.xscale('log')
        plt.ylim([-0.2, 0.70])
        plt.savefig('a.png')

        # Question 2.b
        result_plus_epsilon = []
        result_minus_epsilon = []
        rain = no_rain = 0.0
        temp1 = temp2 = 0.0
        n = 0.0

        for i in range(1, len(rows)):
            if rows[i] == '1':
                rain += 1.0
                n += 1.0
                epsilon = math.sqrt(-(math.log(0.05/2))/(2*n))
                temp1 = (rain / (rain + no_rain)) + epsilon
                temp2 = (rain / (rain + no_rain)) - epsilon
            elif rows[i] == '2':
                no_rain += 1.0
                n += 1.0
                epsilon = math.sqrt(-(math.log(0.05 / 2)) / (2 * n))
                temp1 = (rain / (rain + no_rain)) + epsilon
                temp2 = (rain / (rain + no_rain)) - epsilon
            result_plus_epsilon.append(temp1)
            result_minus_epsilon.append(temp2)

        plt.plot(result_plus_epsilon)
        plt.plot(result_minus_epsilon)
        print(len(result_plus_epsilon))
        print(len(result_minus_epsilon))
        plt.savefig('b.png')

    else:
        print('Invalid question number')
