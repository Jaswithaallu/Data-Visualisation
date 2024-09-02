'''
This is to show the marks of Mira's using a BAR CHART..
'''
import matplotlib.pyplot as plt
No_of_marks_obtained = [35,32,39,37,28,40,32,]
plt.bar(['Hindi','English','Math','Science','AI','Sanskrit','Arts'],No_of_marks_obtained)
plt.title('Bar Chart Of Mira's Marks')
plt.xlabel('Subjects')
plt.ylabel('No. of marks obtained')
plt.show()
