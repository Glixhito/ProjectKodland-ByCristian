def ending_text(state):
    if state.blame >= 3:
        return (
            "SISTEMA: No puedo continuar así.\n"
            "Tus respuestas ya no coinciden.\n"
            "Hemos perdido la coherencia."
        )

    elif state.distortion >= 5:
        return (
            "SISTEMA: Algo se perdió en el camino.\n"
            "Los registros se contradicen.\n"
            "No sé si fui yo quien cambió."
        )

    elif state.repetition >= 4:
        return (
            "SISTEMA: Patrones detectados.\n"
            "Repetición infinita.\n"
            "¿Estamos atrapados en un ciclo?"
        )

    elif state.stability <= 0:
        return (
            "SISTEMA: Estabilidad crítica.\n"
            "La interfaz no puede continuar.\n"
            "Gracias por intentarlo."
        )

    else:
        return (
            "SISTEMA: Proceso completado.\n"
            "Has respondido todas las preguntas.\n"
            "Gracias por participar."
        )
