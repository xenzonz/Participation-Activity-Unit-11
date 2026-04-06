print("helloworld")

def city_country(city, country, population=None):

    formatted_city = city.strip().title()
    formatted_country = country.strip().title()

    if population is not None:
        return f"{formatted_city}, {formatted_country} - population {population}"

    return f"{formatted_city}, {formatted_country}"