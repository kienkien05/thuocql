function saveMedicines() {
    let rows = document.querySelectorAll("#medicinesTable tr");
    let medicines = [];

    rows.forEach((row, index) => {
        if (index === 0) return;

        let id = row.cells[0].textContent;
        let name = row.querySelector(".name").value;
        let quantity = row.querySelector(".quantity").value;
        let price = row.querySelector(".price").value;

        medicines.push({ id, name, quantity, price });
    });

    fetch("/save_medicines", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(medicines)
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        location.reload();
    })
    .catch(error => console.error("Lỗi:", error));
}

function addMedicine() {
    let name = document.getElementById("new_name").value;
    let quantity = document.getElementById("new_quantity").value;
    let price = document.getElementById("new_price").value;

    fetch("/add_medicine", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, quantity, price })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        location.reload();
    })
    .catch(error => console.error("Lỗi:", error));
}
