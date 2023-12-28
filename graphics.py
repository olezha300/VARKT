import csv
import matplotlib.pyplot as plt

# Чтение данных из файла
time = []
velocity = []
altitude = []

with open("/Users/apple/Downloads/Безымянный аппарат_12280258.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Пропуск заголовка
    for row in reader:
        time.append(float(row[0]))
        velocity.append(float(row[1]))
        altitude.append(float(row[3]))

# График зависимости высоты от времени полета
plt.figure(1)
plt.plot(time, altitude)
plt.xlabel("Время полета")
plt.ylabel("Высота")
plt.title("Зависимость высоты ракеты от времени полета")
plt.grid(True)

# График зависимости скорости от времени полета
plt.figure(2)
plt.plot(time, velocity)
plt.xlabel("Время полета")
plt.ylabel("Скорость")
plt.title("Зависимость скорости ракеты от времени полета")
plt.grid(True)

# Вывод графиков на экран
plt.show()
