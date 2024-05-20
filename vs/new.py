from flask import Flask, request, render_template, jsonify
import cv2
import numpy as np

app = Flask(__name__)

def compare_histograms(hist1, hist2, method=cv2.HISTCMP_CORREL):
    return cv2.compareHist(hist1, hist2, method)

def detect_plagiarism(image1_path, image2_path):
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    hist1 = cv2.calcHist([gray_image1], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([gray_image2], [0], None, [256], [0, 256])

    similarity = compare_histograms(hist1, hist2)
    similarity_threshold = 0.9

    return similarity > similarity_threshold

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file1' not in request.files or 'file2' not in request.files:
            return jsonify({'error': 'Both files must be uploaded'})

        file1 = request.files['file1']
        file2 = request.files['file2']

        if file1.filename == '' or file2.filename == '':
            return jsonify({'error': 'Both files must be uploaded'})

        file1_path = 'uploaded_image1.jpg'
        file2_path = 'uploaded_image2.jpg'

        file1.save(file1_path)
        file2.save(file2_path)

        if detect_plagiarism(file1_path, file2_path):
            return jsonify({'message': 'Plagiarism Detected!'})
        else:
            return jsonify({'message': 'No Plagiarism Detected.'})

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
