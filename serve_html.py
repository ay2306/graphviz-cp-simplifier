import http.server
import socketserver
import socket
import sys
import psutil
PORT = 8000
LOCALHOST = 'localhost'
def get_pid(port):
    connections = psutil.net_connections()
    for con in connections:
        if con.raddr != tuple():
            if con.raddr.port == port:
                return con.pid, con.status
        if con.laddr != tuple():
            if con.laddr.port == port:
                return con.pid, con.status
    return -1


def close_port_if_open(port = PORT, HOST = LOCALHOST):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if sock.connect_ex((HOST, port)) == 0:
        print("PORT OPEN")
        p_id = get_pid(port)
        psutil.Process(p_id).kill()
        
def serve_file(filename, port = PORT):
    close_port_if_open(port)
    handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", port), handler) as httpd:
        print("Server started at localhost:" + str(port))
        httpd.serve_forever()