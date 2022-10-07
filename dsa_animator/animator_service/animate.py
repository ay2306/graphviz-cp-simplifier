import os
import sys
from shutil import copyfile

from animator_service.animations import animation_handler


def convert_array_to_string(arr):
    out = ""
    for i in arr:
        if len(out) > 1:
            out += ","
        tmp = i.replace('\n', '\\\n')
        out += f"'{tmp}'"
    return out


def animate(animation_name, input_directory="", input_file=""):
    # copyfile(INPUT_FILE, OUTPUT_FILE)
    # FILE_WRITER = open(OUTPUT_FILE, 'a+')
    data = ""
    with open("animator_service/templates/basic.html", "r") as txt_file:
        data += '\n'.join(txt_file.readlines())
    data += convert_array_to_string(animation_handler.run_animation(animation_name))
    data += "\n] \n</script>"
    return data
    # print(data)
    # print('data
    # ', data)
    # FILE_WRITER.write(data)


def process_flags():
    global flags
    global OUTPUT_FILE
    global INPUT_FILE
    populate_flags_with_default()
    for flag in sys.argv[1:]:
        key, value = split_flag(flag)
        flags[key] = value

    OUTPUT_FILE = f'{CWD}/{flags["output_directory"]}/{flags["output_name"]}.html'
    INPUT_FILE = f'{CWD}/{flags["input_directory"]}/{flags["input_name"]}.html'
