import csv


with open('weather_data.csv') as csvfile:
    temps = []
    rows = csv.DictReader(csvfile)
    for row in rows:
        temps.append(int(row['temp']))

print(temps)




