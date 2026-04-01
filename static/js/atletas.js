// =============================
// LISTAR ATLETAS (HOME / ADMIN)
// =============================

document.addEventListener("DOMContentLoaded", () => {

    const container = document.getElementById("card-container");

    if (container) {
        fetch("/api/atletas")
            .then(response => response.json())
            .then(atletas => {
                container.innerHTML = "";

                atletas.forEach(atleta => {
                    const card = document.createElement("div");
                    card.className = "card";

                    card.innerHTML = `
                        <img src="/static/images/atletas/${atleta.img}" alt="${atleta.nome}">
                        <h3>${atleta.nome}</h3>
                        <p><strong>Idade:</strong> ${atleta.idade}</p>
                        <p><strong>Esporte:</strong> ${atleta.esporte}</p>
                    `;

                    container.appendChild(card);
                });
            })
            .catch(error => console.error("Erro ao carregar atletas:", error));
    }

    // =============================
    // CADASTRAR ATLETA (ADMIN)
    // =============================

    const form = document.getElementById("form-atleta");

    if (form) {
        form.addEventListener("submit", (e) => {
            e.preventDefault();

            const formData = new FormData(form);

            fetch("/api/atletas", {
                method: "POST",
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.erro) {
                    alert(data.erro);
                    return;
                }

                alert("Atleta cadastrado com sucesso!");
                form.reset();
            })
            .catch(error => console.error("Erro ao cadastrar atleta:", error));
        });
    }

});
