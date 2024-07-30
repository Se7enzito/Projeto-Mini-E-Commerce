document.getElementById('compradorForm').addEventListener('submit', function(event) {
    event.preventDefault();

    fetch(this.action, {
        method: this.method,
        body: new FormData(this)
    }).then(response => {
        if (response.ok) {
            this.reset();
            window.location.href = "/";
        } else {
            alert("Erro ao criar o comprador.");
        }
    }).catch(error => {
        console.error('Erro:', error);
        alert("Erro ao criar o comprador.");
    });
});

document.getElementById('vendedorForm').addEventListener('submit', function(event) {
    event.preventDefault();

    fetch(this.action, {
        method: this.method,
        body: new FormData(this)
    }).then(response => {
        if (response.ok) {
            this.reset();
            window.location.href = "/";
        } else {
            alert("Erro ao criar o comprador.");
        }
    }).catch(error => {
        console.error('Erro:', error);
        alert("Erro ao criar o comprador.");
    });
});

document.getElementById('itemForm').addEventListener('submit', function(event) {
    event.preventDefault();

    fetch(this.action, {
        method: this.method,
        body: new FormData(this)
    }).then(response => {
        if (response.ok) {
            this.reset();
            window.location.href = "/";
        } else {
            alert("Erro ao criar o comprador.");
        }
    }).catch(error => {
        console.error('Erro:', error);
        alert("Erro ao criar o comprador.");
    });
});

const myModal = new bootstrap.Modal(
    document.getElementById("modalId"),
    options,
);