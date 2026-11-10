import argparse
import os
import tornado.ioloop
import tornado.web

class HomeHandler(tornado.web.RequestHandler):
    HOME_PAGE = ""
    def get(self):
        self.set_header("Content-Type", "text/html; charset=utf-8")
        with open('index.html') as f:
            self.HOME_PAGE =f.read()
            self.write(self.HOME_PAGE)

        # self.write(HOME_PAGE)

    def head(self):
        self.set_header("Content-Type", "text/html; charset=utf-8")
        self.set_header("Content-Length", len(self.HOME_PAGE.encode("utf-8")))


def make_app(rooter: str, default_file: str | None = None):
    return tornado.web.Application([
        (r"/", HomeHandler),                              # home page (exact match)
        (r"/(.*)", tornado.web.StaticFileHandler, {       # everything else = static
            "path": rooter,
            "default_filename": default_file or "",
        }),
    ])


def main():
    parser = argparse.ArgumentParser(description="Simple Tornado static file server")
    parser.add_argument("--port", type=int, default=8585)
    parser.add_argument("--root", default=os.path.abspath("."))
    parser.add_argument("--index", default="index.html")
    args = parser.parse_args()

    make_app(args.root, args.index).listen(args.port)
    print(f"Home:    http://localhost:{args.port}/")
    print(f"Statics: {args.root} served at http://localhost:{args.port}/<file>")
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()