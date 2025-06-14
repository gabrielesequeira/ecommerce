document.addEventListener("DOMContentLoaded", () => {
  const containerItens = document.querySelector(".carrinho-itens");
  const textoVazio = document.querySelector(".carrinho-vazio");
  const resumo = document.querySelector(".carrinho-resumo");
  const totalSpan = document.getElementById("carrinho-total");

  let carrinho = JSON.parse(localStorage.getItem("carrinho")) || [];

  if (carrinho.length === 0) {
    textoVazio.style.display = "block";
    resumo.style.display = "none";
    return;
  }

  textoVazio.style.display = "none";
  resumo.style.display = "block";

  let total = 0;

  carrinho.forEach(produto => {
    const item = document.createElement("div");
    item.classList.add("item-carrinho");

    const subtotal = produto.preco * produto.quantidade;
    total += subtotal;

    item.innerHTML = `
      <div class="carrinho-item">
        <img src="${produto.imagem}" alt="${produto.nome}" width="100">
        <div>
          <h3>${produto.nome}</h3>
          <p>${produto.descricao}</p>
          <p>Preço unitário: R$ ${produto.preco.toFixed(2)}</p>
          <p>Quantidade: ${produto.quantidade}</p>
          <p><strong>Subtotal: R$ ${subtotal.toFixed(2)}</strong></p>
        </div>
      </div>
    `;

    containerItens.appendChild(item);
  });

  totalSpan.textContent = `R$ ${total.toFixed(2)}`;
});

function limparCarrinho() {
  localStorage.removeItem("carrinho");
  location.reload();
}
