# Get started with socket_project

## Simple setup
### 1. Working tree
```
root/
├─ main.py
└── frontends/
   └── ... # html, css, js, img files must be placed here 
```

### 2. Your `main.py` file
```py
# The most basic code in order to run the local server
from socket_project.server.host import Host

host = Host("localhost", 8000)

@host.url.route("/")
def home_page():
    return 'index.html'

host.run_server()
```
