from flask import Flask

app = Flask(__name__)

# Dictionary mapping the ID (1, 2, 3) to your specific images
# Note: I've updated the keys to '1', '2', and '3' to match Table 1
image_data = {
    "1": {
        "url": "https://storage.googleapis.com/s2561435-_ccws_cw1_diet1/journey.jpg",
        "caption": "Pause and enjoy the journey."
    },
    "2": {
        "url": "https://storage.googleapis.com/s2561435-_ccws_cw1_diet1/music.jpg",
        "caption": "Music makes everything beautiful"
    },
    "3": {
        "url": "https://storage.googleapis.com/s2561435-_ccws_cw1_diet1/wasgood.jpg",
        "caption": "Wasgood hommie, don't forget to be grateful."
    }
}

# The <chosenpath> here is 'view'. You can change this to anything you like.
@app.route('/view/<image_num>')
def display_image(image_num):
    if image_num in image_data:
        img = image_data[image_num]
        return f"""
        <html>
        <head>
            <title>App Engine Viewer - Image {image_num}</title>
            <style>
                body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; padding: 50px; background-color: #f4f4f9; }}
                .container {{ background: white; padding: 20px; display: inline-block; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); }}
                img {{ max-width: 500px; border-radius: 10px; }}
                h2 {{ color: #333; }}
                .caption {{ font-style: italic; color: #555; margin-top: 15px; font-size: 1.2em; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h2>Task 2d: Image {image_num}</h2>
                <p>Student: Shanon Mwangi (S2561435)</p>
                <hr>
                <img src="{img['url']}" alt="Cloud Image {image_num}">
                <p class="caption">"{img['caption']}"</p>
                <br>
                <a href="/">Back to Home</a>
            </div>
        </body>
        </html>
        """
    return "<h1>Image Not Found</h1><p>Please use /view/1, /view/2, or /view/3</p>", 404

@app.route('/')
def home():
    return "<h1>App Engine Image Viewer</h1><p>Try navigating to <a href='/view/1'>/view/1</a></p>"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)