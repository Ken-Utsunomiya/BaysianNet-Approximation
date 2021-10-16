
import sys
import csv
import matplotlib.pyplot as plt

if __name__ == '__main__':
    question = sys.argv[1]

    if question == 'a':
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
        plt.plot(result)
        plt.xlabel('Number of Samples')
        plt.ylabel('P(r | s,w)')
        plt.xscale('log')
        plt.savefig('rain.png')

    else:
        print('Invalid question number')
