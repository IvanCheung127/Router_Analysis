import tkinter.filedialog
import re


config_file = tkinter.filedialog.askopenfilename()
with open (config_file,'rt',encoding='utf-8') as default_file:
    split_config = re.split(r'\<\S+\>',default_file.read())
    print(split_config)
