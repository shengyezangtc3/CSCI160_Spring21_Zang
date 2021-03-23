RGB = {
    "red"   : 0,
    "green" : 0,
    "blue"  : 0
}

# Get rgb color values
red_amount = int(input())
green_amount = int(input())
blue_amount = int(input())

RGB["red"] = red_amount
RGB["green"] = green_amount
RGB["blue"] = blue_amount

min_value = min(RGB.values())
print(RGB["red"]-min_value, RGB["green"]-min_value, RGB["blue"]-min_value)