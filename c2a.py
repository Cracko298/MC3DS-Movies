import cv2, os, sys
from PIL import Image
from py3dst import Texture3dst

def extract_and_resize_frames(video_path):
    out_dir = os.path.join(os.getcwd(), "animation_out")
    os.makedirs(out_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Cannot open video file.")
        return

    frame_count = 0
    output_index = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        resized = cv2.resize(frame, (256, 128), interpolation=cv2.INTER_AREA)
        for _ in range(1):
            filename = os.path.join(out_dir, f"{output_index}.png")
            cv2.imwrite(filename, resized)
            output_index += 1

        frame_count += 1

    cap.release()
    print(f"Done! Extracted {frame_count} frames, saved {output_index} images in {out_dir}")

def stack_frames_vertically(input_dir="animation_out", output_file="animation_atlas.png"):
    files = [f for f in os.listdir(input_dir) if f.endswith(".png")]
    files = sorted(files, key=lambda x: int(os.path.splitext(x)[0]), reverse=True)

    if not files:
        print("No PNG files found in the input directory.")
        return

    first_img = Image.open(os.path.join(input_dir, files[0]))
    width, height = first_img.size
    total_height = len(files) * height
    stacked_img = Image.new("RGB", (width, total_height))

    y_offset = 0
    for fname in files:
        img = Image.open(os.path.join(input_dir, fname))
        stacked_img.paste(img, (0, y_offset))
        y_offset += height

    stacked_img.save(output_file)
    print(f"Stacked {len(files)} frames into {output_file} ({width}x{total_height})")

def img_2_3dst():
    Image.MAX_IMAGE_PIXELS = None
    image = Image.open(".\\animation_atlas.png")
    texture = Texture3dst().fromImage(image)
    texture.export(".\\exampleAnimation.3dst")
    print("Animation Atlas Exported to: .\\exampleAnimation.3dst")

if __name__ == "__main__":
    video_file = str(sys.argv[1])
    extract_and_resize_frames(video_file)
    stack_frames_vertically()
    img_2_3dst()
