#!/bin/bash

# Verificar si se proporcionó un nombre
if [ -z "$1" ]; then
    echo "❌ Debes proporcionar un nombre para el entorno virtual."
    echo "Uso: ./createVirtualEnv.sh nombreDelEntorno"
    exit 1
fi

ENV_NAME="$1"
VENV_DIR=~/virtualenvs/$ENV_NAME

# Crear carpeta base si no existe
mkdir -p ~/virtualenvs

# Verificar si virtualenv está instalado
if ! command -v virtualenv &> /dev/null && [ ! -x ~/.local/bin/virtualenv ]; then
    echo "❌ 'virtualenv' no está instalado. Ejecutá:"
    echo "pip3 install --user virtualenv"
    exit 1
fi

# Crear entorno virtual si no existe
if [ ! -d "$VENV_DIR" ]; then
    echo "🛠️  Creando entorno virtual en: $VENV_DIR"
    ~/.local/bin/virtualenv "$VENV_DIR"
else
    echo "✅ Entorno virtual ya existe: $VENV_DIR"
fi

# Activar entorno
source "$VENV_DIR/bin/activate"

# Instalar dependencias desde el requirements.txt local
if [ ! -f requirements.txt ]; then
    echo "❌ No se encontró requirements.txt en $(pwd)"
    deactivate
    exit 1
fi

echo "📦 Instalando dependencias desde requirements.txt..."
pip install -r requirements.txt

echo "✅ Entorno virtual '$ENV_NAME' listo. Activalo con:"
echo "source $VENV_DIR/bin/activate"
