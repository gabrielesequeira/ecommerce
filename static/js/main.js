function toggleSenha() {
    const senhaInput = document.getElementById('senha');
    const toggleButton = document.querySelector('.toggle-senha');

    if (senhaInput.type === 'password') {
        senhaInput.type = 'text';
        toggleButton.innerHTML = '🙈'; // Mostrando senha
    } else {
        senhaInput.type = 'password';
        toggleButton.innerHTML = '👁️'; // Escondendo senha
    }
}
