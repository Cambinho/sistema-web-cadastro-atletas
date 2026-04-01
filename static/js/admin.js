document.getElementById("form-atleta").addEventListener("submit", function (e) {
    e.preventDefault();

    const dados = {
        nome: this.nome.value,
        idade: parseInt(this.idade.value),
        esporte: this.esporte.value,
        img: this.img.value
    };

    fetch("/api/atletas", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(dados)
    })
    .then(res => res.json())
    .then(resposta => {
        document.getElementById("mensagem").innerText = resposta.mensagem;
        this.reset();
    });
});
