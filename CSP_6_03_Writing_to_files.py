import random

#You need to create your own test file for this assignment.
#Because we are dealing with both reading and writing to files. Your test file will be more complicated than it has been.

def writeFile(inputList, fileName):
    with open(fileName, 'w') as file:
        for item in inputList:
            file.write(str(item) + '\n')
    return "oogabooga.txt"
def sortNames(fileName, targetFile):
    #Modify the below function such that it takes in source file and a target file.
    #Sort all of the values from the source file and write them to the target file
    #I recommend using .sort() for this. You do not need to write the sorting algorithm yourself.
    with open(fileName, 'r') as src:
        lines = src.readlines()

        # Remove whitespace/newlines
    lines = [line.strip() for line in lines]

    # Sort the values
    lines.sort()

    # Write sorted values to the target file
    with open(targetFile, 'w') as tgt:
        for line in lines:
            tgt.write(line + '\n')
    return "namesNew.txt"

sortNames("names.txt","namesNew.txt")



def highScore(newScore: int):

    with open("scores.txt", "a") as file:
        file.write(str(newScore) + "\n")
    with open("scores.txt", "r") as file:
        scores = file.readlines()
    scores = [int(score.strip()) for score in scores]
    return sum(scores) / len(scores)
highScore(random.randint(1,100))

