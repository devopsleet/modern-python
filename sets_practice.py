farm_animals = {"sheep"}
wild_animals = ["lion"]

# print(wild_animals)
all_animals_1 = farm_animals.union(wild_animals)
print(all_animals_1)

all_animals_2 = farm_animals | wild_animals
print(all_animals_2)

# from prescription_data import adverse_interactions
#
# meds_to_watch = set()
#
# for interactions in adverse_interactions:
#     print(interactions)
#     #meds_to_watch = meds_to_watch.union(interactions)
#
# print(sorted(meds_to_watch))
