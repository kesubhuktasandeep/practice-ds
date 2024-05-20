from flask import Flask, render_template, request
import cv2
import numpy as np

app = Flask(__name__)

def compare_histograms(hist1, hist2, method=cv2.HISTCMP_CORREL):
    return cv2.compareHist(hist1, hist2, method)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect_plagiarism():
    image1 = request.files['image1']
    image2 = request.files['image2']

    gray_image1 = cv2.cvtColor(cv2.imread(image1), cv2.COLOR_BGR2GRAY)
    gray_image2 = cv2.cvtColor(cv2.imread(image2), cv2.COLOR_BGR2GRAY)

    hist1 = cv2.calcHist([gray_image1], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([gray_image2], [0], None, [256], [0, 256])

    similarity = compare_histograms(hist1, hist2)
    similarity_threshold = 0.9

    if similarity > similarity_threshold:
        result = "Plagiarism Detected!"
    else:
        result = "No Plagiarism Detected."

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)