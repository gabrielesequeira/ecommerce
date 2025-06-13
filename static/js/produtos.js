// produtos.js

document.addEventListener("DOMContentLoaded", () => {
  const botoes = document.querySelectorAll(".produto-card button");

  botoes.forEach((botao, index) => {
    botao.addEventListener("click", () => {
      const card = botao.closest(".produto-card");
      const nome = card.querySelector("h3").innerText;
      const descricao = card.querySelector("p").innerText;
      const imagem = card.querySelector("img").src;
      const preco = 49.90 + index * 10; // Exemplo de preço fictício (pode vir do backend depois)

      const produto = {
        id: index + 1,
        nome,
        descricao,
        imagem,
        preco,
        quantidade: 1
      };

      adicionarAoCarrinho(produto);
    });
  });

  function adicionarAoCarrinho(produto) {
    let carrinho = JSON.parse(localStorage.getItem("carrinho")) || [];

    const index = carrinho.findIndex(p => p.id === produto.id);

    if (index !== -1) {
      carrinho[index].quantidade += 1;
    } else {
      carrinho.push(produto);
    }

    localStorage.setItem("carrinho", JSON.stringify(carrinho));
    alert(`${produto.nome} foi adicionado ao carrinho.`);
  }
});
