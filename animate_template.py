import os
import sys
from shutil import copyfile

from animations import animation_handler
from serve_html import serve_file
import webbrowser
import threading

flags = {}
CWD = os.path.dirname(os.path.realpath(__file__))
FILE_WRITER = None
INPUT_FILE = None
OUTPUT_FILE = None
THREADS = {}


def split_flag(flag):
    s = flag.split('=')
    if len(s) != 2:
        raise Exception("Not a valid flag - {}".format(flag))
    value = s[1]
    s = s[0].split('--')
    if len(s) != 2:
        raise Exception("Not a valid flag - {}".format(flag))
    key = s[1]
    return key, value


def run_in_a_thread(name, target_function, args):
    THREADS[name] = threading.Thread(target=target_function, name=name, args=args)
    THREADS[name].daemon = True
    THREADS[name].start()


def populate_flags_with_default():
    global flags
    flags['input_directory'] = 'templates'
    flags['input_name'] = 'basic'
    flags['output_name'] = 'multi_source_bfs'
    flags['output_directory'] = 'outputs'
    flags['delete_after_use'] = None


def convert_array_to_string(arr):
    out = ""
    for i in arr:
        if len(out) > 1:
            out += ","
        tmp = i.replace('\n', '\\\n')
        out += f"'{tmp}'"
    return out


def main():
    global flags
    global OUTPUT_FILE
    global INPUT_FILE
    global FILE_WRITER
    global THREADS

    copyfile(INPUT_FILE, OUTPUT_FILE)
    FILE_WRITER = open(OUTPUT_FILE, 'a+')
    data = convert_array_to_string(animation_handler.run_animation(flags['output_name']))
    print('data', data)
    FILE_WRITER.write(data)
    FILE_WRITER.write("\n] \n</script>")
    # Does not work, need to fix
    # webbrowser.open(f'localhost:8000/outputs/{flags["output_name"]}.html',new=0, autoraise=True)


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


if __name__ == '__main__':
    process_flags()
    main()
    try:
        pass
    except Exception as error:
        print(error)
        if os.path.isfile(OUTPUT_FILE):
            os.remove(OUTPUT_FILE)
    finally:
        if FILE_WRITER is not None:
            FILE_WRITER.close()
        if flags['delete_after_use']:
            if os.path.isfile(OUTPUT_FILE):
                os.remove(OUTPUT_FILE)
        else:
            if 'noserve' not in flags:
                serve_file('abc.txt')
