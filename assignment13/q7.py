#7) Plot graph comparing two semester results

import matplotlib.pyplot as plt

subjects = ["Maths","Python","DSA","DBMS","OS"]

sem3 = [75,80,78,82,74]
sem4 = [85,88,84,90,86]

plt.figure(figsize=(8,5))

plt.plot(subjects, sem3,
         marker='o',
         linestyle='--',
         linewidth=2,
         label='Semester 3')

plt.plot(subjects, sem4,
         marker='s',
         linestyle='-',
         linewidth=2,
         label='Semester 4')

plt.title("Semester Result Comparison")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.grid(True)
plt.legend()

plt.show()