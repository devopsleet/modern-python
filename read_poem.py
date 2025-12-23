import csv, math
import heapq
def bipolar_dino(file1, file2):

    g = 9.8

    dict = {}
    with open('data1.csv','r') as file1:
        reader = csv.DictReader(file1)

        for row in reader:
            dict[row["NAME"]] = float(row["LEG_LENGTH"])

    heap = []
    with open('data2.csv', 'r') as file2:
        reader = csv.DictReader(file2)

        for row in reader:
            name = row["NAME"].strip()
            stance = row["STANCE"].strip().lower()

            if name in dict and stance == "bipedal":
                stride_length = float(row["STRIDE_LENGTH"])

                leg_length = dict[name]
                try:
                    speed = ((stride_length / leg_length) -1 ) * math.sqrt(leg_length * g)

                    heap.append((speed, name))
                except ZeroDivisionError:
                    continue


    heap.sort(key= lambda x : x[0], reverse= True)

    for _, name in heap:
        print(name)

    #     print(heap)
    #
    # while heap:
    #     _, name = heapq.heappop(heap)
    #     print(name)


bipolar_dino('data1.csv', 'data2.csv')
