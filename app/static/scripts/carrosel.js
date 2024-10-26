const totalImagens = 2;
const carrosselContainer = document.querySelector('.carrosel_galeria');
const capa = document.querySelector('.capa');

function adicionarImagens() {
    for (let i = 1; i <= totalImagens; i++) {
        const img = document.createElement('img');
        img.src = `static/images/galeria/img_${i}.jpg`; 
        img.alt = `Imagem ${i}`;
        carrosselContainer.appendChild(img);
    }
}

adicionarImagens();
let indiceAtual = 0;
const imagens = document.querySelectorAll('.carrosel_galeria img');

function mostrarImagemAtual() {
    imagens.forEach((img) => img.classList.remove('ativa'));
    imagens[indiceAtual].classList.add('ativa');
}
function proximaImagem() {
    indiceAtual = (indiceAtual + 1) % imagens.length;
    mostrarImagemAtual();
}

function imagemAnterior() {
    indiceAtual = (indiceAtual - 1 + imagens.length) % imagens.length;
    mostrarImagemAtual();
}

document.querySelector('.proximo_galeria').addEventListener('click', proximaImagem);
document.querySelector('.anterior_galeria').addEventListener('click', imagemAnterior);
mostrarImagemAtual();

