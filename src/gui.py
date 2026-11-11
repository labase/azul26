from browser import document, html


class Bryt:
    document = document
    html = html
#
# def main(br):
#         tabuleiro = br.document.body
#         tabu_box = br.html.DIV(Class="box has-background-white-ter p-5", style="border: 4px solid #2c3e50;")
#         tabuleiro <= tabu_box


def azul(br):
    ''' <div id="ct" class="container" style="max-width: 850px;">

        <!-- Painel Geral (Moldura do Tabuleiro) -->
        <div class="box has-background-white-ter p-5" style="border: 4px solid #2c3e50;"></div>
    </div>
    '''
    tabuleiro = br.document.body
    tabu_box = br.html.DIV(Class="box has-background-white-ter p-5", style="border: 4px solid #2c3e50;")
    tabuleiro <= tabu_box
    print("tabuleiro")
    # bx = html.DIV(class="box has-background-white-ter p-5" style="border: 4px solid #2c3e50;")
    # bx = html.DIV()
    # document["ct"] <= bx

    # from gui import azul
    # import gui
    print("gui import main tabuleiro")
    # gui.azul(br)


azul(Bryt)

