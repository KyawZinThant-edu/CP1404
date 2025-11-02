HEX_COLOURS = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedAlmond": "#ffebcd",
    "blue": "#0000ff",
    "blueviolet": "#8a2be2",
    "brown": "#a52a2a"
}

print("Welcome to the Hex Colour Code Lookup!")
print("Available colours:", ", ".join(HEX_COLOURS.keys()))

colour_name = input("\nEnter colour name: ").strip()
while colour_name != "":
    try:
        # Try to find the colour (case-insensitive)
        # Convert input to title case to match dictionary keys
        formatted_name = colour_name.lower()
        hex_code = HEX_COLOURS[formatted_name]
        print(f"{formatted_name} is {hex_code}")
    except KeyError:
        print(f"Invalid colour name: '{colour_name}'")

    colour_name = input("\nEnter colour name: ").strip()

print("Goodbye!")