#!/usr/bin/env bash

# =====================================================
# 🧩 Script: updateRequirements.sh
# 📦 Propósito:
#    - Actualiza el entorno virtual existente
#    - Instala nuevas librerías (si se pasan como argumentos)
#    - Actualiza automáticamente requirements.txt
#
# uso: ./updateRequirements Python numpy
# =====================================================

# 📁 Directorio base donde se crean los entornos virtuales
VENV_DIR="$HOME/virtualenvs"
ENV_NAME="$1"

# ✅ Verificación de argumentos
if [ -z "$ENV_NAME" ]; then
    echo "❌ Uso: $0 <nombre_entorno> [paquete1 paquete2 ...]"
    exit 1
fi

# 📍 Ruta completa del entorno virtual
VENV_PATH="$VENV_DIR/$ENV_NAME"

if [ ! -d "$VENV_PATH" ]; then
    echo "❌ El entorno '$ENV_NAME' no existe en $VENV_DIR"
    exit 1
fi

# 🧠 Activar entorno virtual
echo "✅ Activando entorno: $ENV_NAME"
source "$VENV_PATH/bin/activate"

# 🚀 Instalar dependencias existentes
if [ -f requirements.txt ]; then
    echo "📦 Instalando dependencias desde requirements.txt..."
    pip install -r requirements.txt
else
    echo "⚠️ No se encontró requirements.txt, se omitió la instalación inicial."
fi

# 📥 Instalar paquetes adicionales si se pasaron como argumentos
if [ $# -gt 1 ]; then
    shift
    echo "➕ Instalando nuevos paquetes: $@"
    pip install "$@"
fi

# 🧾 Actualizar requirements.txt con el entorno actual
echo "📝 Actualizando requirements.txt..."
pip freeze > requirements.txt

# 🔚 Desactivar entorno
deactivate
echo "✅ Entorno '$ENV_NAME' actualizado correctamente."
