# Date:2020/5/12
# Author:Lingchen
# Mark: 提供一个支持CGI的WEB服务器
from http.server import HTTPServer, CGIHTTPRequestHandler

port = 8086
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()
