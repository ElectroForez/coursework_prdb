from PyQt5 import QtPrintSupport, QtGui
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtPrintSupport import QPrinter


class CapchaDialogController(QObject):
    def __init__(self, view, model):
        super().__init__()

        self._model = model
        self._view = view

    @pyqtSlot()
    def reload_capcha(self):
        capcha = self._model.generate_capcha()
        self._model.capcha = capcha

    @pyqtSlot(str)
    def check_capcha(self, value):
        if self._model.capcha != value:
            self._view.show_error()
            self._view._parent.on_block_auth()
        else:
            self._view._parent.on_good_capcha()
        self._view.close()

    @pyqtSlot()
    def download_capcha(self):
        # printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.PrinterResolution)
        # printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
        # printer.setPaperSize(QtPrintSupport.QPrinter.A4)
        # printer.setOrientation(QtPrintSupport.QPrinter.Portrait)
        # printer.setOutputFileName('output.pdf')
        #
        # doc = QtGui.QTextDocument()
        # doc.print_(printer)

        # printer = QPrinter(QPrinter.HighResolution)
        # printer.setOutputFormat(QPrinter.PdfFormat)
        # printer.setOutputFileName('output.pdf')
        # self._view._ui.capcha_label.document().print_(printer)
        print_widget(self._view._ui.capcha_label, 'output.pdf')
        pass

def print_widget(widget, filename):
    printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
    printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
    printer.setOrientation(QtPrintSupport.QPrinter.Portrait)
    printer.setOutputFileName(filename)
    painter = QtGui.QPainter(printer)

    # start scale
    xscale = printer.pageRect().width() * 1.0 / widget.width()
    yscale = printer.pageRect().height() * 1.0 / widget.height()
    scale = min(xscale, yscale)
    painter.translate(printer.paperRect().center())
    painter.scale(scale, scale)
    painter.translate(-widget.width() / 2, -widget.height() / 2)
    # end scale

    widget.render(painter)
    painter.end()