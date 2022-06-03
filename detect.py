import os
import imp


def iterateOverFile(filename):
    fileFunctionList = []
    if filename.endswith(".py"):
        modulename = filename[:-3]
        # print(modulename)
        # print(directory+os.sep+modulename)
        foo = imp.load_source('module', filename)
        for name, val in foo.__dict__.items():  # iterate through every module's attributes
            if callable(val):                      # check if callable (normally functions)
                # print(val)                              # call it
                crosshairString = modulename + "." + name
                fileFunctionList.append(crosshairString)
        return fileFunctionList  # return list of file.function strings for crosshair to use
