import os


def fileAction(filename,text,par):
    with open(filename, par) as f:
        if par != 'r':
            f.write(text)
        else:
            print(f.read())
def scanDir(path):
    dir_list = os.listdir(path)
    for item in dir_list:
        print ("item: %s" % item)

        root, ext = os.path.splitext(item)
        if not ext:
            ext = '(directory)'
            item = item + ext

    print(dir_list)

    return dir_list
