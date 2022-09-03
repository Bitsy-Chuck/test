import json
import os

# Read db and generate temp text file with video names for input.
import subprocess


def generate_temp_input_file():
    return None


def equalize_resolution():
    os.system("ffmpeg -y -i mylist.txt -vf \"[in]scale=iw*min(480/iw\,320/ih):ih*min(480/iw\,320/ih)[scaled]; ["
              "scaled]pad=480:320:(480-iw*min(480/iw\,320/ih))/2:(320-ih*min(480/iw\,320/ih))/2[padded]; ["
              "padded]setsar=1:1[out]\" -c:v libx264 -c:a copy \"%%~ni_shrink.mp4\"")
    return None


def equalize_SAR():
    return None


def get_video_metadata(path, name) -> json:
    abs_path = os.path.abspath(path)
    command = "ffprobe -v quiet -print_format json -show_format  -show_streams {}".format(abs_path + "/" + name)
    res = json.loads(subprocess.check_output(command, shell=True)) # TODO: Remove shell=true
    return res


def fix_scale(path, file):
    cmd = "ffmpeg -y -i {} -vf " \
          "\"[in]scale=iw*min(480/iw\,320/ih):ih*min(480/iw\,320/ih)[scaled]; " \
          "[scaled]pad=480:320:(480-iw*min(480/iw\,320/ih))/2:(320-ih*min(480/iw\,320/ih))/2[padded]; " \
          "[padded]setsar=1:1[out]\" -c:v libx264 -c:a copy " \
          "\"{}\"".format(file, "output-" + file)
    os.system(cmd)
    if subprocess.check_call(cmd) != 0:
        raise Exception("cannot scale video : {}".format(path + "/" + file))
    #     write to db
    with open(".assets/in.txt", 'a') as f:
        f.write("file {}".format("output-{}".format(file)))
    print("wrote to file")


def merge():
    cmd = "ffmpeg -i in.txt -filter_complex \"[0]setdar=16/9[a];[1]setdar=16/9[b]; [a][0:a][b][1:a]concat=n=2:v=1:a=1\" -vsync 2 output.mp4"


def get_videos_to_merge():
    # fetch from db

    return None


def get_video_duration(path, name) -> float:
    return float(get_video_metadata(path, name)['format']['duration'])


def merge_video():
    video_meta1 = get_video_metadata()
    video_meta2 = get_video_metadata()

    # get smaller resolution video
    # equalize resolution
    # equalize SAR
    # Merge video


def t1():
    records = db.

