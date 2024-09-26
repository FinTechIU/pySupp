import os, pwd

print("Hello World, " + pwd.getpwuid(os.getuid())[0].title() + "!");
