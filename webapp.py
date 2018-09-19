from flask import Flask, request

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='template')

@app.route('/')
def inicio():
    return app.send_static_file('inicial.html')


@app.route('/sobre')
def sobre():
    return app.send_static_file('sobre.html')

@app.route('/simulados')
def simulados():
    return app.send_static_file('simulados.html')

@app.route('/login')
def login():
    return app.send_static_file('login.html')

@app.route('/cadastro')
def cadastro():
    return app.send_static_file('cadastro.html')




if __name__ == '__main__':
  app.run(debug=True)
