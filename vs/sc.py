import cv2
import numpy as np
import os

def compare_histograms(hist1, hist2, method=cv2.HISTCMP_CORREL):
    return cv2.compareHist(hist1, hist2, method)

def detect_plagiarism(image_path1, image_path2):
    image1 = cv2.imread(image_path1)
    image2 = cv2.imread(image_path2)

    gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    hist1 = cv2.calcHist([gray_image1], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([gray_image2], [0], None, [256], [0, 256])

    similarity = compare_histograms(hist1, hist2)

    similarity_threshold = 0.9

    if similarity > similarity_threshold:
        result = "Plagiarism Detected!"
    else:
        result = "No Plagiarism Detected."

    return result

def main():
    image_folder = 'your_folder_path_here'
    image_files = os.listdir(image_folder)

    for i in range(len(image_files)):
        for j in range(i + 1, len(image_files)):
            image_path1 = os.path.join(image_folder, image_files[i])
            image_path2 = os.path.join(image_folder, image_files[j])

            result = detect_plagiarism(image_path1, image_path2)
            print(f"Comparison between {image_files[i]} and {image_files[j]}: {result}")

if __name__ == "__main__":
    main()
