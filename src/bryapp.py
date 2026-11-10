
from browser import document, html

class Board:
    def __init__(self, document, html):
        self.d = document
        self.h = html

    def go(self):
        d, h = self.d, self.h
        bx = h.DIV(Class="box has-background-white-ter p-5", style="border: 4px solid #2c3e50;")
        ct = h.DIV(bx, Class="container", style="max-width: 850px;")
        prd = d["brd"]
        _ = prd <= ct
        print("go = Board(document, html)")


def app(document, html):
    board = Board(document, html)
    board.go()
    print("board = Board(document, html)")


if __name__ == "__main__":
    app(document, html)