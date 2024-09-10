import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:, %(message)s')

project_name = "Yolov5 with FPN head"


list_of_files = [
    "models/yolov5_fpn.yaml",  # YOLOv5 model config with FPN
    "train.ipynb",  # Training script
    "detect.ipynb",  # Detection script
    ".github/workflows/.gitkeep",  # GitHub workflows placeholder
    "setup.py",  # Setup file for packaging
]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating a new file: {filepath}")

    else:
        logging.info(f"{filename} already exists!")