import qrcode

# set the maximum frame number
max_num = 100

for i in range(max_num):
    fname = "num" + str(i) + ".png"
    img = qrcode.make(str(i))
    img.save(fname)
