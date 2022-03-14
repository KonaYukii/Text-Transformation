import sys

def removeDuplicates(sampleList):
  # remove any word that appears more than once
  setList = set(sampleList)
  returnList = list(setList)
  return returnList

def addedTxt(userInput):
  if userInput == '':
    userInput = 'result'
  fixedInput = userInput.split(".")
  finalFix = fixedInput[0] + ".txt"
  return finalFix

# obtain information from the textfile
textList = []
userInput = input("Which file do you want to open?\n")
try:
  importFile = open(userInput, 'r')
except:
  print("Import failed. Please try again.")
  sys.exit(1)
newFile = importFile.read().splitlines()
# loop through the words 
for index, word in enumerate(newFile):
  textList.append(word)

result = removeDuplicates(textList)
# save the result into another text file
userSave = input("What name do you want to save your file as?\n")
fixedSavedFile = addedTxt(userSave)
try:
  with open(fixedSavedFile, "w") as resultFile:
    resultFile.write('\n'.join(result))
except:
  print("Import failed. Please try again.")
  sys.exit(1)
importFile.close()