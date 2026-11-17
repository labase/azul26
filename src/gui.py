""" Web GUI controller.

Classes neste módulo:
    - :py:class:`AzulGUI` handle browser DOM functions.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    26.11
   |br| Initial class implementation (04).
   |br| Working version with Bottle, Bulma & Brython (11).
   |br| Brython basics of game board (17).

|   **Open Source Notification:** This file is part of open source program **Azul**
|   **Copyright © 2026  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <https://is.gd/3Udt>`_.
|   `Labase <https://labase.github.io/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""
from browser import document, html  # type: ignore[PyUnresolvedReferences]

class PorLadrilhos:
    def __init__(self):
        ladrilhos = "column is-third is-flex is-flex-direction-column is-align-items-flex-end pr-5"
        ladrilhos_style = "border-right: 2px solid #ccc;"
        dentro = html.DIV(self.dentro(), Class="columns is-mobile")
        self.base = html.DIV(dentro, Class=ladrilhos, style=ladrilhos_style)

    def dentro(self):
        ass = "column is-third is-flex is-flex-direction-column-reverse is-align-items-flex-end pr-5"
        def ladrilhos():
            ld = html.DIV(Class="box p-0 m-1 has-background-white tile-slot")
            return html.DIV(ld, Class ="is-flex mb-2")
        def col(siz=5):
            # return html.DIV([ladrilhos() for _ in range(siz)], Class=ass) #, style=style)
            return html.DIV([ladrilhos() for _ in range(5-siz+1)], Class=ass) #, style=style)
        return [col(siz) for siz in range(5,0, -1)]
    def monta(self):
        return self.base


class AzulGUI:
    document = document
    html = html

    def monta(self):
        tabuleiro = self.document.body
        part = PorLadrilhos().monta()
        part2 = PorLadrilhos().monta()
        part3 = PorLadrilhos().monta()
        tabu_box = html.DIV([part, part2, part3], Class="columns is-mobile")#, style=style)
        tabu_box = html.DIV(tabu_box, Class="container", style="max-width: 850px;")
        tabuleiro <= tabu_box
        print("tabuleiro")


def azul(br):
    br().monta()

if __name__ == "__main__":
    azul(AzulGUI)

