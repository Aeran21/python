import csv
f = open('busanpeople.csv')
data = csv.reader(f)

num = []
for row in data:
  for i in row[4:]:
    num.append(int(i))

import matplotlib.pyplot as plt
plt.bar(range(len(num)),num, label='세대 수')
plt.legend()
plt.show()