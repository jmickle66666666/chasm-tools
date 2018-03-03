import binfile

csm = binfile.BinFile("CSM.BIN")

print(csm.num_files)
print(csm.directory[0].name)
