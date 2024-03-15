# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# # average = sum(temp_list) / len(temp_list)
# # print(round(average, 2))
# print(data["temp"].mean())
#
#
# print(data["temp"].max())

# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# # print(monday.condition)
# fahrenheit_monday = monday.temp[0] * 9/5 + 32
# print(fahrenheit_monday)

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors = data["Primary Fur Color"].to_list()
Gray = colors.count("Gray")
Red = colors.count("Cinnamon")
Black = colors.count("Black")
squirrel_count_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [Gray, Red, Black]
}
df = pandas.DataFrame(squirrel_count_dict)
df.to_csv("squirrel_count.csv")

