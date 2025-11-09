import os


def get_files_info(working_directory, directory="."):
    fullpath = os.path.join(working_directory, directory)
    abspath = os.path.abspath(fullpath)

    # check if abs path to directory is outside working_directory
    if directory not in os.listdir(working_directory) and directory != ".":
        return (f'  Error: Cannot list "{directory}" as it is outside the permitted working directory.')

    # check if working_directory is a directory
    if os.path.isdir(os.path.abspath(fullpath)) is not True:
        return f"  Error: {directory} is not a directory"

    try:
        contents_list = []
        for item in os.listdir(abspath):
            path = os.path.join(fullpath, item)
            itempath = os.path.abspath(path)
            filesize = os.path.getsize(itempath)
            isDir = False
            if os.path.isdir(itempath):
                isDir = True

            contents_list.append(f" - {item}: file_size={
                                 filesize} bytes, is_dir={isDir}")

        return "\n".join(contents_list)
    except Exception as e:
        return f"  Error: {e}"
