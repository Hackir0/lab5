import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('C:/BSUIR/testSyap.csv', nrows=1000)

missing_data = data.isna().any()
if missing_data.sum() == 0:
    print("Пропусков нет")
else:
    print("Количесвто пропусков в каждом столбце")
    print(missing_data[missing_data == True])

numeric_columns = data.select_dtypes(include=[int, float]).columns
for column in numeric_columns:
    if data[column].isna().any():
        data[column].fillna(data[column].mean(), inplace=True)

# Заменяем отсутствующие значения в строковых столбцах на пустые строки
string_columns = data.select_dtypes(include=object).columns
for column in string_columns:
    if data[column].isna().any():
        data[column].fillna('', inplace=True)

room_counts = {}
for index, row in data.iterrows():
    room_count = row['Rooms']
    if room_count in room_counts:
        room_counts[room_count] += 1
    else:
        room_counts[room_count] = 1

for room_count, count in room_counts.items():
    print(f"{room_count}-комнатная квартира:{count}")

fig, ax = plt.subplots()
ax.set_yscale('log')
ax.boxplot(data["Square"], vert=False)
ax.set_title('Ящик с усами(логарифмическая шкала)')

fig, ax = plt.subplots()
ax.hist(data["Square"], bins=50)
ax.set_title("Гистограмма")
plt.show()

pivot = data.pivot_table(index='DistrictId', columns='Rooms', values='Id', aggfunc='count', fill_value=0)
print(pivot)

data.to_csv("result_data.csv", index=False)
