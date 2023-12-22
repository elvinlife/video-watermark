## This repo shows how to add qr-code to every frame in a video

### Generate qr-code images
Inside the `qrcode` folder, run "encode.py" to generate qr-code pngs. Here, every picture represents a number.

### Add watermark to every frame
* Run "bash video2png.sh" to decode a video to pictures
* Run "python3 watermark.py" to add the corresponding qr-code(the frame id) to every decoded picture
* Run "bash png2video.sh" to encode the pictures with qr-code into a video

### Decode the qr-code attached to every frame
* Run "python3 decode_qrcode.py" to decode the qr-code attached with a frame
