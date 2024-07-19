import os
import glob
import json
import cv2
import numpy as np
from PIL import Image
from tqdm import tqdm


def create_mask_from_json(json_path, dest_root):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    image_height = data['imageHeight']
    image_width = data['imageWidth']
    mask = np.zeros((image_height, image_width), dtype=np.uint8)

    for shape in data['shapes']:
        if shape['label'] == 'black':
            points = np.array(shape['points'], dtype=np.int32)
            cv2.fillPoly(mask, [points], 255)
        if shape['label'] == 'white':
            points = np.array(shape['points'], dtype=np.int32)
            cv2.fillPoly(mask, [points], 120)

    mask_image = Image.fromarray(mask)

    json_dirname = os.path.dirname(json_path)
    mask_dirname = json_dirname.replace(root, dest_root)
    os.makedirs(mask_dirname, exist_ok=True)

    mask_filename = os.path.basename(json_path).replace('.json', '.png')
    mask_path = os.path.join(mask_dirname, mask_filename)

    mask_image.save(mask_path)
    print(f"Saved mask to {mask_path}")


if __name__ == "__main__":
    root = r"C:\Users\lenovo\Desktop\TEM"  # 替换为存放JSON文件的根目录
    dest = r"D:\py_project\SS1\dataset2_medical\mask"  # 替换为你希望保存掩码图像的根目录

    json_files = glob.glob(os.path.join(root, '**', '*.json'), recursive=True)

    for json_file in tqdm(json_files):
        create_mask_from_json(json_file, dest)
