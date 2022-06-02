import os, imp
directory = 'examples'

for filename in os.listdir(directory):
    if filename.endswith(".py"):
        modulename = filename[:-3]
        print(modulename)
        print(directory+os.sep+modulename)
        foo = imp.load_source('module', directory+os.sep+filename)
        for name, val in foo.__dict__.iteritems(): # iterate through every module's attributes
            if callable(val):                      # check if callable (normally functions)
                print(val)                              # call it
    else:
        continue