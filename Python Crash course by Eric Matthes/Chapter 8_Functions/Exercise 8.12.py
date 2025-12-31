def make_sandwich(size, *contents):
    """Create a sandwhich of the specified size with specified contents"""
   
    print(f"\nOrder Ready! For {size.title()} sandwhich"
          " with the following contents:")
    
    for content in contents:
        print(f"- {content.title()}")


make_sandwich("Large", "beef")
make_sandwich("small", "extra cheese", "tomato", "chicken")
make_sandwich("extra large", "ketchup", "mustard",
              "pork", "lettuce", "eggs", "sausages")
    
