import os

UPLOAD_FOLDER = "backend/uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
from flask import Flask, send_from_directory
from flask_cors import CORS
from routes.resume_routes import resume_bp

app = Flask(
    __name__,
    static_folder="../frontend",
    static_url_path=""
)

CORS(app)

app.register_blueprint(resume_bp)

# serve index
@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")


if __name__ == "__main__":
    app.run(debug=True)