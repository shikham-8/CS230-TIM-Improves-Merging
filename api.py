# info we need:
# owner of repo
# name of repo
# branch that we want to merge into
# name of branch that you are working on
# name of files/functions in question
import requests
import detect

# take all of the below information in config file
OWNER = "shikham-8"
REPOSITORY_NAME = "CS230-TIM-Improves-Merging"
BRANCH_TO_MERGE_TO = "main"
MY_BRANCH = "main"
# don't need these if copying files
# FUNCTION_TO_COMPARE_1 = "cut1"
# FUNCTION_TO_COMPARE_2 = "cut2"
global REFACTOR
REFACTOR = False


def getRefactoringChange() -> bool:
    return REFACTOR


def setRefactoringChange(ref: bool):
    globalVariables = globals()
    globalVariables["REFACTOR"] = ref


def getMostRecentMainCommit():
    url = f"https://api.github.com/repos/{OWNER}/{REPOSITORY_NAME}/commits/{BRANCH_TO_MERGE_TO}"
    user_data = requests.get(url).json()
    return user_data


def checkRefactoringCommit(commitObject):
    if ("refactor" in commitObject["message"].lower()):
        setRefactoringChange(True)
    else:
        setRefactoringChange(False)


def getMostRecentMyBranchCommit():
    url = f"https://api.github.com/repos/{OWNER}/{REPOSITORY_NAME}/commits/{MY_BRANCH}"
    user_data = requests.get(url).json()
    return user_data


def getFilesInCommit(commitSHA):
    url = f"https://api.github.com/repos/{OWNER}/{REPOSITORY_NAME}/commits/{commitSHA}"
    file_data = requests.get(url).json()
    listOfFiles = file_data["files"]
    return listOfFiles


def getCallableItems(files):
    filesAndFunctions = []
    for file in files:
        filename = file["filename"]
        filesAndFunctions.append(detect.iterateOverFile(filename))
    # print(filesAndFunctions)
    removeNones = list(filter(None, filesAndFunctions))
    flatList = [item for sublist in removeNones for item in sublist]
    # print(flatList)
    return flatList


# getCallableItems(getFilesInCommit(getMostRecentMainCommit()["sha"]))
