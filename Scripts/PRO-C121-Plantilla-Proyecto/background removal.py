# Importar cv2 para capturar el video.
import cv2

import numpy as np

# Establecer el índice de cámara como 0.
camera = cv2.VideoCapture(0)

# Establecer el ancho y altura del cuadro como 640 X 480.
camera.set(3 , 640)
camera.set(4 , 480)

# Cargar la imagen de la montaña.
mountain = cv2.imread('mount everest.jpg')

# Ajustar el tamaño de la imagen de la montaña a 640 X 480.


while True:

    # Leer el cuadro desde la cámara establecida.
    status , frame = camera.read()

    # Si obtenemos el cuadro exitosamente.
    if status:

        # Lo volteamos.
        frame = cv2.flip(frame , 1)

        # Convertir la imagen a RGB para un procesamiento sencillo.
        frame_rgb = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)

        # Crear límites.
        lower_bound = np.array([])
        upper_bound = np.array([])

        # Poner límites a la imagen.

        # Invertir la máscara.

        # Operación de bit a bit y operación para extraer el primer plano / persona.

        # Imagen final.

        # Mostrar la imagen final.
        cv2.imshow('frame' , frame)

        # Esperar 1ms antes de mostrar otro cuadro.
        code = cv2.waitKey(1)
        if code  ==  32:
            break

# Soltar la cámara y cerrar todas las ventanas abiertas.
camera.release()
cv2.destroyAllWindows()
