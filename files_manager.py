import os, shutil, sys, re

U_NAME = os.getlogin()
download_dir = fr"C:\\users\\{U_NAME}\Downloads"
arrange_dir = fr"C:\\users\\{U_NAME}\Downloads"

comp_fold = os.path.join(arrange_dir, "compressed")
program_fold = os.path.join(arrange_dir, "programs")
document_fold = os.path.join(arrange_dir, "documents")
audio_fold = os.path.join(arrange_dir, "audio")
pictures_fold = os.path.join(arrange_dir, "pictures")
videos_fold = os.path.join(arrange_dir, "videos")
others_fold = os.path.join(arrange_dir, "others")
files = [os.path.join(download_dir, x) for x in os.listdir(download_dir)]


def make_dir(folder):
    try:
        os.mkdir(folder)
    except Exception as e:
        pass


for out_fold in [others_fold, videos_fold, comp_fold, audio_fold, document_fold, pictures_fold, program_fold]:
    make_dir(out_fold)


def check_file_type(file_name):
    if re.search("^.*\.(jpg|ico|bmp|psd|svg|tif|svg|gif|png)$", file_name):
        return pictures_fold
    elif re.search("^.*\.(doc|pdf|docx|rtf|txt|wpd|rtf|ppt)$", file_name):
        return document_fold
    elif re.search("^.*\.(exe|EXE|py|msi)$", file_name):
        return program_fold
    elif re.search("^.*\.(aif|cda|mid|midi|mp3|mpa|ogg|wav|wma)$", file_name):
        return audio_fold
    elif re.search("^.*\.(zip|7z|arj|deb|pkg|rar|rpm|gz|zip|bin|dmg|iso)$", file_name):
        return comp_fold
    elif re.search("^.*\.(3g2|3gp|avi|flv|h264|264|m4v|mkv|mov|mp4|mpg|mpeg)$", file_name):
        return videos_fold
    else:
        return others_fold


for file in files:
    if "." in file:
        output_fold = check_file_type(file)
        print(os.path.join(output_fold, file.split("/")[-1]))
        shutil.move(file, os.path.join(output_fold, file.split("\\")[-1]))
