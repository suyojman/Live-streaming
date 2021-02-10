# Live-streaming
This is a simple implementation of HTTP Live streaming(HLS) using python and HTML

# Installation Process

1. Create a virtual environment of python 3.6
2. Install all the dependencies mentioned in the requirements.txt file i.e pip install -r requirements.txt
3. Change the output path of your machine in the convert.py file @line 9
4. Run the convert.py file to convert the video into .m3u8 extension i.e python convert.py
5. You will have to enter the path of the video which you want to convert. For example : /home/user/Downloads/video2.mp4
6. After the conversion is completed..Please note down the path where the video has been converted.It will be shown in the terminal itself after conversion
7. Run a simple http server by running the following command : python3 -m http.server 8000 
8. Open the browser and goto 127.0.0.1:8000
9. You will see a video player as well as an input field for the video path
10.Enter the video path which you had just noted down and Press Play
11. The video will be played according to Adaptive Bitrate Streaming using HLS
