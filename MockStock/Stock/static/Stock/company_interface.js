// window.alert("script loaded");

document.getElementById("update_price").onchange = (event) => {
    event.preventDefault();
    const updated_price = document.getElementById("update_price");
    const updated_price_val = updated_price.value;
    const curVal = parseFloat(document.getElementById("curVal").innerHTML.split("₹")[1]);
    if (updated_price_val < curVal) {
        updated_price.classList.remove("text-green-500");
        updated_price.classList.add("text-red-500");
    } else if (updated_price_val > curVal) {
        updated_price.classList.add("text-green-500");
        updated_price.classList.remove("text-red-500");
    } else {
        updated_price.classList.remove("text-green-500");
        updated_price.classList.remove("text-red-500");
    }
    // console.log(curVal);
};

document.getElementById("priceUpdateForm").onsubmit = (event) => {
    event.preventDefault();

    const company_id = document.getElementById("company_id").value;
    const updated_price = document.getElementById("update_price").value;

    console.log(company_id, updated_price);

    fetch(`/priceUpdate?company=${company_id}&updated_price=${updated_price}`)
    .then(request => request.json())
    .then(data => {
        console.log(data["message"]);

        if (data["message"] != "No Change")
            window.location.reload();
    })
};