import csv, math, heapq


def fastest_to_slowest(file, file2):

    g = 9.8

    dict = {}

    with open('data1.csv', 'r') as f1:
        data = csv.DictReader(f1)

        for row in data:
            dict[row["NAME"]] = float(row["LEG_LENGTH"])

    heap = []

    with open('data2.csv', 'r') as f2:
        data = csv.DictReader(f2)

        for row in data:
            if row["STANCE"] == "bipedal":

                name = row["NAME"]

                if name in dict:

                    stride = float(row["STRIDE_LENGTH"])
                    leg = dict[name]

                    speed = ((stride/leg) - 1) * math.sqrt(leg * g)

                    heap.append((speed, name))

    fastest = heapq.nlargest(len(heap), heap, key= lambda x: x[0])

    #heap.sort(reverse= True)

    for _, name in fastest:
        print(name)


fastest_to_slowest('data1.csv', 'data2.csv')
