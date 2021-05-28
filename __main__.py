from moviepy.editor import *

file_path = sys.argv[1]

if len(sys.argv) != 2:
    print("Insufficient arguments")
    print("path of target directory")
    sys.exit()

targets = os.listdir(file_path)
have_to_remove = []

def determine(x):
    if not x.endswith(".mp4") or not "." in x:
        return True
    return False

targets = [x for x in targets if not determine(x)]


for target in targets:
    targetname = target[:len(target)-4]
    print("target name : {}".format(targetname))
    clip = VideoFileClip(file_path+"/"+target)
    duration = clip.duration # float
    duration = int(duration)
    start = duration-60
    if start <= 0:
        start = 0
    
    clip = clip.subclip(start, duration)
    clip.write_videofile(file_path+"/"+targetname+"_last_1_min.mp4")