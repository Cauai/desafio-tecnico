@echo off
setlocal

REM Caminho fixo do seu Python
set "PYTHON_EXE=C:\Users\cauai\AppData\Local\Programs\Python\Python313\python.exe"

REM 1. Cria o ambiente virtual se não existir
IF EXIST ".venv" (
    echo Ambiente virtual .venv ja existe.
) ELSE (
    echo Criando ambiente virtual .venv...
    "%PYTHON_EXE%" -m venv .venv
)

REM 2. Ativa o ambiente virtual e instala os requisitos
echo Instalando dependencias...
call .venv\Scripts\activate
pip install -r requirements.txt

REM 3. Executa o script principal
echo Iniciando consumidor Kafka...
python main.py

endlocal
pause
