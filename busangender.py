import csv

gfile = open('busanpeople.csv')
gender = csv.reader(gfile)
a = []
b = []
for g in gender:
  for i in g[2:3]:
    a.append(-int(i.replace(',','')))
  for i in g[3:4]:
    b.append(int(i.replace(',','')))

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rc('font', family = 'NanumGothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title('부산의 남녀 성별 인구 분포')
plt.barh(range(len(b)),b, label='여성')
plt.barh(range(len(a)),a, label='남성')

plt.legend()
plt.show()

print(plt)