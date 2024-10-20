# Projeto JAX - Aplicação WEB

## O projeto

- Trata-se da aplicação WEB que centraliza presença digital do ProjetoJAX. 
- Inicialmente se apresenta como Static_Web, contudo posteriormente irá evoluir [ o céu é o limite ]

## Stacks e tecnologias

- HTML5 / CSS3 / JavaScript -> FrontEnd

- Python / Flask -> BackEnd

## Estrutura de Diretórios
project-jax/
│
├── app.py                -> Arquivo principal para iniciar o Flask
├── config.py             -> Configurações globais
├── requirements.txt      -> Dependências
├── Procfile              -> Arquivo para o Render
├── app/                  -> Pasta do aplicativo (onde ficam módulos e rotas)
│   ├── __init__.py       -> Arquivo de inicialização do app Flask
│   ├── routes.py         -> Definição das rotas
│   ├── models.py         -> Definição dos modelos (caso seja necessário no futuro)
│   └── modules/          -> Módulos de funcionalidades extras
│       └── example.py    -> Exemplo de módulo
│
|   ├── static/           -> Arquivos estáticos (CSS, JS, imagens)
│       ├── styles/
│           └── Arquivos CSS
│       ├── scripts/
│           └── Arquivos JS
│       └── images/
│           └── Arquivos de Imagens
│
│   ├── templates/        -> Templates HTML
└──     └── Arquivos HTML

## Estrura de rotas

/home
Redireciona para a página inicial

/jax_services
Redireciona para a página posterior do serviço e/ou página inicial ( evita acessos para rotas inexistentes ou usadas para testes de ambientes dev )

/sobre
Redireciona para a página sobre
