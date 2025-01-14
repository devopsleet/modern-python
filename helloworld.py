election_parties = ["bjp", "congress", "dmk", "x"]

constituency = [240, 100, 40]

# bjp 240
# congress 100
# dmk 40

for party in election_parties:
    print(party)

for value in constituency:
    print(value)


for party, value in zip(election_parties, constituency):
    print(party, value)


tuple1 = ('p', 'q')
set1 = {100, 200}

result = zip(tuple1, set1)
print(list(result))
