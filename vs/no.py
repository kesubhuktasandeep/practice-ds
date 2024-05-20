import cv2
import numpy as np

def compare_histograms(hist1, hist2, method=cv2.HISTCMP_CORREL):
    return cv2.compareHist(hist1, hist2, method)

def main():
    # Load two images for comparison
    image1 = cv2.imread('image1.jpg')
    image2 = cv2.imread('image2.jpg')

    # Convert images to grayscale
    gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Calculate histograms for grayscale images
    hist1 = cv2.calcHist([gray_image1], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([gray_image2], [0], None, [256], [0, 256])

    # Compare histograms
    similarity = compare_histograms(hist1, hist2)

    # Define a similarity threshold (adjust as needed)
    similarity_threshold = 0.9

    # Perform plagiarism detection based on similarity
    if similarity > similarity_threshold:
        print("Plagiarism Detected!")
    else:
        print("No Plagiarism Detected.")

if __name__ == "__main__":
    main()
