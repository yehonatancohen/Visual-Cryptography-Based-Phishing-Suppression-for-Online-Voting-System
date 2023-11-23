import os
import boto3
import io
import uuid
from PIL.Image import Image
from PIL import Image as ImageOpen
AWS_BUCKET_NAME = os.environ['BUCKETEER_BUCKET_NAME']
AWS_ACCESS_KEY_ID = os.environ['BUCKETEER_AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['BUCKETEER_AWS_SECRET_ACCESS_KEY']
#s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
#s3.upload_file('C:/Users/gurgu/OneDrive/שולחן העבודה/תכנות/שנה 5/פרויקט גמר/Database connection testing/database/users.py', "bucketeer-dbd89d22-fa63-4680-a140-c7d5f41d0736", 'shares/users.py')
#ImageOpen.open(io.BytesIO(s3.get_object(Bucket=AWS_BUCKET_NAME, Key="shares/2c3220aa-46db-419c-91eb-fd1dab9d2208.png")['Body'].read())).show()

SHARES_FOLDER_PATH='shares/'   
CANDIDATES_IMG_FOLDER_PATH='candidates/'


def save_share(img: Image):
    """
    This function receives a Pillow image file\n
    and saves the image at SHARES_FOLDER_PATH with a unique ID
    and returns the path saved
    """
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    SHARE_PATH = SHARES_FOLDER_PATH + str(uuid.uuid4())+ '.png'
    byte_stream = io.BytesIO()
    img.save(byte_stream, format='PNG')
    byte_stream.seek(0)
    s3.put_object(Bucket=AWS_BUCKET_NAME, Key=SHARE_PATH, Body=byte_stream.read(), ContentType='image/png')

    return SHARE_PATH

def get_img_from_bucket(path):
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    response = s3.get_object(Bucket=AWS_BUCKET_NAME, Key=path)

    file_content = response['Body'].read()

    img = ImageOpen.open(io.BytesIO(file_content))

    return img

def save_candidate_img(img: Image):
    """
    This function receives a Pillow image file\n
    and saves the image at CANDIDATES_IMG_FOLDER_PATH with a unique ID
    and returns the path saved
    """
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    SHARE_PATH = CANDIDATES_IMG_FOLDER_PATH + str(uuid.uuid4())+ '.png'
    byte_stream = io.BytesIO()
    img.save(byte_stream, format='PNG')
    byte_stream.seek(0)
    s3.put_object(Bucket=AWS_BUCKET_NAME, Key=SHARE_PATH, Body=byte_stream.read(), ContentType='image/png')

    return SHARE_PATH
