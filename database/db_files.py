import os
import uuid
from PIL import ImageFile
SHARES_FOLDER_PATH='./database/shares'


def save_img(img: ImageFile):
    """
    This function receives a Pillow image file\n
    and saves the image at SHARES_FOLDER_PATH with a unique ID
    and returns the path saved
    """
    if not os.path.isdir(SHARES_FOLDER_PATH):
        os.mkdir(SHARES_FOLDER_PATH)
    img_path = os.path.join(SHARES_FOLDER_PATH, str(uuid.uuid4())+ '.' + img.format.lower()).replace('\\','/')
    img.save(img_path)
    return img_path
