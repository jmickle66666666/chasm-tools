class Datafile:
    def __init__(self, name, size, position):
        self.name = name
        self.size = size
        self.position = position
        self.data = None
        self.ext = name[name.find('.')+1:]

    def to_file(self, path):
        with open(path + self.name, "wb") as f:
            f.write(self.data)


class BinFile:
    def __init__(self, path):

        self.directory = []
        self.num_files = 0

        with open(path, "rb") as f:
            f.read(4)
            self.num_files = int.from_bytes(f.read(2), 'little')
            self.directory = []

            for i in range(self.num_files):
                self.directory.append(self.read_directory_entry(f))

            for i in range(self.num_files):
                f.seek(self.directory[i].position)
                self.directory[i].data = f.read(self.directory[i].size)
                self.directory[i].to_file("out/")

    def get_entry(self, name):
        for i in range(len(self.directory)):
            if self.directory[i].name == name:
                return self.directory[i].data
        return None

    @staticmethod
    def read_directory_entry(data):
        name_size = int.from_bytes(data.read(1), 'little')
        name = data.read(name_size).decode('utf-8')
        data.read(12 - name_size)
        file_size = int.from_bytes(data.read(4), 'little')
        file_position = int.from_bytes(data.read(4), 'little')
        return Datafile(name, file_size, file_position)
