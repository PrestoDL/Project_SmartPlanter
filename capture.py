import datetime
import os

def capture_image(save_dir="images"):
    os.makedirs(save_dir, exist_ok=True)
    today = datetime.date.today().isoformat()
    filename = f"{today}.jpg"
    path = os.path.join(save_dir, filename)

    os.system(f"fswebcam -r 640x480 --no-banner {path}")

    return path
