import csv

def save_result(location, station, pm10, advice):
    with open('dust_result.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([location, station, pm10, advice])
