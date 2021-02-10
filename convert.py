import ffmpeg_streaming
from ffmpeg_streaming import Formats
import os 
import ntpath

class VideoStreaming():
    def __init__(self,path):
        self.path = path
        self.output_path = "/home/yipl/Workspace/freelance/live-streaming/media/"

    def create_dir(self,directory_name):
        parent_dir = self.output_path
        directory = directory_name
        path = os.path.join(parent_dir, directory) 
        os.mkdir(path)
        current_path = os.path.abspath(os.path.join(parent_dir, directory))
        print(current_path)
        print("Directory '% s' created" % directory) 
        return current_path


    def convert_to_hls(self):
        try:
            video = ffmpeg_streaming.input(self.path)
            directory_name = ntpath.basename(self.path).split(".")[0]
            current_path = self.create_dir(directory_name)
            final_path = os.path.abspath(os.path.join(current_path, directory_name+'.m3u8'))
            print("Your m3u8 file is in '% s 'this directory" %final_path)
            print("Converting !!")
            hls = video.hls(Formats.h264())
            hls.auto_generate_representations()
            hls.output(final_path)
            print('Done!!')
        except Exception as e:
            print(e)



video_path = input("Enter yoiur video path !!!")
instance = VideoStreaming(video_path)
instance.convert_to_hls()


# video = ffmpeg_streaming.input(video_path)
# print("Converting")
# hls = video.hls(Formats.h264())
# hls.auto_generate_representations()
# hls.output('/home/yipl/Workspace/freelance/live-streaming/media/suyoj2.m3u8')
# print('Done!!')