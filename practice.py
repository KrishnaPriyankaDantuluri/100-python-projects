from asyncio import start_unix_server
from os.path import split

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# split_words = sentence.split()
# import  random
#
# split_count = {student:len(student) for student in split_words  }
#
# result = [split_count]
# print(result)
#
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()}
print(weather_f)



