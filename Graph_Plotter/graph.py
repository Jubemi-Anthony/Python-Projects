import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [13,27,50,83, 60]

tick_label = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
plt.bar(x, y, tick_label=tick_label, width=0.8, color=['brown', 'red'])

# a = [2,4,5,6,7,9,14]
# b = [3,4,6,7,8,9,29]

# plt.plot(x,y, color='green', linestyle='dashed', linewidth=3, marker='o', markerfacecolor='blue', markersize=12)
# plt.ylim(0,40)
# plt.xlim(0,40)
# plt.plot(a,b, label= 'Line 2')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title("Ant's Python Graph")
# plt.legend()

plt.show()