import http.server
import socketserver


def start_server():
    PORT = 8000

    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as webServer:
        print(f"Serving at port http://localhost:{PORT}/")
        try:
            webServer.serve_forever()            
        except KeyboardInterrupt:
            pass

        webServer.server_close()
        print("Server stopped.")


if __name__ == "__main__":
    print("Hello")
    start_server()
