@echo off
setlocal

echo ================================
echo Iniciando o setup do projeto...
echo ================================

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

REM 3. Executa o docker compose
echo Executando Docker...
docker-compose up

REM 4. Executa o kafka producer
echo Executando Docker...
python src/kafka_producer_mock.py

REM 5. Mensagem final de sucesso
echo ================================
echo Projeto executado com sucesso! ✅
echo ================================

endlocal
pause
