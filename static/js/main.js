// static/js/main.js

// 1. na página contato.html
document.addEventListener('DOMContentLoaded', function () { //código executado depois que o html é carregado evitando erros ao acessar elementos que ainda não existem
    const form = document.querySelector('.form-contato'); //armazena o form da página contato em uma variavel form
    if (form) {
        form.addEventListener('submit', function () { 
            alert('Sua mensagem foi enviada!'); // envia um alerta caso encontrado e submetido
        });
    }

    document.addEventListener('DOMContentLoaded', function () {
        const senhaInput = document.querySelector('input[name="senha"]');
        const toggle = document.querySelector('.toggle-senha');

        if (senhaInput && toggle) {
            toggle.addEventListener('click', function () {
                const isPassword = senhaInput.type === 'password';
                senhaInput.type = isPassword ? 'text' : 'password';
                toggle.textContent = isPassword ? '👁️‍🗨️' : '👁️';
            });
        }
    });





});
