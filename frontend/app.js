/*lógica do frontend*/

fetch("http://localhost:5000/api/products")
    .then((response) => response.json())
    .then((data) => {
        console.log("Products:", data.products);
    })
    .catch((error) => console.error("Error fetching products:", error));

