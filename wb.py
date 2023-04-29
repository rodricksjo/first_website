from http.server import HTTPServer, SimpleHTTPRequestHandler

# Set the server address and port
server_address = ('localhost', 8001)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

# Start the server
print('Server running at localhost:8001...')
httpd.serve_forever()
