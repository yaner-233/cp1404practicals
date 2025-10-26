color_codes = {
    'aliceblue': '#f0f8ff',
    'black': '#000000',
    'white': '#ffffff',
    'red': '#ff0800',
    'blue': '#0000ff',
    'green': '#66ff00',
    'yellow': '#fff600',
    'purple': '#8a2be2',
    'orange': '#cc5500',
    'pink': '#ff91af'
}
print(color_codes)

color_name = input("Enter color: ").strip()
while color_name != "":
    lower_color = color_name.lower()
    try:
        print(f"{color_name} ({lower_color}) : {color_codes[lower_color]}")
    except KeyError:
        print(f"Sorry whitout'{color_name}'message.")
    color_name = input("Enter color: ").strip()