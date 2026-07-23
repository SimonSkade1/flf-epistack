#!/usr/bin/env python3
"""Serve a built Quartz `public/` dir with Quartz-style clean-URL routing.

Quartz emits `<slug>.html` files but links to extensionless `<slug>`. A plain
static server 404s those. This server tries `<path>`, then `<path>.html`, then
`<path>/index.html`, matching how the notes link to each other — so the model
viewer's node/edge clicks open real note pages.

Usage: python3 scripts/serve_public.py [port] [--root public]
"""
import functools
import http.server
import os
import posixpath
import socketserver
import sys
import urllib.parse


class Handler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # strip query/fragment, normalise
        path = path.split("?", 1)[0].split("#", 1)[0]
        path = urllib.parse.unquote(path)
        clean = posixpath.normpath(path).lstrip("/")
        full = os.path.join(self.directory, clean)
        if os.path.isdir(full):
            idx = os.path.join(full, "index.html")
            return idx if os.path.exists(idx) else full
        if os.path.exists(full):
            return full
        # clean URL: try appending .html
        if os.path.exists(full + ".html"):
            return full + ".html"
        return full  # let it 404

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        pass  # quiet


def main():
    port = 8080
    root = "public"
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--root":
            root = args[i + 1]
            i += 2
        else:
            port = int(args[i])
            i += 1
    root = os.path.abspath(root)
    handler = functools.partial(Handler, directory=root)
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("127.0.0.1", port), handler) as httpd:
        print(f"serving {root} at http://localhost:{port}/  (model: /static/model/)")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
