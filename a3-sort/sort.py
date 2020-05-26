import sys
from time import perf_counter
from ui_form import Ui_Form
from PySide2.QtWidgets import QApplication, QWidget, QMessageBox
from PySide2.QtCore import Slot

class Sort(QWidget):
    def __init__(self):
        super(Sort, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.sortButton.clicked.connect(self.sortArray)

    @Slot()
    def sortArray(self):
        def toArray(inputStr): return [int(item) for item in inputStr.split()]

        def toOutputFormat(arrInfo):
            arr = arrInfo[0]
            comparisons = arrInfo[1]
            changes = arrInfo[2]
            time = arrInfo[3]
            return (''.join([str(item) + ' ' for item in arr]) + 
                    " (number of changes = {}; number of comparisons = {}; run time = {} sec.)".format(comparisons,
                                                                                                       changes, time))

        try:
            arr = toArray(self.ui.inputArray.text())
            assert arr
        except:
            msg = QMessageBox()
            msg.setText("INVALID INPUT")
            msg.exec()
        else:
            self.ui.sortedArrayInsert.setText(toOutputFormat(SortCore.insertSort(arr)))
            self.ui.sortedArraySelect.setText(toOutputFormat(SortCore.selectSort(arr)))

class SortCore:
    @staticmethod
    def insertSort(arr):
        comparisonsNumber = 0
        changesNumber = 0
        startTime = perf_counter()
        for rightIndex, rightItem in enumerate(arr[1:], 1):
            for leftIndex, leftItem in enumerate(arr[0:rightIndex]):
                comparisonsNumber += 1
                if leftItem > rightItem:
                    changesNumber += 1
                    arr.insert(leftIndex, arr.pop(rightIndex))
                    break
        runTime = perf_counter() - startTime
        return (arr, changesNumber, comparisonsNumber, runTime)

    @staticmethod
    def selectSort(arr):
        comparisonsNumber = 0
        changesNumber = 0
        startTime = perf_counter()
        for leftIndex, leftItem in enumerate(arr):
            minItem = (leftIndex, leftItem)
            for rightIndex, rightItem in enumerate(arr[leftIndex+1:]):
                comparisonsNumber += 1
                if rightItem < minItem[1]:
                    minItem = (rightIndex, rightItem)
            changesNumber += 1
            arr.insert(leftIndex, arr.pop(minItem[0]))
        runTime = perf_counter() - startTime
        return (arr, changesNumber, comparisonsNumber, runTime)

if __name__ == "__main__":
    app = QApplication([])
    window = Sort()
    window.show()
    sys.exit(app.exec_())
