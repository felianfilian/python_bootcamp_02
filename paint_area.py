def paint_cans(height, width):
    can_count = height * width / 5
    print(f"{height} x {width} = {can_count}")


def paint_area():
    print("paint area")
    height = int(input("wall height:\n"))
    width = int(input("wall width:\n"))
    paint_cans(height, width)


