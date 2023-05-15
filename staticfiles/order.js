function modPrice() {
    var price = document.getElementById("price").innerText;
    var quantity = document.getElementById("quantity").value;
    var total = parseInt(price) * parseInt(quantity);
    document.getElementById("total_price").innerHTML = "Total price: $" + total;
}