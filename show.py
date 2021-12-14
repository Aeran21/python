import matplotlib.pyplot as plt
plt.rc('font', family='NanumBarunGothic')
import csv
from bs4 import BeautifulSoup

svgfile = open('/content/Busan.svg','r').read()
csvfile = csv.reader(open('/content/busanpeople.csv'), delimiter=',')

num={}
li = []

for i in csvfile:
  j = i[0]
  count = int(i[1])
  num[j]=count
  li.append(num)

sorted(num.items(),key = lambda item: item[1], reverse=True)

soup = BeautifulSoup(svgfile)
paths = soup.findAll('path')

colors = ["#FCE4EC","#F8BBD0","#F48FB1","#F06292", "#EC407A", "#E91E63", "#D81B60","#C2185B","#AD1457"]
path_style = 'fill:'

for p in paths:
    if p['id']:
        count = num[p['id']]
        if count >=  400000:
            color_class = 8
            plt.plot(count, label='asdf')
        elif count >= 350000:
            color_class = 7
        elif count >= 300000:
            color_class = 6
        elif count >= 250000:
            color_class = 5
        elif count >= 200000:
            color_class = 4
        elif count >= 150000:
            color_class = 3
        elif count >= 100000:
            color_class = 2
        elif count >= 50000:
            color_class = 1
        else :
            color_class = 0
        color = colors[color_class]
        p['style'] = path_style + color
        
import sys
sys.stdout = open('busanpeopleNum.html','w')
print(soup.prettify())