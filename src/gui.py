""" Web GUI controller.

Classes neste módulo:
    - :py:class:`AzulGUI` handle browser DOM functions.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    26.11
   |br| Initial class implementation (04).
   |br| Working version with Bottle, Bulma & Brython (11).

|   **Open Source Notification:** This file is part of open source program **Azul**
|   **Copyright © 2026  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <https://is.gd/3Udt>`_.
|   `Labase <https://labase.github.io/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""
from browser import document, html


class AzulGUI:
    document = document
    html = html

def azul(br):
    tabuleiro = br.document.body
    tabu_box = br.html.DIV(Class="box has-background-white-ter p-5", style="border: 4px solid #2c3e50;")
    tabuleiro <= tabu_box
    print("tabuleiro")

if __name__ == "__main__":
    azul(AzulGUI)

