import sys

def removeDuplicates(sampleList):
  # remove any word that appears more than once
  setList = set(sampleList)
  returnList = list(setList)
  return returnList

def uniqueLetters(wordList):
  # remove any word that does not have unique letters
  listOfWords = []
  for word in wordList:
    lowerWord = word.lower()
    setWord = set(lowerWord)
    if len(setWord) == len(word):
      listOfWords.append(word)
  return listOfWords

def addedTxt(userInput):
  #adding .txt to user input when saving file
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
for index, word in enumerate(newFile):
  textList.append(word)

# asking user what they want to do with the file
while True:
  operationInput = input("What do you want to do with the file? Below are the options. Please input a number.\n 1. Remove duplicates\n 2. Words with unique letters\n 3. Do nothing\n")
  try:
    if operationInput == "1":
      modifiedList = removeDuplicates(textList) 
      break
    elif operationInput == "2":
      modifiedList = uniqueLetters(textList)
      break
    elif operationInput == "3":
      print("Nothing happened")
      importFile.close()
      sys.exit(1) 
    else:
      print("Please review the options and try again")
  except:
    print("System error. Please try again")
    sys.exit(1)

# saving the output into a new textfile
saveInput = input("What name do you want to save your file as?\n")
fixedSavedFile = addedTxt(saveInput)
try:
  with open(fixedSavedFile, "w") as resultFile:
    resultFile.write('\n'.join(modifiedList))
except:
  print("Import failed. Please try again.")
  sys.exit(1)
importFile.close()