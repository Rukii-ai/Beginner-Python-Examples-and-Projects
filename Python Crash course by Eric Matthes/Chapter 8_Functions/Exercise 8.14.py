def make_car(manufacturer_name, model_name, **car_details):
    """Provide relevant information about a car"""
    
    car_details["Manufacturer"] = manufacturer_name
    car_details["Model"] = model_name

    return car_details


new_car = make_car("Ford", "Model-T", Color="Black",
         Date_of_Purchase="12th of December, 1892")

print(new_car)

