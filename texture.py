from PIL import Image


class Texture:
    def __init__(self, data):
        self.width = int.from_bytes(bytearray(data[2:4]), 'little')
        self.height = int.from_bytes(bytearray(data[4:6]), 'little')
        self.data = data

    def to_image(self, palette):
        img = Image.new("RGBA", (self.width, self.height), "black")
        for i in range(self.width * self.height):
            img_x = i % self.width
            img_y = i // self.width
            img.putpixel((img_x, img_y), palette.get_color(self.data[800 + i]))
        return img