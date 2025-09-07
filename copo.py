import turtle
import math

def curva_koch(t, longitud, nivel):
    """
    Dibuja una curva de Koch recursivamente
    
    Args:
        t: objeto turtle
        longitud: longitud del segmento
        nivel: nivel de recursión (0 = línea recta)
    """
    if nivel == 0:
        # Caso base: dibuja una línea recta
        t.forward(longitud)
    else:
        # Caso recursivo: dividir en 4 segmentos
        longitud_nueva = longitud / 3
        
        # Primer segmento
        curva_koch(t, longitud_nueva, nivel - 1)
        
        # Girar 60° hacia la izquierda y dibujar segundo segmento
        t.left(60)
        curva_koch(t, longitud_nueva, nivel - 1)
        
        # Girar 120° hacia la derecha y dibujar tercer segmento
        t.right(120)
        curva_koch(t, longitud_nueva, nivel - 1)
        
        # Girar 60° hacia la izquierda y dibujar cuarto segmento
        t.left(60)
        curva_koch(t, longitud_nueva, nivel - 1)

def copo_nieve_koch(t, longitud, nivel):
    """
    Dibuja un copo de nieve de Koch completo (3 curvas de Koch formando un triángulo)
    """
    for i in range(3):
        curva_koch(t, longitud, nivel)
        t.right(120)

def forma_imagen_koch_exacta(t, longitud, nivel):
    """
    Dibuja EXACTAMENTE la forma de tu imagen:
    - Primera curva de Koch COMPLETA
    - PRIMER CUARTO (0.25) de la segunda curva 
    - ÚLTIMO CUARTO (0.25) de la tercera curva
    """
    # 1. Primera curva de Koch COMPLETA
    curva_koch(t, longitud, nivel)
    
    # Girar 120° hacia la derecha para la segunda curva
    t.right(120)
    
    # 2. PRIMER CUARTO de la segunda curva
    dibujar_primer_cuarto_curva_koch(t, longitud, nivel)
    
    # Posicionarnos para el último cuarto de la tercera curva
    posicionarse_para_ultimo_cuarto_tercera_curva(t, longitud, nivel)
    
    # 3. ÚLTIMO CUARTO de la tercera curva
    dibujar_ultimo_cuarto_curva_koch(t, longitud, nivel)

def dibujar_primer_cuarto_curva_koch(t, longitud, nivel):
    """
    Dibuja exactamente el PRIMER CUARTO de una curva de Koch
    (solo el primer segmento de 4)
    """
    if nivel == 0:
        # Caso base: dibuja un cuarto de línea recta
        t.forward(longitud / 4)
    else:
        # Caso recursivo: dibujar solo el primer segmento de los 4
        longitud_nueva = longitud / 3
        
        # Primer segmento (completo) - esto es 1/4 de la curva total
        curva_koch(t, longitud_nueva, nivel - 1)

def dibujar_ultimo_cuarto_curva_koch(t, longitud, nivel):
    """
    Dibuja exactamente el ÚLTIMO CUARTO de una curva de Koch
    (solo el cuarto segmento de 4)
    """
    if nivel == 0:
        # Caso base: dibuja un cuarto de línea recta
        t.forward(longitud / 4)
    else:
        # Caso recursivo: dibujar solo el cuarto segmento de los 4
        longitud_nueva = longitud / 3
        
        # Cuarto segmento (completo) - esto es 1/4 de la curva total
        curva_koch(t, longitud_nueva, nivel - 1)

def posicionarse_para_ultimo_cuarto_tercera_curva(t, longitud, nivel):
    """
    Posiciona la tortuga para empezar a dibujar el ÚLTIMO CUARTO de la tercera curva
    """
    # Desde donde terminamos el primer cuarto de la segunda curva,
    # necesitamos ir al inicio del último cuarto de la tercera curva
    
    # Primero, simular ir al final de la segunda curva (sin dibujar)
    simular_tres_cuartos_restantes_segunda_curva(t, longitud, nivel)
    
    # Girar 120° para orientarnos hacia la tercera curva
    t.right(120)
    
    # Simular los primeros 3 cuartos de la tercera curva (sin dibujar)
    simular_tres_cuartos_curva_koch(t, longitud, nivel)

def simular_tres_cuartos_restantes_segunda_curva(t, longitud, nivel):
    """
    Simula el movimiento de los 3 cuartos restantes de la segunda curva sin dibujar
    (segmentos 2, 3 y 4)
    """
    t.penup()
    
    if nivel == 0:
        # Simular 3/4 de línea recta
        t.forward(3 * longitud / 4)
    else:
        longitud_nueva = longitud / 3
        
        # Simular segundo segmento
        t.left(60)
        simular_curva_koch(t, longitud_nueva, nivel - 1)
        
        # Simular tercer segmento
        t.right(120)
        simular_curva_koch(t, longitud_nueva, nivel - 1)
        
        # Simular cuarto segmento
        t.left(60)
        simular_curva_koch(t, longitud_nueva, nivel - 1)
    
    t.pendown()

def simular_tres_cuartos_curva_koch(t, longitud, nivel):
    """
    Simula los primeros 3 cuartos de una curva de Koch sin dibujar
    (segmentos 1, 2 y 3)
    """
    t.penup()
    
    if nivel == 0:
        # Simular 3/4 de línea recta
        t.forward(3 * longitud / 4)
    else:
        longitud_nueva = longitud / 3
        
        # Simular primer segmento
        simular_curva_koch(t, longitud_nueva, nivel - 1)
        
        # Simular segundo segmento
        t.left(60)
        simular_curva_koch(t, longitud_nueva, nivel - 1)
        
        # Simular tercer segmento
        t.right(120)
        simular_curva_koch(t, longitud_nueva, nivel - 1)
        
        # Preparar orientación para el cuarto segmento
        t.left(60)
    
    t.pendown()

def simular_curva_koch(t, longitud, nivel):
    """
    Simula una curva de Koch completa sin dibujar (solo movimiento)
    """
    if nivel == 0:
        t.forward(longitud)
    else:
        longitud_nueva = longitud / 3
        
        # Simular los 4 segmentos
        simular_curva_koch(t, longitud_nueva, nivel - 1)
        
        t.left(60)
        simular_curva_koch(t, longitud_nueva, nivel - 1)
        
        t.right(120)
        simular_curva_koch(t, longitud_nueva, nivel - 1)
        
        t.left(60)
        simular_curva_koch(t, longitud_nueva, nivel - 1)

def demo_forma_imagen_exacta():
    """
    Copo de nieve de Koch - MITAD
    """
    # Configurar la ventana
    ventana = turtle.Screen()
    ventana.bgcolor("black")
    ventana.title("Mitad del Copo de Nieve de Koch")
    ventana.setup(width=900, height=700)
    
    # Crear y configurar la tortuga
    tortuga = turtle.Turtle()
    tortuga.speed(0)
    tortuga.color("cyan")
    tortuga.pensize(2)
    
    # Dibujar la forma exacta con diferentes niveles de recursión
    niveles = [0, 1, 2, 3, 4]
    longitud_base = 300
    
    for i, nivel in enumerate(niveles):
        # Limpiar la pantalla para cada nueva forma
        if i > 0:
            input(f"Presiona Enter para ver la forma EXACTA de nivel {nivel}...")
            tortuga.clear()
        
        # Posicionar para cada nivel
        tortuga.penup()
        tortuga.goto(-150, 100)
        tortuga.pendown()
        tortuga.setheading(0)
        
        print(f"Dibujando forma EXACTA de tu imagen - Nivel {nivel}")
        print("1 curva completa + 1/4 segunda + 1/4 tercera")
        
        # Cambiar color según el nivel
        colores = ["white", "cyan", "lightblue", "blue", "darkblue"]
        tortuga.color(colores[i])
        
        # Dibujar la forma EXACTA de tu imagen
        forma_imagen_koch_exacta(tortuga, longitud_base, nivel)
    
    print("¡Completado! Haz clic en la ventana para cerrar.")
    ventana.exitonclick()

def demo_interactivo_exacto():
    """
    Versión interactiva para probar diferentes niveles de la forma exacta
    """
    ventana = turtle.Screen()
    ventana.bgcolor("black")
    ventana.title("Forma EXACTA - Modo Interactivo")
    ventana.setup(width=900, height=700)
    
    tortuga = turtle.Turtle()
    tortuga.speed(0)
    tortuga.color("cyan")
    tortuga.pensize(2)
    
    while True:
        try:
            nivel = int(input("Ingresa el nivel de recursión (0-6, o -1 para salir): "))
            
            if nivel == -1:
                break
                
            if nivel < 0 or nivel > 6:
                print("Por favor ingresa un nivel entre 0 y 6")
                continue
            
            # Limpiar y reposicionar
            tortuga.clear()
            tortuga.penup()
            tortuga.goto(-150, 100)
            tortuga.pendown()
            tortuga.setheading(0)
            
            print(f"Dibujando forma EXACTA de nivel {nivel}...")
            print("1 curva completa + 1/4 segunda + 1/4 tercera")
            
            # Cambiar color según el nivel
            colores = ["white", "cyan", "lightblue", "blue", "darkblue", "navy", "midnightblue"]
            tortuga.color(colores[nivel])
            
            forma_imagen_koch_exacta(tortuga, 300, nivel)
            
        except ValueError:
            print("Por favor ingresa un número válido")
        except KeyboardInterrupt:
            break
    
    ventana.bye()

def demo_comparacion():
    """
    Demo que muestra la diferencia entre copo completo y forma exacta
    """
    ventana = turtle.Screen()
    ventana.bgcolor("black")
    ventana.title("Comparación: Copo Completo vs Mitad de Copo")
    ventana.setup(width=1200, height=700)
    
    tortuga = turtle.Turtle()
    tortuga.speed(0)
    tortuga.pensize(2)
    
    nivel = 3  # Nivel fijo para la comparación
    
    # Dibujar copo completo a la izquierda
    tortuga.color("orange")
    tortuga.penup()
    tortuga.goto(-400, 0)
    tortuga.pendown()
    tortuga.setheading(0)
    
    print("Dibujando copo COMPLETO...")
    copo_nieve_koch(tortuga, 200, nivel)
    
    # Dibujar forma exacta a la derecha
    tortuga.color("cyan")
    tortuga.penup()
    tortuga.goto(100, 0)
    tortuga.pendown()
    tortuga.setheading(0)
    
    print("Dibujando forma EXACTA de tu imagen...")
    forma_imagen_koch_exacta(tortuga, 200, nivel)
    
    print("Comparación completada. Clic para cerrar.")
    ventana.exitonclick()

if __name__ == "__main__":
    print("Copo de Nieve de Koch - Forma Exacta Corregida")
    print("="*50)
    print("1. Demo forma EXACTA (1 completa + 1/4 + 1/4)")
    print("2. Modo interactivo forma exacta")
    print("3. Comparación: Copo completo vs Forma exacta")
    
    try:
        opcion = input("Elige una opción (1, 2 o 3): ").strip()
        
        if opcion == "1":
            demo_forma_imagen_exacta()
        elif opcion == "2":
            demo_interactivo_exacto()
        elif opcion == "3":
            demo_comparacion()
        else:
            print("Opción no válida. Ejecutando demo de forma exacta...")
            demo_forma_imagen_exacta()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")