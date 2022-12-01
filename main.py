from jinja2 import Environment
from jinja2 import FileSystemLoader

from wsgiref.simple_server import make_server

env = Environment(loader=FileSystemLoader("templates"))

def application(environ, start_response): # WSGI - interface
    status = "200 OK"

    context = {
        "username": "Alex",
        "courses": ["Python", "JavaScript", "Ruby"]
    }

    path = environ.get('PATH_INFO')
    
    if path == "/":
        template = env.get_template("index.html")
    
    elif path == "/courses":
        template = env.get_template("courses.html")

    response = template.render(**context)
    start_response(status, [])

    return [bytes(response, 'UTF-8')]


PORT  = 8000

with make_server('localhost', PORT, application) as server: # create a namespace
    print(f">>> The server is listening in port {PORT} ")
    server.serve_forever()
