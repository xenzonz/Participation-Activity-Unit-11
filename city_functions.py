#print("helloworld")

def city_country(city, country, population=None):

    formatted_city = city.strip().title()
    formatted_country = country.strip().title()

    if population is not None:
        return f"{formatted_city}, {formatted_country} - population {population}"

    return f"{formatted_city}, {formatted_country}"

#def main():
    #print(city_country('santiago', 'chile', population=1919111))
    #print(city_country('tokyo', 'japan', population=13_960_000))

#main()
