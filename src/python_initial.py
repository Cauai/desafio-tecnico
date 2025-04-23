import os
import sys
import subprocess
import time

def criar_venv():
    try:
        if os.path.exists(".venv"):
            print("Ambiente virtual .venv já existe.")
            return

        print("Criar venv padrão")
        subprocess.check_call([sys.executable, "-m", "venv", ".venv"])

        # Aguarda um instante para garantir que o sistema crie o diretório
        time.sleep(1)

        # Verifica novamente se o ambiente foi criado com sucesso
        if os.path.exists(".venv"):
            print("Ambiente .venv criado com sucesso. Encerrando terminal...")
            os.system("taskkill /F /PID " + str(os.getppid()))
        else:
            print("Erro: .venv não foi criado corretamente.")

    except Exception as e:
        print(f"Erro ao criar o ambiente virtual: {e}")

if __name__ == "__main__":
    criar_venv()