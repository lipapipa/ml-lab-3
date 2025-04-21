import subprocess

with open("best_model.txt", "r", encoding="utf-8") as f:
    path = f.read().strip()

print(f"Serving model at: {path}")

# Запускаем MLflow в фоне (если нужно - можно убрать shell=True)
subprocess.Popen([
    "mlflow", "models", "serve",
    "-m", path,
    "-p", "5003",
    "--no-conda"
], shell=True)
