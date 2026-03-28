from printers import Printer

class HtmlPrinter(Printer):
    def print_page(self, page):
        print(f"<div style='single-page'>{page}</div>")
