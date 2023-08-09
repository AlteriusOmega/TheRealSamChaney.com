from geometry_generator import *
import js
import svgwrite

print(f"geometry_interface.py ran!")

interface_element = Element("interface")

svg_output_width = 500
diameter = svg_output_width / 2

center = [svg_output_width*0.5, svg_output_width*0.5]
print(f"center is {center}")

svg_output = Element("svg-output")

# Note, drawing_global is global variable from geometry_generator.py itself 

repl = Element("py-repl")

def render_drawing_html():
    print(f"render_drawing_html ran!")
    print(f"printed right after printing render_drawing_html ran!")
    svg_string = drawing_global.tostring()
    print(f"svg_string is {svg_string}")
    svg_output.element.innerHTML = svg_string

def clear_drawing():
    global drawing_global
    print(f"clear_drawing ran! and drawing is {drawing_global} and drawing xml is {drawing_global.get_xml()}")
    drawing_global = svgwrite.Drawing(output_path)
    render_drawing_html() # Render the drawing to update the page with empty drawing