import subprocess
import os

try:
    with open("best_model.txt", "r", encoding="utf-8") as f:
        path = f.read().strip()

    print(f"[INFO] Serving model from: {path}")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Model path does not exist: {path}")

    subprocess.Popen([
        "mlflow", "models", "serve",
        "-m", path,
        "-p", "5003",
        "--no-conda"
    ], shell=True)

except Exception as e:
    print(f"[ERROR] {e}")
    raise
