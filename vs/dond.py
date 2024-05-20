from flask import Flask, request, jsonify
import numpy as np
from skimage import io, img_as_float
from skimage.metrics import structural_similarity as ssim

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        uploaded_image = img_as_float(io.imread(file))
        uploaded_image_path = 'uploaded_image.jpg'
        io.imsave(uploaded_image_path, uploaded_image)
        return jsonify({'message': 'Image uploaded successfully'})

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Plagiarism Image Detection</title>
    </head>
    <body>
        <h1>Plagiarism Image Detection</h1>
        <form action="/" method="POST" enctype="multipart/form-data">
            <input type="file" name="file" accept="image/*">
            <input type="submit" value="Upload Image">
        </form>

        <h2>Plagiarism Detection Result:</h2>
        <div id="result"></div>

        <form action="/detect_plagiarism" method="POST" enctype="multipart/form-data">
            <input type="file" name="file" accept="image/*">
            <input type="submit" value="Detect Plagiarism">
        </form>
    </body>
    </html>
    """

@app.route('/detect_plagiarism', methods=['POST'])
def detect_plagiarism():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    uploaded_image = img_as_float(io.imread(file))
    uploaded_image_path = 'uploaded_image.jpg'

    # Load the uploaded image and a reference image for plagiarism detection
    reference_image = io.imread('reference_image.jpg')

    # Calculate the Structural Similarity Index (SSI) between the images
    ssi_score = ssim(uploaded_image, reference_image, multichannel=True)

    return jsonify({'ssi_score': ssi_score})

if __name__ == '__main__':
    app.run(debug=True)
