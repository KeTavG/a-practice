import sys
import os
from time import perf_counter

INPUT_FILE_NAME = "C:\\Users\\ketav\\source\\a-practice\\a5-seqprocessing\\input.txt"
OUTPUT_FILE_NAME = "C:\\Users\\ketav\\source\\a-practice\\a5-seqprocessing\\output.txt"
A_FILE = "C:\\Users\\ketav\\source\\a-practice\\a5-seqprocessing\\a.txt"
B_FILE = "C:\\Users\\ketav\\source\\a-practice\\a5-seqprocessing\\b.txt"
C_FILE = "C:\\Users\\ketav\\source\\a-practice\\a5-seqprocessing\\c.txt"
SPACE_SYMBOL = ' '

class SeqProcessingCore:
    @staticmethod
    def externalMergeSort(inputFile=INPUT_FILE_NAME, outputFile=OUTPUT_FILE_NAME):
        def copyFile(fromFile, toFile):
            r = open(fromFile, "r")
            w = open(toFile, "w")
            w.write(r.read())
            r.close()
            w.close()

        def splitSeq(srcSeq, bSeq=B_FILE, cSeq=C_FILE):
            seqLength = os.path.getsize(srcSeq)
            currIndex = 0
            (lastB, lastC) = (0, 0)
            (switchFlag, counter) = (True, 0) # (True - b | False - c, writed number counter)
            srcFile = open(srcSeq, "r")
            bFile = open(bSeq, "w")
            cFile = open(cSeq, "w")
            while currIndex < seqLength:
                currItem = srcFile.read(1)
                currIndex += 1
                currNumberStr = currItem
                while currItem != SPACE_SYMBOL and currIndex < seqLength:
                    currItem = srcFile.read(1)
                    currIndex += 1
                    currNumberStr += currItem
                currNumber = int(currNumberStr)
                if not counter:
                    bFile.write(str(currNumber) + ' ')
                    counter += 1
                    lastB = currNumber
                else:
                    if switchFlag:
                        if lastB <= currNumber:
                            bFile.write(str(currNumber) + ' ')
                            counter += 1
                            lastB = currNumber
                        else:
                            switchFlag = not switchFlag
                            cFile.write(str(currNumber) + ' ')
                            counter += 1
                            lastC = currNumber
                    else:
                        if lastC <= currNumber:
                            cFile.write(str(currNumber) + ' ')
                            counter += 1
                            lastC = currNumber
                        else:
                            switchFlag = not switchFlag
                            bFile.write(str(currNumber) + ' ')
                            counter += 1
                            lastB = currNumber
            srcFile.close()
            bFile.close()
            cFile.close()

        def mergeSeq(srcSeq, bSeq=B_FILE, cSeq=C_FILE):
            bLength = os.path.getsize(bSeq)
            cLength = os.path.getsize(cSeq)
            currBIndex = 0
            currCIndex = 0
            currBNumber = 0
            currCNumber = 0
            (lastB, lastC) = (0, 0)
            (switchFlag, counter) = (True, 0) # (True - b | False - c, writed number counter)
            newBSeqFlag = False
            newCSeqFlag = False
            amountSeq = 1
            srcFile = open(srcSeq, "w")
            bFile = open(bSeq, "r")
            cFile = open(cSeq, "r")
            while currBIndex < bLength and currCIndex < cLength:
                if (switchFlag or not counter) and not newBSeqFlag:
                    currBItem = bFile.read(1)
                    currBIndex += 1
                    currBNumberStr = currBItem
                    while currBItem != SPACE_SYMBOL and currBIndex < bLength:
                        currBItem = bFile.read(1)
                        currBIndex += 1
                        currBNumberStr += currBItem
                    currBNumber = int(currBNumberStr)
                    if not counter:
                        lastB = currBNumber
                if (not switchFlag or not counter) and not newCSeqFlag:
                    currCItem = cFile.read(1)
                    currCIndex += 1
                    currCNumberStr = currCItem
                    while currCItem != SPACE_SYMBOL and currCIndex < cLength:
                        currCItem = cFile.read(1)
                        currCIndex += 1
                        currCNumberStr += currCItem
                    currCNumber = int(currCNumberStr)
                    if not counter:
                        lastC = currCNumber
                if lastC > currCNumber and not newCSeqFlag:
                    amountSeq += 1
                    newCSeqFlag = True
                    while lastB <= currBNumber:
                        srcFile.write(str(currBNumber) + ' ')
                        counter += 1
                        lastB = currBNumber
                        currBItem = bFile.read(1)
                        currBIndex += 1
                        currBNumberStr = currBItem
                        while currBItem != SPACE_SYMBOL and currBIndex < bLength:
                            currBItem = bFile.read(1)
                            currBIndex += 1
                            currBNumberStr += currBItem
                        currBNumber = int(currBNumberStr)
                    newBSeqFlag = True
                elif lastB > currBNumber and not newBSeqFlag:
                    amountSeq += 1
                    newBSeqFlag = True
                    while lastC <= currCNumber:
                        srcFile.write(str(currCNumber) + ' ')
                        counter += 1
                        lastC = currCNumber
                        currCItem = cFile.read(1)
                        currCIndex += 1
                        currCNumberStr = currCItem
                        while currCItem != SPACE_SYMBOL and currCIndex < cLength:
                            currCItem = cFile.read(1)
                            currCIndex += 1
                            currCNumberStr += currCItem
                        currCNumber = int(currCNumberStr)
                    newCSeqFlag = True
                else:
                    if currBNumber <= currCNumber:
                        switchFlag = True
                        newBSeqFlag = False
                        srcFile.write(str(currBNumber) + ' ')
                        counter += 1
                        lastB = currBNumber
                    else:
                        switchFlag = False
                        newCSeqFlag = False
                        srcFile.write(str(currCNumber) + ' ')
                        counter += 1
                        lastC = currCNumber
            if currCIndex == cLength:
                if switchFlag:
                    endCSeq = False
                    while currBIndex < bLength:
                        if switchFlag:
                            currBItem = bFile.read(1)
                            currBIndex += 1
                            currBNumberStr = currBItem
                            while currBItem != SPACE_SYMBOL and currBIndex < bLength:
                                currBItem = bFile.read(1)
                                currBIndex += 1
                                currBNumberStr += currBItem
                            currBNumber = int(currBNumberStr)
                        if currBNumber <= currCNumber:
                            switchFlag = True
                            srcFile.write(str(currBNumber) + ' ')
                            if lastB > currBNumber:
                                amountSeq += 1
                            lastB = currBNumber
                        else:
                            switchFlag = False
                            srcFile.write(str(currCNumber) + ' ')
                            endCSeq = True
                            break
                    if not endCSeq:
                        srcFile.write(str(currCNumber) + ' ')
                    else:
                        srcFile.write(str(currBNumber) + ' ')
                        if lastB > currBNumber:
                                amountSeq += 1
                        lastB = currBNumber
                        while currBIndex < bLength:
                            currBItem = bFile.read(1)
                            currBIndex += 1
                            currBNumberStr = currBItem
                            while currBItem != SPACE_SYMBOL and currBIndex < bLength:
                                currBItem = bFile.read(1)
                                currBIndex += 1
                                currBNumberStr += currBItem
                            currBNumber = int(currBNumberStr)
                            srcFile.write(str(currBNumber) + ' ')
                            if lastB > currBNumber:
                                amountSeq += 1
                            lastB = currBNumber
                else:
                    srcFile.write(str(currBNumber) + ' ')
                    if lastB > currBNumber:
                            amountSeq += 1
                    lastB = currBNumber
                    while currBIndex < bLength:
                        currBItem = bFile.read(1)
                        currBIndex += 1
                        currBNumberStr = currBItem
                        while currBItem != SPACE_SYMBOL and currBIndex < bLength:
                            currBItem = bFile.read(1)
                            currBIndex += 1
                            currBNumberStr += currBItem
                        currBNumber = int(currBNumberStr)
                        srcFile.write(str(currBNumber) + ' ')
                        if lastB > currBNumber:
                            amountSeq += 1
                        lastB = currBNumber
            elif currBIndex == bLength:
                if not switchFlag:
                    endBSeq = False
                    while currCIndex < cLength:
                        if not switchFlag:
                            currCItem = cFile.read(1)
                            currCIndex += 1
                            currCNumberStr = currCItem
                            while currCItem != SPACE_SYMBOL and currCIndex < cLength:
                                currCItem = cFile.read(1)
                                currCIndex += 1
                                currCNumberStr += currCItem
                            currCNumber = int(currCNumberStr)
                        if currBNumber <= currCNumber:
                            switchFlag = True
                            srcFile.write(str(currBNumber) + ' ')
                            endBSeq = True
                            break
                        else:
                            switchFlag = False
                            srcFile.write(str(currCNumber) + ' ')
                            if lastC > currCNumber:
                                amountSeq += 1
                    if not endBSeq:
                        srcFile.write(str(currBNumber) + ' ')
                    else:
                        srcFile.write(str(currCNumber) + ' ')
                        if lastC > currCNumber:
                                amountSeq += 1
                        lastC = currCNumber
                        while currCIndex < cLength:
                            currCItem = cFile.read(1)
                            currCIndex += 1
                            currCNumberStr = currCItem
                            while currCItem != SPACE_SYMBOL and currCIndex < cLength:
                                currCItem = cFile.read(1)
                                currCIndex += 1
                                currCNumberStr += currCItem
                            currCNumber = int(currCNumberStr)
                            srcFile.write(str(currCNumber) + ' ')
                            if lastC > currCNumber:
                                amountSeq += 1
                            lastC = currCNumber
                else:
                    srcFile.write(str(currCNumber) + ' ')
                    if lastC > currCNumber:
                            amountSeq += 1
                    lastC = currCNumber
                    while currCIndex < cLength:
                        currCItem = cFile.read(1)
                        currCIndex += 1
                        currCNumberStr = currCItem
                        while currCItem != SPACE_SYMBOL and currCIndex < cLength:
                            currCItem = cFile.read(1)
                            currCIndex += 1
                            currCNumberStr += currCItem
                        currCNumber = int(currCNumberStr)
                        srcFile.write(str(currCNumber) + ' ')
                        if lastC > currCNumber:
                            amountSeq += 1
                        lastC = currCNumber
            return amountSeq

        srcSeq = A_FILE
        copyFile(inputFile, srcSeq)
        amountSeq = 0 
        while amountSeq != 1:
            splitSeq(srcSeq)
            amountSeq = mergeSeq(srcSeq)
        copyFile(srcSeq, outputFile)

if __name__ == "__main__":
    startTime = perf_counter()
    try:
        SeqProcessingCore.externalMergeSort()
    except:
        print("INVALID INPUT")
    else:
        runTime = perf_counter() - startTime
        print("Run time = {} sec.".format(runTime))
