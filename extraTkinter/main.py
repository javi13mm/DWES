from loading_window import LoadingWindow
from difficulty_window import DifficultyWindow
from game_window import GameWindow

if __name__ == "__main__":
    # Ventana de descarga de imágenes del ahorcado y json de palabras:
    app1 = LoadingWindow()
    while True:
        # Ventana de selección de dificultad:
        app2 = DifficultyWindow()
        if app2.choice != "salir":
            # Ventana de juego:
            app3 = GameWindow(app2.choice, app1.images, app1.palabras_json)
        else:
            break