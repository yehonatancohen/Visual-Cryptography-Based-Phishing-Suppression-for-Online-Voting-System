from PIL import Image, ImageDraw, ImageFont
import os, sys
from random import SystemRandom
random = SystemRandom()

xrange = range
images_location = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images\\")

# Create the original image with text and save it
def create_original_image(x,y,text):
    img = Image.new('1', (x, y), 1)
    draw = ImageDraw.Draw(img)
    font_size = 70
    font = ImageFont.truetype('arial.ttf', font_size)
    _,_,text_width, text_height = draw.textbbox((0,0),text, font=font)
    draw.text(((x-text_width)/2, (y-text_height)/2), text, font=font, fill=0, antialias=False)
    img.save(images_location + 'original.png', 'PNG')
    return img


def create_shares(original_image):
    out_filename_A = images_location + "share_A.png"
    out_filename_B = images_location + "share_B.png"

    img = original_image.convert('1')  # convert image to 1 bit

    print("Image size: {}".format(img.size))
    # Prepare two empty slider images for drawing
    width = img.size[0]*2
    height = img.size[1]*2
    print("{} x {}".format(width, height))
    out_image_A = Image.new('1', (width, height))
    out_image_B = Image.new('1', (width, height))
    draw_A = ImageDraw.Draw(out_image_A)
    draw_B = ImageDraw.Draw(out_image_B)


    patterns = ((1, 1, 0, 0), (1, 0, 1, 0), (1, 0, 0, 1),
                (0, 1, 1, 0), (0, 1, 0, 1), (0, 0, 1, 1))
    # Cycle through pixels
    for x in xrange(0, int(width/2)):
        for y in xrange(0, int(height/2)):
            pixel = img.getpixel((x, y))
            pat = random.choice(patterns)
            # A will always get the pattern
            draw_A.point((x*2, y*2), pat[0])
            draw_A.point((x*2+1, y*2), pat[1])
            draw_A.point((x*2, y*2+1), pat[2])
            draw_A.point((x*2+1, y*2+1), pat[3])
            if pixel == 0:  # Dark pixel so B gets the anti pattern
                draw_B.point((x*2, y*2), 1-pat[0])
                draw_B.point((x*2+1, y*2), 1-pat[1])
                draw_B.point((x*2, y*2+1), 1-pat[2])
                draw_B.point((x*2+1, y*2+1), 1-pat[3])
            else:
                draw_B.point((x*2, y*2), pat[0])
                draw_B.point((x*2+1, y*2), pat[1])
                draw_B.point((x*2, y*2+1), pat[2])
                draw_B.point((x*2+1, y*2+1), pat[3])

    out_image_A.save(out_filename_A, 'PNG')
    out_image_B.save(out_filename_B, 'PNG')
    return (out_image_A, out_image_B)


def create_combination(out_image_A, out_image_B):
    width = out_image_A.width
    height = out_image_A.height
    out_image_combined = Image.new('1', (width, height))

    for x in range(width):
        for y in range(height):
            # Get the pixel values for the two input images
            pixel_A = out_image_A.getpixel((x, y))
            pixel_B = out_image_B.getpixel((x, y))

            # If either pixel is black, output black. Otherwise, output white.
            if pixel_A == 0 or pixel_B == 0:
                out_image_combined.putpixel((x, y), 0)
            else:
                out_image_combined.putpixel((x, y), 1)



    out_filename_combined = images_location + "share_combined.png"
    out_image_combined.save(out_filename_combined, 'PNG')
    print("Combined image saved as: {}".format(out_filename_combined))

original_image = create_original_image(300, 150, "cohen")
(share_img_A, share_img_B) = create_shares(original_image)
create_combination(share_img_A, share_img_B)