import cv2
import numpy as np

# 1. Gürültü Giderme
def denoise(image):
    return cv2.GaussianBlur(image, (5, 5), 0)

# 2. Kontrast Artırma (CLAHE)
def enhance_contrast(image):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    l = clahe.apply(l)

    merged = cv2.merge((l,a,b))
    return cv2.cvtColor(merged, cv2.COLOR_LAB2BGR)

# 3. Parlaklık Normalizasyonu
def normalize_brightness(image):
    return cv2.normalize(image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

# 4. Tüm pipeline
def preprocess_pipeline(image):
    image = denoise(image)
    image = enhance_contrast(image)
    image = normalize_brightness(image)
    return image