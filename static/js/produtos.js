document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.produto-card').forEach((card, inicio) => {
        const nome = card.querySelector('h3').innerText;
        const descricao = card.querySelector('p').innerText;
        const img = card.querySelector('img').getAttribute('src');
        const preco = 29.90 + inicio * 10; // só para teste

        card.querySelector('button').addEventListener('click', () => {
            let carrinho = JSON.parse(localStorage.getItem('carrinho')) || [];

            // adiciona produto
            carrinho.push({ nome, descricao, preco, img });

            // salva no localStorage
            localStorage.setItem('carrinho', JSON.stringify(carrinho));

            alert(`${nome} adicionado ao carrinho!`);
        });
    });
});
