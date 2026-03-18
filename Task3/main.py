from flask import Flask, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

BUCKET_NAME = "s2561435-_ccws_cw1_diet1"
STUDENT_ID = "S2561435"

# Dictionary mapping Table 1 numbers  filenames
file_map = {
    "1": "journey.jpg",
    "2": "music.jpg",
    "3": "wasgood.jpg"
}

@app.route('/')
def home():
    return """
    <h1>Task 3b: Metadata App</h1>
    <p>Click to view the metadata for each image:</p>
    <ul>
        <li><a href="/info/1">/info/1</a></li>
        <li><a href="/info/2">/info/2</a></li>
        <li><a href="/info/3">/info/3</a></li>
    </ul>
    """

# This route uses 'info' as the <chosenpath> to be different from Task 2
@app.route('/info/<image_num>')
def get_metadata(image_num):
    filename = file_map.get(image_num)
    
    if not filename:
        return jsonify({"error": "Image not found. Use 1, 2, or 3"}), 404

    # 1. Construct the REST API URL for metadata
    api_url = f"https://storage.googleapis.com/storage/v1/b/{BUCKET_NAME}/o/{filename}"

    try:
        # 2. Call the REST API method 
        response = requests.get(api_url)
        
        if response.status_code == 200:
            api_data = response.json()
            
            # 3. Create the subset JSON response with required fields
            subset = {
                "image_file_name": api_data.get("name"),
                "type_of_content": api_data.get("contentType"),
                "file_size": api_data.get("size"),
                "time_of_creation": api_data.get("timeCreated"),
                "student_id": STUDENT_ID,
                "request_time_and_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            return jsonify(subset)
        else:
            return jsonify({"error": "Could not fetch metadata from Google"}), response.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # 0.0.0.0 makes it accessible on local network/VM
    app.run(host="0.0.0.0", port=8080, debug=True)