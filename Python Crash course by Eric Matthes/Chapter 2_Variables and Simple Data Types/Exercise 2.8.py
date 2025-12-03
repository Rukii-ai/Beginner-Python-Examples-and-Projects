url = "https://www.github.com"
clean_url = url.removeprefix("https://")

filename = "python_notes.txt"
clean_filename = filename.removesuffix(".txt")

print(f"The url is {clean_url} and the file stored there is {clean_filename}")