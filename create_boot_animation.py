import argparse
import os
import tempfile
import zipfile
from PIL import Image
import gifextract

def create(source, width, height, fps, save_to):
    zip=True
    source_dir = ""
    temp_dir = None
    if os.path.isdir(source):
        source_dir = source
    elif os.path.isfile(source) and get_extension(source) == "gif":
        temp_dir = tempfile.TemporaryDirectory()
        gifextract.processImage(source, temp_dir.name)
        source_dir = temp_dir.name
    else:
        print("Error: invalid source path: " + source)
        return

    images = get_images_paths(source_dir)
    if len(images) <= 0:
        print("Error: no images to process")
        return

    if not os.path.exists(save_to):
        os.makedirs(save_to)

    path_to_desc_file = create_desc_file(save_to, width, height, fps)

    dir_for_images = save_to + "/part0"
    if not os.path.exists(dir_for_images):
        os.makedirs(dir_for_images)

    count = 0
    for img in images:
        count = transform_images(img, count, width, height, dir_for_images)

    with open(path_to_desc_file, "a") as f:
        print("p 1 0 part0", file=f)

    if zip is True:
        zip_file = zipfile.ZipFile(save_to + "/bootanimation.zip", mode="w",
                                   compression=zipfile.ZIP_STORED)

        zip_file.write(path_to_desc_file,
                       arcname=os.path.basename(path_to_desc_file))

        zip_dir(dir_for_images, zip_file)
        zip_file.close()

    print("Done")
    return True

    

def get_extension(t_path):
    path_parts = str.split(t_path, '.')
    extension = path_parts[-1:][0]
    extension = extension.lower()
    return extension


def get_images_paths(t_folder):
    if not os.path.isdir(t_folder):
        return list()

    image_extensions = ("jpg", "jpeg", "bmp", "png", "tiff")
    images = list()
    entries = os.listdir(t_folder)
    for entry in entries:
        file_path = os.path.join(t_folder, entry)
        extension = get_extension(file_path)
        if os.path.isfile(file_path) and extension in image_extensions:
            images.append(file_path)

    images.sort()
    return images


def create_desc_file(t_folder, width, height, fps):
    file_name = t_folder + "/desc.txt"
    fd = open(file_name, mode="w+")
    print("{} {} {}".format(width, height, fps), file=fd)
    return file_name


def transform_images(t_img_path, t_count, width, height, save_to_path):
    original_img = Image.open(t_img_path)

    # Scale image
    width_percent = (width / float(original_img.width))
    height_size = int((float(original_img.height) * float(width_percent)))
    original_img = original_img.resize((width, height_size), Image.LANCZOS)

    result_image = Image.new("RGB", (width, height), "white")

    width_pos = 0
    height_pos = int(height / 2 - original_img.height / 2)
    result_image.paste(original_img, (width_pos, height_pos))

    result_img_name = "{0:0{width}}.png".format(t_count, width=5)
    result_img_path = save_to_path + "/" + result_img_name
    result_image.save(result_img_path)
    t_count += 1
    return t_count


def zip_dir(t_path, zip_file):
    path_head, last_dir = os.path.split(t_path)
    images = get_images_paths(t_path)
    for img in images:
        img_path_in_zip = last_dir + "/" + os.path.basename(img)
        zip_file.write(img, arcname=img_path_in_zip,
                         compress_type=zipfile.ZIP_STORED)

