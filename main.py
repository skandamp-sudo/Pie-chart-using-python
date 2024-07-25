from matplotlib import pyplot as plt
import numpy as np

langs = ['cricket', 'kabbadi', 'football', 'chess', 'tennis']
students = [50, 40, 60, 20, 20]

plt.pie(students, labels=langs, autopct='%1.2f%%')
plt.show()
