#Drill 2
from pyscript import document, display


def area_triangle(base, height):
    return {'base': base, 'height': height}

def computing_area(e):
    output = document.getElementById("display1")
    output.innerHTML = ""

    base1 = int(document.getElementById("Input1").value)
    height1 = int(document.getElementById("Input2").value)

    area67 = (base1 * height1) / 2
    triangle_info = area_triangle(base1, height1)

    display(f'Base: {base1} Height: {height1} Area: {area67}',
            target="display1")
    display(triangle_info, target="display1")