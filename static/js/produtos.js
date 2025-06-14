document.addEventListener("DOMContentLoaded", () => {
  const botoesAdicionar = document.querySelectorAll(".btn-adicionar");

  botoesAdicionar.forEach(botao => {
    botao.addEventListener("click", () => {
      const id = botao.dataset.id;
      const nome = botao.dataset.nome;
      const preco = parseFloat(botao.dataset.preco);
      const descricao = botao.dataset.descricao;
      const imagem = botao.dataset.imagem;

      const produto = {
        id,
        nome,
        preco,
        descricao,
        imagem
      };

      adicionarAoCarrinho(produto);
    });
  });
});

function adicionarAoCarrinho(produto) {
  let carrinho = JSON.parse(localStorage.getItem("carrinho")) || [];

  const existente = carrinho.find(p => p.id === produto.id);

  if (existente) {
    existente.quantidade += 1;
  } else {
    produto.quantidade = 1;
    carrinho.push(produto);
  }

  localStorage.setItem("carrinho", JSON.stringify(carrinho));
  alert(`✅ ${produto.nome} adicionado ao carrinho!`);
}
