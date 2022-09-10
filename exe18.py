# like scripts with argv
def like_script_argv(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# Getting only two arguments
def two_arg(arg1,arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# getting only one arguments
def only_one(arg1):
    print(f"arg1: {arg1}")

# With no arguments
def no_arg():
    print("In this function there is no argument")

like_script_argv("shri","Ram")
two_arg("RAM","SHIV")
only_one("SHRI RAM")
no_arg()

print("****this is end of user define function.****")
