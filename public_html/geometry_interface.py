from geometry_generator import *
import js
import svgwrite

# await micropip.install("svgwrite")

interface_element = Element("interface")

print("print test!")

diameter = 100

center = [diameter, diameter]

triangle = Polygon(3, diameter, center)

svg_output = Element("svg-output")

triangle.draw()

svg_string = drawing_global.tostring()

# print(svg_string)

svg_output.element.innerHTML = svg_string

def test_function():
    print("test function ran!")
    
repl = Element("py-repl")
    
def run_geometry():
    drawing_global = svgwrite.Drawing(output_path)
    print(f"repl contents was {repl.element.getPySrc()}")
    