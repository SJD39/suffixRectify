import os

def getFilePaths(folder):
    filePaths = []

    for filePath, dirnames, fileNames in os.walk(folder):
        for fileName in fileNames:
                filePaths.append(filePath + "\\" + fileName)

    return filePaths