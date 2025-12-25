favorite_languages = { 
      'jen': ['python', 'rust'], 
      'sarah': ['c'], 
      'edward': ['rust', 'go'], 
      'phil': ['python', 'haskell'], 
      } 

for name, languages in favorite_languages.items(): 
    print(f"\n{name.title()}'s favorite languages are:") 
    
    for language in languages: 
        print(f"\t{language.title()}")


"""
You should not nest lists and dictionaries too deeply. If
you’re nesting items much deeper than what you see
in the preceding examples, or if you’re working with
someone else’s code with significant levels of nesting,
there’s most likely a simpler way to solve the
problem.
"""