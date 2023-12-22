import os

n_frames = int(os.popen("ls source | wc -w").read())
if not os.path.exists("output"):
    os.makedirs("output")

for i in range(1, n_frames+1):
    fid = "%04d" % (i)
    cmd = "ffmpeg -y -i ./source/fig_" + fid + ".png -i ./qrcode/num" + str(i) + ".png -filter_complex \"overlay=0:0\" ./output/fig_" + fid + ".png"
    os.system(cmd)
