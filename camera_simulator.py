from pathlib import Path


def capture_image():
    """Simulate capturing an image using an ESP32-CAM."""

    image_path = input(
        "Enter the fruit image path (e.g., test_images/apple.jpg): "
    ).strip().strip('"')

    image_file = Path(image_path)

    if not image_file.is_file():
        print(f"Error: Image not found: {image_file.resolve()}")
        return None

    print("\n[CAMERA] Image captured successfully.")
    print(f"[CAMERA] Image path: {image_file.resolve()}")

    return image_file


if __name__ == "__main__":
    capture_image()