import os

label_dirs = ['datasets/Wildfire_Smoke/train/labels',
              'datasets/Wildfire_Smoke/valid/labels']

original_tag = '0'
new_tag = '11'
for directory in label_dirs:
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            with open(f, "r") as fid:
                d = fid.readlines()
                newlines = []
                for line in d:
                    newlines.append(line.replace(original_tag, new_tag, 1))

            with open(f, 'w') as f:
                for line in newlines:
                    f.write(line)


