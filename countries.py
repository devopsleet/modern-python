filename = 'D:/Python/country_info.txt'

countries = {}
with open(filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep="\n\t")
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency
        }
        print(country_dict)
        countries[country.casefold()] = country_dict


print(countries)

while True:
    chosen_country = input("Please select the country name ").casefold()
    if chosen_country in countries:
        country_data = countries[chosen_country]
        print(f"The capital city is {country_data['capital']}")
    elif chosen_country == 'quit':
        break

# while True:
#     country_name_entered_by_user = input("Enter the country name = ")
#     for country, data in countries.items():
#         if country_name_entered_by_user in countries:
#             print(f"The capital city of {country_name_entered_by_user} is {countries['country['capital']']}")
#         else:
#             break
