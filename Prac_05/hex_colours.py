hex_colours = {'aqua': '#00ffff', 'beaver': '#9f8170', 'black': '#000000', 'blond': '#faf0be', 'coral': '#ff7f50', 'fawn': '#e5aa70', 'gray': '#bebebe', 'lilac': '#c8a2c8',  'mint': '#3eb489', 'pear': '#d1e231'}

for color in hex_colours:
    color = input("Color: ").lower()
    if color in hex_colours:
        print(hex_colours[color])
    elif color == ' ':
        break
    else:
        print("Enter a valid color")

