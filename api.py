# info we need:
# owner of repo
# name of repo
# branch that we want to merge into
# name of branch that you are working on
# name of files/functions in question
import requests
import base64

# take all of the below information in config file
OWNER = "shikham-8"
REPOSITORY_NAME = "CS230-TIM-Improves-Merging"
BRANCH_TO_MERGE_TO = "main"
MY_BRANCH = "main"
# don't need these if copying files
# FUNCTION_TO_COMPARE_1 = "cut1"
# FUNCTION_TO_COMPARE_2 = "cut2"
REFACTOR = True

url = f"https://api.github.com/repos/{OWNER}/{REPOSITORY_NAME}/contents/diffbehavior/a.py?cover"
user_data = requests.get(url).json()

# decode file contents
decoded_content = base64.b64decode(user_data["content"])
# format into python file

# strategy -
# copy contents of file to temp directory
# copy file from second branch to temp directory
# run diffbehavior / cover on those files/functions } this might need to be shell script
# output --> notify
print(decoded_content)
