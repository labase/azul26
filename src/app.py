from bottle import Bottle, run, static_file
BODY = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Azul</title>
  <link  rel="stylesheet"  href="https://cdn.jsdelivr.net/npm/bulma@1.0.4/css/bulma.min.css">
  <script src="/libbr/brython.js"> </script>
  <script src="/libbr/brython_stdlib.js"> </script>
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
<brython-options debug="1" pythonpath="/"></brython-options>
<script type="text/python" src="gui.py">
</script>
</body>

</html>'''
class MyServer(object):
    def __init__(self):
        self.HOME_PAGE = BODY
        self.app = Bottle()
        self.init_routes()

    def init_routes(self):
        """Initialize all routes"""
        @self.app.route('/')
        def hello():
            return BODY

        @self.app.route('/gui.py')
        def send_static():
            print("filename gui")
            return static_file("gui.py", root=".", mimetype="text/python")
    def run(self):
        run(self.app, host='0.0.0.0', port=8080)
# Example usage
if __name__ == "__main__":
    server = MyServer()
    server.init_routes()
    server.run()