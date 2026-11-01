import tensorflow as tf
import numpy as np
from PIL import Image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# Load the trained fruit recognition model
MODEL_PATH = "fruit_recognition_model.keras"

print("Loading fruit recognition model...")

model = tf.keras.models.load_model(MODEL_PATH)

# Class order must match the order used during model training
CLASS_NAMES = ["apple", "banana", "orange"]

print("Model loaded successfully!")


def predict_fruit(image_path):
    """
    Predict whether an image contains an apple, banana, or orange.
    """

    # Open the image and convert it to RGB
    image = Image.open(image_path).convert("RGB")

    # Resize the image to 224 x 224 pixels
    image = image.resize((224, 224))

    # Convert the image to a NumPy array
    image_array = np.array(image, dtype=np.float32)

    # Add a batch dimension
    image_array = np.expand_dims(image_array, axis=0)

    # Apply MobileNetV2 preprocessing exactly once
    image_array = preprocess_input(image_array)

    # Predict the fruit
    predictions = model.predict(image_array, verbose=0)

    # Find the class with the highest prediction score
    predicted_index = int(np.argmax(predictions[0]))

    predicted_fruit = CLASS_NAMES[predicted_index]
    confidence = float(predictions[0][predicted_index]) * 100

    # Display the result
    print("\n------ Fruit Recognition Result ------")
    print(f"Predicted fruit: {predicted_fruit}")
    print(f"Confidence: {confidence:.2f}%")
    print("--------------------------------------")

    return predicted_fruit, confidence


if __name__ == "__main__":

    image_path = input(
        "\nEnter the path to a fruit image: "
    ).strip().strip('"')

    try:
        predict_fruit(image_path)

    except FileNotFoundError:
        print("Error: Image file not found. Check the image path.")

    except Exception as error:
        print(f"An error occurred: {error}")