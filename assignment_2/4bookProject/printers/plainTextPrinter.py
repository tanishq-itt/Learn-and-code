from printers import Printer

class PlainTextPrinter(Printer):
    def print_page(self, page):
        print(page)
