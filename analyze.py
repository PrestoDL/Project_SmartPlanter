import joblib
from utils.color_utils import get_avg_color
from utils.area_utils import get_lettuce_area

def analyze_image(image_path, model_path="models/status_model.pkl"):
    avg_rgb = get_avg_color(image_path)

    model = joblib.load(model_path)
    status = model.predict([avg_rgb])[0]

    area = get_lettuce_area(image_path)

    return {
        "rgb": avg_rgb,
        "status": status,
        "area": area
    }
