import os
import sys

walk_dir = "/home/prog/tmp" #sys.argv[1]

print('walk_dir = ' + walk_dir)
print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

# print(os.walk(walk_dir))
# print(list(os.walk(walk_dir)))

all_dirs = list(os.walk(walk_dir))

for root, subdirs, files in all_dirs:
    print('root: ' + root)
    print("subdirs: " + str(subdirs))
    print("files: " + str(files))

    for filename in files:
        file_path = os.path.join(root, filename)
        print("%s : %i" % (file_path, os.path.getsize(file_path)))

