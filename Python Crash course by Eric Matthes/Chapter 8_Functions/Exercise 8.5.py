def describe_city(city, country="Nigeria"):
    """Display a city and its country."""
    print(f"{city.title()} is located in {country.title()}.")


describe_city("lagos")
describe_city(city="abuja")
describe_city("paris", "france")