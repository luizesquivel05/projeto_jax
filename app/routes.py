from flask import Blueprint, render_template, Flask, send_from_directory

main = Blueprint("main", __name__)

@main.route('/google-site-verification=<token>.html')
def google_verification():
    return render_template('google-site-verification=OoaVt6jNPKKCO9AiGsIeFX3_muqcrkHbLgRui2LYSRg.html')

@main.route('/sitemap')
def sitemap():
    return render_template('sitemap.xml')

@main.route("/<path:path>")
def jax_services(path):
    try:
        if '.html' not in path:
            return render_template(f'{path}.html')
        else:
            return render_template(f'{path}')
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
