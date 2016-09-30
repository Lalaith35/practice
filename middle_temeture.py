#Необходимо открыть файл на чтение и прочитать его. Каждую
#прочитанную строку надо разбить по разделителю «;» и извлечь поля «Дата и
#время наблюдения» и «Температура».
#Затем нужно найти среднее значение температуры, а так же её
#минимальное и максимальное значения 

import os

file = open("weather.csv","r")

#так как в таблице храняться несколько значений температуры 
#за один день, вычислим среднее значение за день
#в начале в словарь, где будут храниться результаты, сложим первое 
#значение вида {первая дата:0}

string = file.readline()
data_about_weatger = string.split(";")
date_and_time = data_about_weatger[0].split(" ")
date = str(date_and_time[0][1:])
summer = {date:0}

#для того чтобы вычислить среднее значение за день, ищем дату из текущей строки,
#в словаре. Если такая дата есть, складываем температуру, соответствующую этой дате,
#с температурой из текущей строки. Если такой даты нет, делим температуру из предыдущей
#даты на количество суммирований+1 и создаём новую запись

count_sum = 1

for string in file:

	data_about_weatger = string.split(";")
	date_and_time = data_about_weatger[0].split(" ")
	date = str(date_and_time[0][1:])
	temperature = float(data_about_weatger[1][1:-1])

	if date in summer:

		summer[date] +=  temperature
		count_sum += 1
		current_date = date

	else:

		summer[current_date] = round(summer[current_date]/count_sum, 1)
		summer[date] =  temperature 
		count_sum = 0

summer[current_date] = summer[current_date]/count_sum #средняя температура для последней даты

#вычислим среднюю температуру за лето

sum_tempeture = 0

for tempeture in summer.values():
	sum_tempeture += tempeture

mid_tempeture = round(sum_tempeture/len(summer.values()),1)	

#найдём самы жаркий и самый холодный день лета

min_temperature = 100
max_temperature = 0

for date_tempeture in summer:

		if summer[date_tempeture] > max_temperature:

			max_temperature = summer[date_tempeture]
			day_with_max_temperature = date_tempeture

		if	summer[date_tempeture] < min_temperature: 

			min_temperature = summer[date_tempeture]
			day_with_min_temperature = date_tempeture



#print ("middle temperature",mid_tempeture, "\n max tepmerature", day_with_max_temperature, max_temperature, "\n min temperature", day_with_min_temperature, min_temperature)


print ("Средняя температура за лето составила {}\n\n{} средняя температура за день составила {} градусов цельсия. \nЭто маскимальное значение температуры за лето. \n\n{} средняя температура за день составила {} градусов цельсия. \nЭто минимальное значение температуры за лето.".format(mid_tempeture, day_with_max_temperature, max_temperature, day_with_min_temperature, min_temperature)) 

os.system("PAUSE")