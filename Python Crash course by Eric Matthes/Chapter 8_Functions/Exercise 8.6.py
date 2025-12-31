def city_country(city, country):
    """Return a formatted string of the city and country."""
    return f"{city.title()}, {country.title()}"


print(city_country("lagos", "nigeria"))
print(city_country("paris", "france"))
print(city_country("tokyo", "japan"))