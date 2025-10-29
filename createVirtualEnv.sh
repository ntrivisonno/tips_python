#!/bin/bash
# -------------------------------------------------------------------
# Crear entorno virtual con python3 -m venv en ~/virtualenvs/<nombre>
# Uso: ./createVirtualEnv.sh nombreDelEntorno
# Activa virtualEnv: source /home/zeeburg/virtualenvs/Python/bin/activate
# -------------------------------------------------------------------

# Verificar nombre del entorno
if [ -z "$1" ]; then
    echo "❌ Debes proporcionar un nombre para el entorno virtual."
    echo "Uso: ./createVirtualEnv.sh nombreDelEntorno"
    exit 1
fi

ENV_NAME="$1"
VENV_DIR="$HOME/virtualenvs/$ENV_NAME"

# Crear carpeta base si no existe
mkdir -p "$HOME/virtualenvs"

# Verificar que Python y venv estén disponibles
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 no está instalado."
    echo "Instalalo con:"
    echo "sudo apt install python3 python3-venv python3-pip"
    exit 1
fi

# Crear entorno si no existe
if [ ! -d "$VENV_DIR" ]; then
    echo "🛠️  Creando entorno virtual en: $VENV_DIR"
    python3 -m venv "$VENV_DIR"
else
    echo "✅ Entorno virtual ya existe: $VENV_DIR"
fi

# Activar entorno
source "$VENV_DIR/bin/activate"

# Actualizar pip
echo "⬆️  Actualizando pip..."
pip install --upgrade pip

# Instalar dependencias si existe requirements.txt
if [ -f requirements.txt ]; then
    echo "📦 Instalando dependencias desde requirements.txt..."
    pip install -r requirements.txt
else
    echo "⚠️  No se encontró requirements.txt en $(pwd)"
fi

# Mensaje final
echo "✅ Entorno virtual '$ENV_NAME' listo."
echo "👉 Activalo con:"
echo "   source $VENV_DIR/bin/activate"
