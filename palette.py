from PIL import Image


class Palette:
    def __init__(self, data):
        self.colors = []
        for i in range(256):
            self.colors.append((data[(i * 3) + 0] * 4,
                                data[(i * 3) + 1] * 4,
                                data[(i * 3) + 2] * 4))

    def to_image(self):
        img = Image.new("RGBA", (16,16), "white")
        for i in range(256):
            img.putpixel((i % 16, i // 16), self.colors[i])
        return img

    def get_color(self, index):
        return self.colors[index]