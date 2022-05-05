from http.server import HTTPServer, BaseHTTPRequestHandler

class serverHTTP(BaseHTTPRequestHandler):
  def do_GET(self):
      if self.path == '/':
            self.path = '/teste.html'
      try:
            verifArquivo = open(self.path[1:]).read()
            self.send_response(200)
      except:
            verifArquivo = "[404] Arquivo não encontrado"
            self.send_responde(404)
        
      self.end_headers()
      self.wfile.write(bytes(verifArquivo, "utf-8 pt-br"))

server = HTTPServer(('', 8000), serverHTTP)

def main():
      PORT = 8000 
      serv = HTTPServer(('', PORT), serverHTTP)

print ('[INFO] Servidor ON')
server.serve_forever()

server.serve_close()
print('[INFO] Servidor OFF')