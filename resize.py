from PIL import Image

def resize_image(input_path, output_path, size):
    """Resize the image to the specified size and save it."""
    with Image.open(input_path) as img:
        # Use the LANCZOS resampling filter for high-quality resizing
        img = img.resize(size, Image.Resampling.LANCZOS)
        img.save(output_path)

# Example usage
resize_image("./pictures/logo-no-background.png", "resized_logo.png", (500, 500))  # Resize to 100x100 pixels

