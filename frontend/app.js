// Carregar lista de produtos
async function loadProducts() {
    const response = await fetch('/products');
    const products = await response.json();

    const productList = document.getElementById('product-list');
    productList.innerHTML = '';

    products.forEach(product => {
        const productElement = document.createElement('div');
        productElement.innerHTML = `
            <h3>${product.name} - R$${product.price.toFixed(2)}</h3>
            <p>${product.description}</p>
            <button onclick="addToCart(${product.id})">Adicionar ao Carrinho</button>
        `;
        productList.appendChild(productElement);
    });
}

// Adicionar item ao carrinho
async function addToCart(productId) {
    await fetch('/cart', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ product_id: productId, quantity: 1 })
    });

    alert('Item adicionado ao carrinho!');
    loadCart();
}

// Carregar carrinho
async function loadCart() {
    const response = await fetch('/cart');
    const cart = await response.json();

    const cartDiv = document.getElementById('cart');
    cartDiv.innerHTML = '';

    cart.forEach(item => {
        cartDiv.innerHTML += `<p>Produto ID: ${item.product_id}, Quantidade: ${item.quantity}</p>`;
    });
}

// Carregar dados ao iniciar
loadProducts();
loadCart();
