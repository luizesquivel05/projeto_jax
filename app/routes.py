from flask import Blueprint, render_template, Flask

main = Blueprint("main", __name__)

@main.route("/<path:path>")
def jax_services(path):
    try:
        return render_template(f'{path}.html')
    except Exception as e:
        if '.html' in str(e):
            return render_template('error.html', title="ERROR", error=f"Página ( {str(e)} ) não encontrada")
        return render_template('error.html', title="ERROR", error=str(e))

@main.route('/')
def home():
    return render_template('home.html', title='Home')

@main.route('/sobre')
def sobre():
    return render_template('sobre.html', title='Sobre')

@main.route('/galeria')
def galeria():
    return render_template('galeria.html', title='Galeria')

@main.route('/contato')
def contato():
    return render_template('contato.html', title='Contato')

@main.route('/historia')
def historia():
    return render_template('historia.html', title='História')

@main.route('/funcionalidades')
def funcionalidades():
    return render_template('funcionalidades.html', title='Funcionalidades')

@main.route('/documento')
def documento():
    return render_template('documento.html', title='Documentacao')
