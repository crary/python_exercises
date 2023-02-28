

def rectangleDrawing(width,height):
    if width < 1 or height < 1:
        return

    for _ in range(height):
        for _ in range(width):
            print('#', end='')
        print()

rectangleDrawing(2,6)