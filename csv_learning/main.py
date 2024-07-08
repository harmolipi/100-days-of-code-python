# import csv
#
# with open("weather_data.csv") as file:
#     # contents = file.readlines()
#     data = csv.reader(file)
#     print(data)
#
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
# print(data)

# temp_list = data["temp"].to_list()
# total = sum(temp_list)

# average = total / temp_list.__len__()
# print(average)

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# converted_temp = (monday.temp[0] * 1.8) + 32
# print(converted_temp)

# data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv(
    "./2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240708.csv"
)
# print(data)

# grouped_data = data.groupby("Primary Fur Color").count()
# print(grouped_data)

colors = ["Cinnamon", "Gray", "Black"]
color_counts = {"Fur Color": [], "Count": []}

for color in colors:
    color_counts["Fur Color"].append(color)
    color_counts["Count"].append(
        len(data[data["Primary Fur Color"] == color]["Primary Fur Color"])
    )
#
# print(color_counts)
color_data = pandas.DataFrame(color_counts)
print(color_data)
# color_data.to_csv("color_data.csv")

# reds = (
#     data[data["Primary Fur Color"] == "Cinnamon"]["Primary Fur Color"]
#     .to_list()
#     .__len__()
# )
# print(reds["Primary Fur Color"].to_list().__len__())
# print(reds.count())
