def make_shirt(size="L", text="I love Python"):
    """Display the size and text of a shirt."""
    print(f"\nThis is a {size.upper()} shirt with the text"
          f" '{text.title()}' written on it.")
    

make_shirt("m")
make_shirt()
make_shirt(size="s", text="stay positive!!!")