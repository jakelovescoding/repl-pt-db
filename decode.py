from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d
import zlib

def unobscure(obscured: bytes) -> bytes:
    return zlib.decompress(b64d(obscured))


arr = []
with open("db.txt") as file:
    line = file.readlines()
    for i in line:
        arr.append(i.rstrip())
print(arr)

for i in arr:
    print(unobscure(i))