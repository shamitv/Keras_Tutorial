from os.path import dirname
print(__file__)

script_path=__file__

script_dir=dirname(script_path)

print(script_dir)

current_folder = globals()

print(current_folder)