#Задача №2
#Научите Анфису сообщать пользователю, сколько времени шёл его любимый сериал.

#Дата выхода первой серии - 17 апреля 2011 года.

#Дата выхода последней серии - 15 апреля 2019 года.


import datetime as dt

# Дата выхода первой серии.
start_time = dt.datetime(2011, 4, 17)
# Дата выхода последней серии.
final_time = dt.datetime(2019, 4, 15)

# Вычислите, сколько времени шёл сериал.
duration = final_time - start_time

print(duration)