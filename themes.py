#!/usr/bin/python3
import glob
import os
from time import sleep


def add_random_letter(filename):
    if os.path.isfile(filename):
        base_name, ext = os.path.splitext(filename)
        new_name = f"{base_name}{random.choice(string.ascii_letters)}{ext}"
        # os.rename(filename, new_name)
        print(f"Renamed {filename} to {new_name}")
        return new_name
    return file_name


config_files = glob.glob("**/*.conf", recursive=True)
# print(config_files)
# exit()

try:
    os.mkdir("tapes")
    os.mkdir("media")
except:
    pass

for config_file in config_files:
    # print(f"*****{config_file}*****")
    # os.system(f"neofetch --config {config_file}")
    # sleep(0.5)
    file_name = config_file.split("/")[-1].split(".")[0]
    # print(file_name)
    # exit()
    with open("tapes/" + file_name + ".tape", "w+") as f:
        data = f"""
Output "media/{file_name}.gif"

Set FontSize 17
Set Width 1280
Set Height 720
Set FontFamily "ubuntumono Nerd Font mono"
Set Theme "Atom"

#Type "treefetch"
Hide
Type "neofetch --config /home/avik/Desktop/git_projects/github_repos/neofetch_themes/{config_file}"
Enter
Show
Sleep 5s
		"""
        f.write(data)

    # file_name = "tapes/" + file_name + ".tape"
    tape_name = "tapes/" + file_name + ".tape"
    os.system(f"vhs < {tape_name}")
    file_name = add_random_letter(file_name.split("/")[-1].replace(".tape", ".gif"))
    # print(file_name)
    with open("README.md", "a+") as f:
        f.writelines(
            f"### {file_name.split('.')[0]}\n![](media/{file_name.split('.')[0]}.gif)\n"
        )
    # exit()
