from PIL import Image, ImageDraw

# Set the size of the image
width = 200
height = 200

# Set the string to be used as the pattern
pattern = "Hello World!"

# Create a new image object
image = Image.new('1', (width, height), 255)

# Generate two random shares
share1 = Image.new('1', (width, height), 255)
share2 = Image.new('1', (width, height), 255)

# Create a draw object
draw = ImageDraw.Draw(image)

# Draw the pattern on the image
for i, char in enumerate(pattern):
    x = i * 10
    y = ord(char) % height
    draw.text((x, y), char, fill=0)

# Split the image into two shares
for x in range(width):
    for y in range(height):
        pixel = image.getpixel((x, y))
        if pixel == 0:
            share1.putpixel((x, y), 0)
            share2.putpixel((x, y), 255)
        else:
            share1.putpixel((x, y), 255)
            share2.putpixel((x, y), 0)

# Save the shares as separate images
share1.save('share1.png')
share2.save('share2.png')

# Represent the images as text
print('Share 1:')
print(share1.tobytes().hex())

print('Share 2:')
print(share2.tobytes().hex())
