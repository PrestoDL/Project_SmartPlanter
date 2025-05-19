import datetime
import csv
from capture import capture_image
from analyze import analyze_image

def append_log(data, log_file="log.csv"):
    header = ["date", "r", "g", "b", "status", "area"]
    today = datetime.date.today().isoformat()

    with open(log_file, "a", newline="") as f:
        writer = csv.writer(f)
        if f.tell() == 0:
            writer.writerow(header)
        writer.writerow([today] + list(data["rgb"]) + [data["status"], data["area"]])

if __name__ == "__main__":
    img_path = capture_image()
    result = analyze_image(img_path)
    print(f"[{datetime.date.today()}] 상태: {result['status']} / 면적: {result['area']:.1f} 픽셀²")
    append_log(result)
