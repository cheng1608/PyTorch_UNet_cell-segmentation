from PIL import Image
import os


def rotate_image(input_path, output_dir, rotation_angle):
    filename, file_extension = os.path.splitext(os.path.basename(input_path))
    output_path = os.path.join(output_dir, f"{filename}_rotated{rotation_angle}{file_extension}")
    with Image.open(input_path) as img:
        rotated_img = img.rotate(rotation_angle, expand=True)
        rotated_img.save(output_path)

def crop_image(input_path, output_dir, crop_box):
    filename, file_extension = os.path.splitext(os.path.basename(input_path))
    output_path = os.path.join(output_dir, f"{filename}_crop{file_extension}")
    with Image.open(input_path) as img:
        cropped_img = img.crop(crop_box)
        cropped_img.save(output_path)


def process_images_in_folder(folder_path, output_dir, rotation_angle=90):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.tif', '.tiff', '.png')):
            input_path = os.path.join(folder_path, filename)
            rotate_image(input_path, output_dir, rotation_angle)

def crop_images_in_folder(folder_path, output_dir, crop_box=(0, 0, 512, 512)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.tif', '.tiff', '.png')):
            input_path = os.path.join(folder_path, filename)
            crop_image(input_path, output_dir, crop_box)




input_folder_path = r'D:\py_project\SS1\dataset2_medical\mask'  # 输入文件夹路径
output_folder_path = r'D:\py_project\SS1\dataset2_medical'  # 输出文件夹路径
rotation_angle = 270


#crop_images_in_folder(input_folder_path, output_folder_path)
def tif_to_png(tif_path, png_dir):
    filename, _ = os.path.splitext(os.path.basename(tif_path))
    png_path = os.path.join(png_dir, filename + '.png')
    with Image.open(tif_path) as img:
        img.save(png_path, 'PNG')


def batch_convert_tifs_to_pngs(tif_folder, png_folder):
    os.makedirs(png_folder, exist_ok=True)
    for filename in os.listdir(tif_folder):
        if filename.lower().endswith('.tif') or filename.lower().endswith('.tiff'):
            tif_path = os.path.join(tif_folder, filename)
            # 调用函数将TIFF文件转换为PNG文件
            tif_to_png(tif_path, png_folder)



tif_folder = 'D:\py_project\SS1\dataset2_medical\image'  # TIFF文件所在的文件夹路径
png_folder = r'D:\py_project\SS1\new_group_50\image2'  # PNG文件保存的目标文件夹路径
batch_convert_tifs_to_pngs(tif_folder, png_folder)


