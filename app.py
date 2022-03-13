def removeDuplicates(sampleList):
  # remove any word that appears more than once
  setList = set(sampleList)
  returnList = list(setList)
  return returnList

# obtain information from the textfile
textList = []

importFile = open('test.txt', 'r')
newFile = importFile.read().splitlines()
# loop through the words 
for index, word in enumerate(newFile):
  textList.append(word)

result = removeDuplicates(textList)
# save the result into another text file
with open("result.txt", "w") as resultFile:
  resultFile.write('\n'.join(result))
importFile.close()