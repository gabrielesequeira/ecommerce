document.addEventListener('DOMContentLoaded', () => {
    const container = document.querySelector('.carrinho-itens');
    const vazio = document.querySelector('.carrinho-vazio');
    const resumo = document.querySelector('.carrinho-resumo');
    const totalElement = document.getElementById('carrinho-total');

    let carrinho = JSON.parse(localStorage.getItem('carrinho')) || [];

    if (carrinho.length === 0) {
        vazio.style.display = 'block';
        resumo.style.display = 'none';
        return;
    }

    let total = 0;

    carrinho.forEach(item => {
        const card = document.createElement('div');
        card.classList.add('item-carrinho');

        card.innerHTML = `
            <img src="${item.img}" alt="${item.nome}" width="80">
            <div>
                <h4>${item.nome}</h4>
                <p>${item.descricao}</p>
                <p><strong>R$ ${item.preco.toFixed(2)}</strong></p>
            </div>
        `;

        container.appendChild(card);
        total += item.preco;
    });

    totalElement.textContent = `R$ ${total.toFixed(2)}`;
    resumo.style.display = 'block';
});
