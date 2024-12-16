/*lógica do frontend*/

document.addEventListener("DOMContentLoaded", () => {
    function fetchProducts() {
        fetch("http://127.0.0.1:5000/api/products")
            .then(response => response.json())
            .then(data => {
                const productsList = document.getElementById("products-list");
                data.forEach(product => {
                    const productElement = document.createElement("li");
                    productElement.textContent = `${product.name} - R$${product.price}`;
                    const addButton = document.createElement("button");
                    addButton.textContent = "Adicionar ao carrinho";
                    addButton.onclick = () => addToCart(product.id);
                    productElement.appendChild(addButton);
                    productsList.appendChild(productElement);
                });
            })
            .catch(error => console.error("Erro ao carregar produtos:", error));
    }

    function addToCart(productId) {
        const quantity = 1;  // Por simplicidade, vamos adicionar 1 unidade de cada vez
        fetch("http://127.0.0.1:5000/api/cart/add", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ product_id: productId, quantity: quantity })
        })
        .then(response => response.json())
        .then(data => alert(data.message))
        .catch(error => console.error("Erro ao adicionar ao carrinho:", error));
    }

    function fetchCart() {
        fetch("http://127.0.0.1:5000/api/cart")
            .then(response => response.json())
            .then(data => {
                const cartList = document.getElementById("cart-list");
                cartList.innerHTML = '';
                data.forEach(item => {
                    const cartItem = document.createElement("li");
                    cartItem.textContent = `${item.product} - Quantidade: ${item.quantity}`;
                    cartList.appendChild(cartItem);
                });
            })
            .catch(error => console.error("Erro ao carregar carrinho:", error));
    }

    fetchProducts();
    fetchCart();
});
