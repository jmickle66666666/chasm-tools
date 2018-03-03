class Datafile:
    def __init__(self, name, size, position, data):
        self.name = name
        self.size = size
        self.position = position
        self.data = data

    def get_data(self):
        self.data.seek(self.position)
        return self.data.read(self.size)

    def to_file(self, path):
        with open(path + self.name, "wb") as f:
            f.write(self.get_data())


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
                self.directory[i].to_file("out/")

    @staticmethod
    def read_directory_entry(data):
        name_size = int.from_bytes(data.read(1), 'little')
        name = data.read(name_size).decode('utf-8')
        data.read(12 - name_size)
        file_size = int.from_bytes(data.read(2), 'little')
        data.read(2)
        file_position = int.from_bytes(data.read(2), 'little')
        data.read(2)
        return Datafile(name, file_size, file_position, data)
