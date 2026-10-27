from bottle import Bottle, run
BODY = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Azul</title>
  <link  rel="stylesheet"  href="https://cdn.jsdelivr.net/npm/bulma@1.0.4/css/bulma.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/brython/3.15.0/brython.min.js" integrity="sha512-G0CChqkpHKCjVgLM0se6TLfQ0fqmoFqvr5XCONxzF2GoiQmStnd76lKmMLGo/g32mzP3qmIPalp4z+qICfAPYw==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/brython/3.15.0/brython_stdlib.min.js" integrity="sha512-vUqnWPo3+2xMHld57vH6JZjWcUEAofzKGs4egBxZdPMC+IPyRrwe3usgCdmV3jP1xaEENJnou/M0EnP5npDuig==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@1.0.2/css/bulma.min.css">
  <style>
    .bottle-svg { width: 120px; height: auto; }
        /* Único CSS customizado: garantir que os ladrilhos sejam quadrados perfeitos */
        .tile-slot {
            width: 40px;
            height: 40px;
            border-radius: 4px;
        }
        /* Fundo da mesa para contraste */
        body {
            background-color: #d8c3a5; 
            padding: 2rem;
        }

  </style>
</head>
<body>
<H1>"Jogo do Azul"</H1>
 <div class="container" style="max-width: 850px;">
        
        <!-- Painel Geral (Moldura do Tabuleiro) -->
        <div class="box has-background-white-ter p-5" style="border: 4px solid #2c3e50;"></div>
    </div>
</body>
</html>'''
class MyServer(object):
    def __init__(self):
        self.app = Bottle()
        self.init_routes()

    def init_routes(self):
        """Initialize all routes"""
        @self.app.route('/')
        def hello():
            return BODY

    def run(self):
        run(self.app, host='0.0.0.0', port=8080)
# Example usage
if __name__ == "__main__":
    server = MyServer()
    server.run()