from PIL import Image
import os
from pathlib import Path


def create_gif(image_folder, output_name, duration=300):
    images = []

    for file_name in sorted(os.listdir(image_folder)):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(image_folder, file_name)
            img = Image.open(image_path).convert("RGB")
            images.append(img)

    if not images:
        print("❌ No images found!")
        return

    images[0].save(
        output_name,
        save_all=True,
        append_images=images[1:],
        duration=duration,
        loop=0
    )

    print("✅ GIF created successfully!")

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FOLDER = BASE_DIR / "input_images"
OUTPUT_FOLDER = BASE_DIR / "output"
INPUT_FOLDER.mkdir(exist_ok=True)
OUTPUT_FOLDER.mkdir(exist_ok=True)

OUTPUT_GIF = OUTPUT_FOLDER / "output.gif"

create_gif(str(INPUT_FOLDER), str(OUTPUT_GIF), 300)