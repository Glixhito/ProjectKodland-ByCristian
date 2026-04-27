# Fallo de Confirmacion

Un juego experimental de preguntas binarias donde tu memoria y el propio sistema se degradan.
Cada respuesta afecta tu estabilidad, y el sistema puede distorsionar, culparte o caer en bucles.

## Concepto

Eres un operador que responde preguntas dicotomicas (Si / No, Verdad / Mentira…).
El sistema que te evalua no es perfecto: comienza a fallar, a olvidar, a alterar sus registros y a culparte de sus propios errores.

¿Seguiras confiando en el? ¿Afectaran las fallas a tus respuestas?

## Requisitos

- Python 3.8 o superior
- Pygame

## Instalacion

```bash
# Clonar o descargar el proyecto
cd ruta/del/proyecto

# Crear y activar entorno virtual (opcional)
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Instalar Pygame
pip install pygame


#Como Jugar
#Ejecutar el archivo principal
python main.py


#Estructura del Proyecto 
.
├── main.py              # Punto de entrada
├── menu.py              # Menu inicial
├── game.py              # Bucle principal del juego
├── state.py             # Clase MentalState (estabilidad, culpa, etc.)
├── ui.py                # Dibujado de la interfaz (con jitter, barras falsas)
├── memory.py            # Almacenamiento y corrupcion de respuestas
├── enemy.py             # Ruido cognitivo (ataques aleatorios)
├── game_questions.py    # Lista de preguntas base
├── endings.py           # Textos de finalizacion
└── README.md