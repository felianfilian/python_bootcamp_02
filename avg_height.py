def avg_height():
    print("average height caclulator")
    heights = [180, 152, 165]
    total_heights = 0
    for height in heights:
        total_heights += height
    avg_height = total_heights / len(heights)
    print("Average height: " + str(round(avg_height)))


