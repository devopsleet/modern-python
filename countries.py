input_file = 'country_info.txt'

countries = {}

with open(input_file) as country_file:
    # print(repr(country_file.readline()))
    country_file.readline()

    for row in country_file:
        data = row.rstrip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data

        country_dict = {
            'name' : country,
            'capital' : capital,
            'country_code' : code,
            'cc3' : code3,
            'dialing_code' : dialing,
            'timezone' : timezone,
            'currency' : currency

        }

        # print(country_dict)
        countries[country.casefold()] = country_dict
#
# print(countries)
get_name = input("Please Enter the country name = ")

if get_name in countries:
    #print(get_name.casefold())
    data = countries[get_name]
    print(data['capital'])
# print(countries)

# countries = ["a", "b", "c", "d"]
#
# it = iter(countries)
#
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         break
