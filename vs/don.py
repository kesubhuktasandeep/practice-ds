from flask import Flask, request, jsonify
import numpy as np
import cv2

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # You can save the image to a temporary directory or process it directly
    # For this example, we'll assume you have saved it as 'uploaded_image.jpg'

    # Perform plagiarism detection on the uploaded image
    plagiarism_score = detect_plagiarism('uploaded_image.jpg')

    return jsonify({'plagiarism_score': plagiarism_score})

def detect_plagiarism(image_path):
    # Perform plagiarism detection using image processing algorithms
    # Replace this with your plagiarism detection code

    # Dummy example: Calculate the average pixel value
    image = cv2.imread(image_path)
    average_pixel_value = np.mean(image)

    return average_pixel_value

if __name__ == '__main__':
    app.run(debug=True)
