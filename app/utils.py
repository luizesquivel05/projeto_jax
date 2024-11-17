
def create_app():
    from flask import Flask
    from .routes import main
    from config import Config
    app = Flask(__name__)
    app.register_blueprint(main)
    app.config.from_object(Config)
    return app

def load_posts(app):
    import os
    import json
    themes = set() 
    summary_data = {} 
    detailed_data = {} 

    def format_content(content):
        """Formata o conteúdo do post em HTML amigável."""
        paragraphs = content.split("\n\n")
        formatted = ""
        
        for paragraph in paragraphs:
            if paragraph.strip().startswith("Dicas Práticas"):
                formatted += f"<h3>{paragraph.strip()}</h3>"
            elif paragraph.strip().startswith("-"):
                items = paragraph.strip().split("\n")
                formatted += "<ul>"
                for item in items:
                    formatted += f"<li>{item[2:].strip()}</li><\br>" 
                formatted += "</ul>"
            else:
                formatted += f"<p>{paragraph.strip()}</p>"
        
        return formatted

    json_folder = os.path.join(app.root_path, 'static', 'jsons')  

    for filename in os.listdir(json_folder):
        if filename.endswith('.json'):
            file_path = os.path.join(json_folder, filename)

            with open(file_path, 'r', encoding='utf-8') as f:
                post = json.load(f)
                detailed_data[post['id']] = post
                themes.add(post['theme'])
                post['content'] = format_content(post['content'])

                if post['theme'] not in summary_data:
                    summary_data[post['theme']] = []
                summary_data[post['theme']].append({
                    'id': post['id'],
                    'image': post['image'],
                    'title': post['title'],
                    'subtitle': post['subtitle'],
                    'author': post['author'],
                    'theme': post['theme'],
                    'subtheme': post['subtheme'],
                    'date_published': post['date_published'],
                })

    return (sorted(list(themes)), summary_data, detailed_data)

def add_comment(post_id, author, text, app):

    import os
    import json
    from datetime import datetime

    json_folder = os.path.join(app.root_path, 'static', 'jsons')
    post_file = os.path.join(json_folder, f'post_{post_id}.json')

    if not os.path.exists(post_file):
        raise FileNotFoundError(f"Post com ID {post_id} não encontrado.")

    with open(post_file, 'r', encoding='utf-8') as f:
        post_data = json.load(f)

    new_comment = {
        "author": author,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "text": text
    }

    if "comments" not in post_data:
        post_data["comments"] = []

    post_data["comments"].append(new_comment)

    with open(post_file, 'w', encoding='utf-8') as f:
        json.dump(post_data, f, ensure_ascii=False, indent=4)

    return new_comment
