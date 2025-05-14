async function login() {
  const username = document.getElementById('login-username').value;
  const password = document.getElementById('login-password').value;

  const res = await fetch('/login', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({username, password})
  });

  if (res.ok) {
    alert('Login realizado!');
    loadProducts();
    loadCart();
  } else {
    alert('Falha no login.');
  }
}

async function register() {
  const username = document.getElementById('register-username').value;
  const password = document.getElementById('register-password').value;

  const res = await fetch('/register', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({username, password})
  });

  if (res.ok) {
    alert('Cadastro feito com sucesso!');
  } else {
    alert('Erro no cadastro.');
  }
}

async function loadProducts() {
  const res = await fetch('/products');
  const data = await res.json();

  const list = document.getElementById('product-list');
  list.innerHTML = '';
  data.forEach(p => {
    const item = document.createElement('li');
    item.innerHTML = `${p.name} - R$ ${p.price.toFixed(2)} 
      <button onclick="addToCart(${p.id})">Adicionar ao carrinho</button>`;
    list.appendChild(item);
  });
}

async function addToCart(product_id) {
  const res = await fetch('/cart', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({product_id, quantity: 1})
  });

  if (res.ok) {
    alert('Adicionado ao carrinho!');
    loadCart();
  } else {
    alert('Erro ao adicionar.');
  }
}

async function loadCart() {
  const res = await fetch('/cart');
  const list = document.getElementById('cart-list');
  list.innerHTML = '';

  if (res.status === 401) {
    list.innerHTML = '<li>Você precisa estar logado para ver o carrinho.</li>';
    return;
  }

  const data = await res.json();
  data.forEach(item => {
    const li = document.createElement('li');
    li.textContent = `${item.product_name} - Quantidade: ${item.quantity} - Total: R$ ${(item.quantity * item.price).toFixed(2)}`;
    list.appendChild(li);
  });
}

// Carrega produtos e carrinho ao abrir
window.onload = () => {
  loadProducts();
  loadCart();
};
