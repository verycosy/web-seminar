const productList = document.getElementById("product-list");
const newProductName = document.getElementById("new-product-name");
const newProductCategory = document.getElementById("new-product-category");
const addProductBtn = document.getElementById("add-product-btn");

addProductBtn.addEventListener("click", (evt) => {
  fetch("/product", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      name: newProductName.value,
      category: newProductCategory.value,
    }),
  })
    .then((res) => {
      const option = document.createElement("option");
      option.textContent = newProductName.value;

      productList.append(option);
    })
    .catch((err) => {
      console.error(err);
    });
});

productList.addEventListener("change", (evt) => {
  const productId = productList.value;
  fetch(`/product/${productId}`)
    .then((res) => res.json())
    .then((res) => {
      console.log(res);
    })
    .catch((err) => console.error(err));
});
