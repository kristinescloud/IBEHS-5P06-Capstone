import time

from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput

cam1 = Picamera2(0)
cam1.start_preview(Preview.QTGL, x=100,y=300,width=400,height=300)
# ~ cam2 = Picamera2(1)
# ~ cam2.start_preview(Preview.QTGL, x=500,y=300,width=400,height=300)
# ~ video_config1= cam1.create_video_configuration()
# ~ cam1.configure(video_config1)
# ~ video_config2 = cam2.create_video_configuration()
# ~ cam2.configure(video_config2)
cam1.start()
# ~ cam2.start()

# ~ encoder1 = H264Encoder(10000000)
# ~ output1 = FfmpegOutput('testcam1movingpeople.mp4')
# ~ encoder2= H264Encoder(10000000)
# ~ output2 = FfmpegOutput('testcam2movingpeople.mp4')

# ~ cam1.start_recording(encoder1, output1)
# ~ cam2.start_recording(encoder2, output2)

time.sleep(1e8)

print("test")

# ~ cam1.stop_preview()
# ~ cam2.stop_preview()

# ~ cam2.stop()
# ~ cam1.stop()
