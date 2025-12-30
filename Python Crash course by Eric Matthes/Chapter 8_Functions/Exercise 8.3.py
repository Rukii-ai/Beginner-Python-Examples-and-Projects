def make_shirt(size, text):
    """Display the size and text of a shirt."""
    print(f"\nThis is a {size.upper()} shirt with the text"
          f" '{text.title()}' written on it.")
    
make_shirt('xxl', 'hello world!')
make_shirt(size='m', text='python is fun!')
make_shirt(text='stay positive!!!', size='s')
