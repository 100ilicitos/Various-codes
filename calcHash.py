# Calculate hash file
# by Busyman.INc

import hashlib

BLOCKSIZE = 65536
fopen = 'PT.pdf'
hasher = hashlib.md5()
with open(fopen, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
print(hasher.hexdigest())
