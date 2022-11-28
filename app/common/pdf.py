from PyQt5 import QtPrintSupport, QtGui


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
    # painter.translate(printer.paperRect().center())
    painter.scale(scale, scale)
    # painter.translate(-widget.width() / 2, -widget.height() / 2)
    # end scale

    widget.render(painter)
    painter.end()