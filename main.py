from flask import Flask
from PIL import Image

app = Flask(__name__)

def find_dominant_color(filename):
    #Resizing parameters
    width, height = 150,150
    image = Image.open(filename)
    image = image.resize((width, height),resample = 0)
    #Get colors from image object
    pixels = image.getcolors(width * height)
    #Sort them by count number(first element of tuple)
    sorted_pixels = sorted(pixels, key=lambda t: t[0])
    #Get the most frequent color
    dominant_color = sorted_pixels[-1][1]
    return dominant_color

filename = r"C:\Users\WINDOWS 10\Desktop\hackCBS4.0-responsive\assets\images\first.png"
color = find_dominant_color(filename)
print(color)

@app.route('/')
def home():
    return "<h1>Home Page</h1>"

if __name__ == 'main':
    app.run(debug=True)