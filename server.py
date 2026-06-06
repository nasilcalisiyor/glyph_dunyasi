from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Absolute path to the images folder
IMAGE_FOLDER = os.path.join(app.root_path, 'static', 'images')

@app.route('/')
def index():
    # List all image files in the folder
    if not os.path.exists(IMAGE_FOLDER):
        return "Image folder not found!", 404

    images = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif'))]
    return render_template('index.html', images=images)

@app.route('/static/images/<filename>')
def image(filename):
    # Serve individual image files
    return send_from_directory(IMAGE_FOLDER, filename)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

if __name__ == '__main__':
    app.run(debug=True)
    
    
