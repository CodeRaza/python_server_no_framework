import http.server
import socketserver
from urllib.parse import urlparse, parse_qs
import json

port = 8000
directory = "." 
handler = http.server.SimpleHTTPRequestHandler

data = [
    {
        "id": 1,
        "username": "ali"
    },
    {
        "id": 2,
        "username": "raza"
    },
    {
        "id": 3,
        "username": "hassan"
    },
]

class CustomRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path

        params = parse_qs(parsed_url.query)
        
        if path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())
    
        elif path == '/about':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('about.html', 'rb') as file:
                self.wfile.write(file.read())
                
        elif path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            users = json.dumps(data).encode('utf-8')
            
            if params.get("user_id"):
                the_user_id = params['user_id']
                for user in data:
                    if user['id'] == int(the_user_id[0]):
                        user_ = json.dumps(user).encode('utf-8')
                        self.wfile.write(user_)
            else:
                self.wfile.write(users)
                
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

    def do_POST(self):
        
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        
        if path == '/user_data':
            content_length = int(self.headers['Content-Length'])
            user_data = self.rfile.read(content_length).decode('utf-8')
            user_ = json.loads(user_data)
            new_user = {'id': data[-1]['id'] + 1, 'username': user_['username']}
            data.append(new_user)
            
            res = json.dumps({'message': "done"}).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(res)

with socketserver.TCPServer(("", port), CustomRequestHandler) as httpd:
    print(f"Server Up at: http://localhost:{port}/")
    print(f"Let's Goooo!")
    httpd.serve_forever()
