import matplotlib.pyplot as plt
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperatures = [22, 24, 25, 23, 26, 28, 27]
plt.plot(days, temperatures, marker='o')

plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Variations Over a Week')
plt.show()