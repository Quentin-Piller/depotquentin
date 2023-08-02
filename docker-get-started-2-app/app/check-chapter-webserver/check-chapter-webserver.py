from http.server import HTTPServer, BaseHTTPRequestHandler
import requests

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = "http://www.volonte-d.com/"
        response = requests.get(url)

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        if "Oda" in response.text:
            result_message = "La chaîne 'Oda' est présente sur la page."
        else:
            result_message = "La chaîne 'Oda' n'est pas présente sur la page."

        # Construire la réponse HTML avec le résultat du script
        html_response = f"""
        <html>
            <head>
                <title>Résultat du script Python</title>
            </head>
            <body>
                <h1>Résultat du script Python</h1>
                <p>{result_message}</p>
            </body>
        </html>
        """

        # Envoyer la réponse HTTP avec le contenu HTML
        self.wfile.write(html_response.encode('utf-8'))

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print('Serveur HTTP démarré sur le port 8000...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()