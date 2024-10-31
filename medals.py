import csv
import math

g = 9.8


def calculate_speed(leg_length, stride_length):
    return ((stride_length/leg_length) - 1) * math.sqrt(leg_length * g)


dinosaurs = {}

with open('data1.csv', 'r') as file1:
    reader = csv.DictReader(file1)
    for row in reader:
        print(row)
        dinosaurs[row['NAME']] = {
            'leg_length': float(row['LEG_LENGTH']),
            #'diet': row['DIET']
        }

print(dinosaurs)

bipedal_dinosaurs = []

with open('data2.csv', 'r') as file2:
    reader = csv.DictReader(file2)

    for row in reader:
        name = row['NAME']
        if name in dinosaurs and row['STANCE'] == 'bipedal':
            dinosaurs[name]['stride_length'] = float(row['STRIDE_LENGTH'])
            leg_length = dinosaurs[name]['leg_length']
            stride_length = dinosaurs[name]['stride_length']
            # stride_length = row.get('stride_length')
            print(stride_length)
            if stride_length:
                print(dinosaurs[name])
                speed = calculate_speed(leg_length, stride_length)
                bipedal_dinosaurs.append((name, speed))

bipedal_dinosaurs.sort(key=lambda x: x[1], reverse=True)
print(bipedal_dinosaurs)
for dino in bipedal_dinosaurs:
    print(dino[0])
