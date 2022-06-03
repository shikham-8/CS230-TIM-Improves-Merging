# file to parse all files and callables --> bash script to run crosshair

import time
import generated_tests as gt
import os
import stat
import api
import shutil
import subprocess


def parseMyBranch():
    mainCommit = api.getMostRecentMyBranchCommit()
    mainCommitFiles = api.getFilesInCommit(mainCommit["sha"])
    # list of module.functions for main branch
    mainCommitFilesAndFunctions = api.getCallableItems(mainCommitFiles)

    return mainCommitFilesAndFunctions


def createTestFile():
    os.mkdir("tmp")
    # os.chdir("tmp")
    os.open("tmp/crosshair.sh", os.O_APPEND | os.O_CREAT | os.O_RDWR)


def createInitFile(filepathArray):
    dirFilePath = '/'.join(filepathArray[:-1])
    moduleName = filepathArray[-1]
    if "__init__.py" not in os.listdir(dirFilePath):
        # makes this module accessible for tests
        f = open(dirFilePath + "/__init__.py", "a")


def buildImportStatement(filepathArray):
    buildString = "from "
    filepathModule = ".".join(filepathArray[:-1])
    buildString += filepathModule
    # filename without .py extension
    moduleName = filepathArray[-1].split(".")

    buildString += "." + moduleName[0]
    buildString += " import * \n"
    return buildString


def writeTestFile(functionFileList):
    if "tmp" in os.listdir("."):
        shutil.rmtree("tmp")
    os.mkdir("tmp")
    # os.chdir("tmp")
    f = open("tmp/crosshair.sh", "a")
    g = open("tmp/crosshair-results.out", "a")
    if "generated_tests.py" in os.listdir("."):
        os.remove("generated_tests.py")
    h = open("generated_tests.py", "a")
    os.chmod("tmp/crosshair.sh", stat.S_IREAD | stat.S_IEXEC | stat.S_IWRITE)
    f.write("#!/bin/bash\n")
    print(functionFileList)
    for item in functionFileList:  # list of strings in format path/to/filename.functionName
        # print(item)
        splitFilepath = item.split('/')
        createInitFile(splitFilepath)
        importString = buildImportStatement(splitFilepath)
        h.write(importString)
        print("split path: ", splitFilepath)
        for pathPart in splitFilepath[:-1]:
            f.write("cd " + pathPart + "\n")
        f.write("crosshair cover " +
                splitFilepath[-1] + " > " + os.getcwd() + "/tmp/crosshair-results.out \n")

        f.write("cd " + os.getcwd() + "\n")
        # f.close()
        # g.close()
        # h.close()


def runCrosshair():
    f = open("tmp/crosshair.sh", "r")
    g = open("tmp/crosshair-results.out", "w")
    subprocess.call("tmp/crosshair.sh")
    # shutil.copy("tmp/crosshair-results.out", "generated_tests.py")
    f.close()
    g.close()
    g = open("tmp/crosshair-results.out", "r")
    h = open("generated_tests.py", "a")
    # h.write("def tests()")
    for line in g.readlines():
        h.write("print(" + line + ")\n")
    h.write("print('done')")
    g.close()
    h.close()


def shellScriptExecute():
    if "execute.sh" in os.listdir("."):
        os.remove("execute.sh")
    f = open("execute.sh", "a")
    os.chmod("execute.sh", stat.S_IREAD | stat.S_IEXEC | stat.S_IWRITE)
    f.write("#!/bin/bash\n")
    f.write("python3 generated_tests.py > output.txt")
    # f.close()


writeTestFile(parseMyBranch())
runCrosshair()
# shellScriptExecute()
# time.sleep(1)
# subprocess.call("./execute.sh")

# cleanup()
