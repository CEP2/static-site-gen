import os, shutil
from pathlib import Path
from generatepage import generate_page

#copies
def copy_directory(target="static", destination="public"):
    home = Path.cwd()
    origin = os.path.join(home, target)
    dest = os.path.join(home, destination)

    if not os.path.exists(origin):
        raise ValueError(f"origin does not exist {origin}")
    #Clean out destination if exists
    if os.path.exists(dest):
        if os.path.isfile(dest):
            os.remove(dest)
        elif os.path.isdir(dest):
            shutil.rmtree(dest)
        else:
            raise ValueError(f"not a file or dir: {dest}")
    # remake destinatinon
    os.mkdir(dest)
    copy_contents(origin, dest)
    
#Take path, copy path to destination
def copy_contents(origin, dest):
    print(origin, dest, sep='\n')
    # open origin folder contents (list)  
    contents = os.listdir(origin)
    # iterate through folder contents
    for c in contents:
        c_path = os.path.join(origin,c)
        print(f"file check: {c_path}")
        if os.path.isfile(c_path):
            print(f"{c_path} is a file")
            #copy to destination
            shutil.copy(c_path, os.path.join(dest,c))
        # if directory
        elif os.path.isdir(c_path):
            # join dir to dest and origin
            new_origin = os.path.join(origin, os.path.basename(c))
            new_dest = os.path.join(dest, os.path.basename(c))
            # make new directory
            os.mkdir(new_dest)
            # call copy contents on content directory
            copy_contents(new_origin, new_dest)
        else:
            print(f"unable to copy: {c}")

    return

def main():
    origin = "content/index.md"
    dest = "public/index.html"
    template = "template.html"

    copy_directory()
    generate_page(origin,template,dest)


main()