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
        if '.html' not in path and 'sitemap' not in path:
            return render_template(f'{path}.html')
        if 'sitemap' in path:
            return render_template('sitemap.xml')
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

@main.route("/jaxresume")
def jaxresume():
    from .utils import load_posts
    return render_template("jaxresume.html", temas = load_posts(main)[0])

@main.route("/jaxresume/<tema>")
def temas(tema):
    from .utils import load_posts
    tema = str(tema).capitalize()
    posts = load_posts(main)[1][tema]
    if posts is None:
        return render_template("error.html", title="ERROR", error="Tema não encontrado")
    filtered_posts = [post for post in posts if post['theme'].lower() == tema.lower()]
    if len(filtered_posts) == 0:
        return render_template("error.html", title="ERROR", error="Tema não encontrado")
    return render_template("lista_posts.html", posts=filtered_posts, tema=tema)

@main.route("/jaxresume/post/<int:post_id>")
def post(post_id):
    from .utils import load_posts
    post_id = int(post_id)
    posts = load_posts(main)[2][post_id]
    if posts is None:
        return render_template("error.html", title="ERROR", error="Post não encontrado")
    if post is None:
        return render_template("error.html", title="ERROR", error="Post não encontrado")
    return render_template("post_completo.html", post=posts)

@main.route("/jaxresume/post/<post_id>/add_comment", methods=["POST"])
def add_comment_route(post_id):
    from flask import request
    from .utils import add_comment, load_posts
    author = request.form.get("author")
    text = request.form.get("text")

    if not author or not text:
        return "Erro: Nome e texto do comentário são obrigatórios.", 400

    try:
        _ = add_comment(post_id, author, text, main)
        post_id = int(post_id)
        posts = load_posts(main)[2][post_id]
        return render_template("post_completo.html", post=posts)
    except FileNotFoundError as e:
        return render_template("error.html", title="ERROR", error=str(e))
