document.addEventListener('DOMContentLoaded', function() {
    const button = document.getElementById('getStartedButton');
    button.addEventListener('click', function() {
        alert('Estamos separando algumas informações para você. Aguarde um momento.');
        window.open('/documento', '_blank');
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const logo = document.getElementById("logo");
    const navbar = document.getElementById("navbar");

    logo.addEventListener("click", function() {
        navbar.classList.toggle("hidden"); // Alterna a classe 'hidden' no navbar
    });
});