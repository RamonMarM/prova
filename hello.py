from datetime import datetime
from flask import Flask, render_template, request, make_response, redirect, abort
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)

bootstrap = Bootstrap(app)
moment = Moment(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/')
def index(name, prontuario):
    name = Ramon;
    prontuario = pt3019471;
     return render_template('index.html', name = name, prontuario = prontuario, current_time=datetime.utcnow())


#@app.route('/user/<name>/<prontuario>/<institution>')
#def user(name, prontuario, institution):
  #  return render_template('user.html', 
       #                    name=name, 
        #                   prontuario=prontuario,
            #               institution=institution);

@app.route('/professores>')
def contextorequisicao(name):
    user_agent = request.headers.get('User-Agent');
    remote_addr = request.remote_addr;
    remote_host = request.host;
    return render_template('contexto.html',
                           name=name, 
                           user_agent=user_agent, 
                           remote_addr=remote_addr,
                           remote_host=remote_host);







