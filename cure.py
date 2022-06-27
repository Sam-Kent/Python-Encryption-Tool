import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256


for path, dir, files in os.walk("/root/Documents/student/test"):
    for file in files:
        with open(os.path.join(path, file), "rb") as inp:
            fsize = long(inp.read(16))
            IV = inp.read(16)
            hash = SHA256.new("*&$%^@#!%$@$!@erfgfxchgjhFGDFHJGHKJHJGHHKJHH57676877ggfgfd&^%$%#$#$rfrfsdg".encode())
            key = hash.digest()
            cipher = AES.new(key, AES.MODE_CBC, IV)
            outf = file[15:]
            chunksize = 64*1024
            with open(os.path.join(path, outf), 'wb') as outp:
                while True:
                    data = inp.read(chunksize)

                    if len(data) == 0:
                        break

                    outp.write(cipher.decrypt(data))
                outp.truncate(fsize)
