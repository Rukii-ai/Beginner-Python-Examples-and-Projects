cities = {
    'paris': {
        'country': 'france',
        'population': '2.1 million',
        'fact': 'known as the city of light',
        },

    'new york': {
        'country': 'usa',
        'population': '8.3 million',
        'fact': 'known as the big apple',
        },

    'tokyo': {
        'country': 'japan',
        'population': '13.9 million',
        'fact': 'known as the capital of japan',
        },
        }

for city, details in cities.items():
    print(f"\nFun facts about {city.title()}!:")

    for detiail in details:
        print(f"{detiail.title()}: {details[detiail]}")