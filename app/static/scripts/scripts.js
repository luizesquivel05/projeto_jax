document.addEventListener('DOMContentLoaded', function() {
    const button = document.getElementById('getStartedButton');
    button.addEventListener('click', function() {
        alert('Estamos separando algumas informações para você. Aguarde um momento.');
        window.open('https://onedrive.live.com/?redeem=aHR0cHM6Ly8xZHJ2Lm1zL2IvYy85NWYzZTdkYTNkYzRjNWEyL0VlZG9nV0hmY3Y1SWdJZGRiVC15NXlBQmNYS3lzYy1WUFVQa215UDhSVnpTbXc%5FZmJjbGlkPVBBWlhoMGJnTmhaVzBDTVRFQUFhYk1MMWNiaEk5YlRCeTl2Y0pQWEp0WDBfSzhaUTh4UUpTamdvOWZ6OGZVTU53V1VhaW85Y1owYTFrX2FlbV9ZMU5QQTVnY2EyT3NrRlFEY0pjcklR&cid=95F3E7DA3DC4C5A2&id=95F3E7DA3DC4C5A2%21s618168e772df48fe80875d6d3fb2e720&parId=95F3E7DA3DC4C5A2%21s8ce712d2bb55499587e1235168bb7b15&o=OneUp', '_blank');
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const logo = document.getElementById("logo");
    const navbar = document.getElementById("navbar");

    logo.addEventListener("click", function() {
        navbar.classList.toggle("hidden"); // Alterna a classe 'hidden' no navbar
    });
});