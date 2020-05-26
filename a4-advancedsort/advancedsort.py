import sys
import random
from time import perf_counter
from ui_form import Ui_Form
from PySide2.QtWidgets import QApplication, QWidget, QMessageBox
from PySide2.QtCore import Slot

class AdvancedSort(QWidget):
    def __init__(self):
        super(AdvancedSort, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.sortButton.clicked.connect(self.sortArray)

    @Slot()
    def sortArray(self):
        def toArray(inputStr): return [int(item) for item in inputStr.split()]

        def toOutputFormat(arrInfo):
            arr = arrInfo[0]
            time = arrInfo[1]
            return (''.join([str(item) + ' ' for item in arr]) + " (run time = {} sec.)".format(time))

        try:
            arr = toArray(self.ui.inputArray.text())
            assert arr
        except:
            msg = QMessageBox()
            msg.setText("INVALID INPUT")
            msg.exec()
        else:
            self.ui.sortedArrayCocktail.setText(toOutputFormat(AdvancedSortCore.cocktailSortWithInfo(arr)))
            self.ui.sortedArrayQuick.setText(toOutputFormat(AdvancedSortCore.qSortWithInfo(arr)))

class AdvancedSortCore:
    @staticmethod
    def cocktailSort(arr):
        leftIndex = 0
        rightIndex = len(arr) - 1
        startTime = perf_counter()
        while leftIndex <= rightIndex:
            for i in range(leftIndex, rightIndex):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            rightIndex -= 1
            for i in range(rightIndex, leftIndex, -1):
                if arr[i - 1] > arr[i]:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
            leftIndex += 1
        runTime = perf_counter() - startTime
        return arr

    @staticmethod
    def qSort(arr):
        if arr: return (AdvancedSortCore.qSort([x for x in arr if x<arr[0]]) + [x for x in arr if x==arr[0]] 
                        + AdvancedSortCore.qSort([x for x in arr if x>arr[0]]))
        return []

    @staticmethod
    def cocktailSortWithInfo(arr):
        startTime = perf_counter()
        arr = AdvancedSortCore.cocktailSort(arr)
        runTime = perf_counter() - startTime
        return (arr, runTime)

    @staticmethod
    def qSortWithInfo(arr):
        startTime = perf_counter()
        arr = AdvancedSortCore.qSort(arr)
        runTime = perf_counter() - startTime
        return (arr, runTime)

if __name__ == "__main__":
    app = QApplication([])
    window = AdvancedSort()
    window.show()
    sys.exit(app.exec_())
