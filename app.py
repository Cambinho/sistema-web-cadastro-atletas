from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "chave-secreta-super-segura"  # troque em produção

# =====================
# CONFIG BANCO
# =====================
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:SUA_SENHA@localhost:5432/olimpiadas"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

UPLOAD_FOLDER = "static/images/atletas"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}



db = SQLAlchemy(app)

# =====================
# MODEL
# =====================
class Atleta(db.Model):
    __tablename__ = "atletas"

    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String(255))
    nome = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    esporte = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "esporte": self.esporte,
            "img": self.img
        }

# =====================
# ROTAS HTML (SSR)
# =====================

@app.route("/")
def home():
    # agora o JS busca os atletas pela API
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    erro = None

    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]

        if usuario == "admin" and senha == "123":
            session["admin"] = True
            return redirect(url_for("admin"))
        else:
            erro = "Usuário ou senha inválidos"

    return render_template("login.html", erro=erro)


@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect(url_for("home"))


@app.route("/admin")
def admin():
    if not session.get("admin"):
        return redirect(url_for("login"))

    return render_template("index.html")


@app.route("/admin/novo")
def novo_atleta():
    if not session.get("admin"):
        return redirect(url_for("login"))

    return render_template("novo_atleta.html")

# =====================
# API REST
# =====================

# LISTAR ATLETAS
@app.route("/api/atletas", methods=["GET"])
def api_listar_atletas():
    atletas = Atleta.query.all()
    return jsonify([a.to_dict() for a in atletas])

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS



# CRIAR ATLETA
@app.route("/api/atletas", methods=["POST"])
def api_criar_atleta():
    if not session.get("admin"):
        return jsonify({"erro": "Não autorizado"}), 401

    nome = request.form.get("nome")
    idade = request.form.get("idade")
    esporte = request.form.get("esporte")
    arquivo = request.files.get("img")

    if not arquivo or arquivo.filename == "":
        return jsonify({"erro": "Imagem obrigatória"}), 400

    if not allowed_file(arquivo.filename):
        return jsonify({"erro": "Formato de imagem inválido"}), 400

    nome_arquivo = secure_filename(arquivo.filename)
    caminho = os.path.join(app.config["UPLOAD_FOLDER"], nome_arquivo)
    arquivo.save(caminho)

    atleta = Atleta(
        nome=nome,
        idade=int(idade),
        esporte=esporte,
        img=nome_arquivo
    )
    print(request.form)
    print(request.files)

    db.session.add(atleta)
    db.session.commit()

    return jsonify({"mensagem": "Atleta criado com sucesso"}), 201



# EXCLUIR ATLETA
@app.route("/api/atletas/<int:id>", methods=["DELETE"])
def api_excluir_atleta(id):
    if not session.get("admin"):
        return jsonify({"erro": "Não autorizado"}), 401

    atleta = Atleta.query.get_or_404(id)

    db.session.delete(atleta)
    db.session.commit()

    return jsonify({"mensagem": "Atleta excluído"})


# =====================
# MAIN
# =====================
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
