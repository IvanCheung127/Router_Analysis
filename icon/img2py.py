import base64

with open('ico1.ico', 'rb') as fin:
    image_data = fin.read()
    base64_data = base64.b64encode(image_data)

    fout = open('ico1.py', 'w')
    fout.write("img = '%s'" % base64_data.decode())
    fout.close()