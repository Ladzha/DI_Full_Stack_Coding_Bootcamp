def colorize(text, color):
    colors = ('cyan', 'yellow', 'blue', 'green', 'magenta')
    print(text)
    
    try: 
        if color not in colors:
            raise ValueError('No color in tuple') 
        if type(text) !=str:
            print(color) 
            raise TypeError ('Not string type')
    except Exception as error:
        print(error)
      
colorize("hello", "cyan")
colorize(123, "red")
colorize("hello", "red")