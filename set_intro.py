farm_animals = {'cow', 'hen', 'goat', 'sheep', 'horse'}
print(farm_animals)


for animal in farm_animals:
    print(animal)


more_animals = {'sheep', 'goat', 'cow', 'horse', 'hen'}


if more_animals == farm_animals:
    print('The sets are equal')
else:
    print('The sets ar different')


print(set(range(0,20,2)))
