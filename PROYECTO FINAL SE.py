# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 12:22:09 2024

@author: isisa
"""
class ExpertSystem:
    def __init__(self):
        self.saludo()

    def saludo(self):
        print("¡Bienvenido al sistema experto de recomendaciones de productos!")
        self.seleccionar_categoria()

    def seleccionar_categoria(self):
        categorias = ["carros", "celulares", "viajes", "casas"]
        print("¿Qué categoría deseas buscar datos?")
        for i, categoria in enumerate(categorias):
            print(f"{i+1}) {categoria.capitalize()}")
        opcion = int(input("Selecciona una opción (1-4): "))
        if opcion == 2:
            self.seleccionar_caracteristicas_celular()

    def seleccionar_caracteristicas_celular(self):
        caracteristicas = {
            "procesador": ["Procesadores básicos", "Procesadores de rendimiento medio", "Procesadores de alto rendimiento"],
            "camara": ["Cámaras de calidad media", "Cámaras de buena calidad", "Cámaras de alta resolución y múltiples lentes"],
            "pantalla": ["Pantalla de resolución estándar", "Pantallas de alta resolución", "Pantallas de alta definición con tecnologías avanzadas (como OLED o AMOLED)"],
            "almacenamiento": ["Menor capacidad de almacenamiento", "Mayor capacidad de almacenamiento", "Gran capacidad de almacenamiento"]
        }
        seleccion = {}
        for caracteristica, opciones in caracteristicas.items():
            print(f"Selecciona la {caracteristica}:")
            for i, opcion in enumerate(opciones):
                print(f"{i+1}) {opcion}")
            seleccion[caracteristica] = int(input("Selecciona una opción (1-3): ")) - 1

        print("¿Cuál es tu presupuesto para gastar en el celular?")
        print("1) Económico (entre $1,720 y $5,160 MXN)")
        print("2) Gama media (entre $5,160 y $10,320 MXN)")
        print("3) Gama alta (desde $10,320 MXN en adelante)")
        presupuesto = int(input("Selecciona una opción (1-3): ")) - 1

        self.recomendar_celular(seleccion, presupuesto)

    def recomendar_celular(self, seleccion, presupuesto):
        puntajes = {
            "económico": 0,
            "gama media": 0,
            "gama alta": 0
        }

        if seleccion["procesador"] == 0:
            puntajes["económico"] += 1
        elif seleccion["procesador"] == 1:
            puntajes["gama media"] += 1
        else:
            puntajes["gama alta"] += 1

        if seleccion["camara"] == 0:
            puntajes["económico"] += 1
        elif seleccion["camara"] == 1:
            puntajes["gama media"] += 1
        else:
            puntajes["gama alta"] += 1

        if seleccion["pantalla"] == 0:
            puntajes["económico"] += 1
        elif seleccion["pantalla"] == 1:
            puntajes["gama media"] += 1
        else:
            puntajes["gama alta"] += 1

        if seleccion["almacenamiento"] == 0:
            puntajes["económico"] += 1
        elif seleccion["almacenamiento"] == 1:
            puntajes["gama media"] += 1
        else:
            puntajes["gama alta"] += 1

        if presupuesto == 0:
            puntajes["económico"] += 1
        elif presupuesto == 1:
            puntajes["gama media"] += 1
        else:
            puntajes["gama alta"] += 1

        max_puntaje = max(puntajes, key=puntajes.get)

        if max_puntaje == "económico":
            self.mostrar_recomendaciones_economicas()
        elif max_puntaje == "gama media":
            self.mostrar_recomendaciones_gama_media()
        else:
            self.mostrar_recomendaciones_gama_alta()

    def mostrar_recomendaciones_economicas(self):
        celulares = [
            "Xiaomi Redmi 9A\nProcesador MediaTek Helio G25\nPantalla HD+ de 6.53 pulgadas\nCámara trasera de 13 MP\nBatería de 5000 mAh",
            "Samsung Galaxy A03s\nProcesador MediaTek Helio P35\nPantalla HD+ de 6.5 pulgadas\nCámara triple de 13 MP + 2 MP + 2 MP\nBatería de 5000 mAh",
            "Motorola Moto E7\nProcesador MediaTek Helio G25\nPantalla HD+ de 6.5 pulgadas\nCámara dual de 48 MP + 2 MP\nBatería de 4000 mAh",
            "Realme C11\nProcesador MediaTek Helio G35\nPantalla HD+ de 6.5 pulgadas\nCámara dual de 13 MP + 2 MP\nBatería de 5000 mAh",
            "Nokia C20\nProcesador Unisoc SC9863A\nPantalla HD+ de 6.5 pulgadas\nCámara de 5 MP\nBatería de 3000 mAh"
        ]
        print("Recomendaciones de celulares económicos:")
        for celular in celulares:
            print(f"\n{celular}")
        print("\nLos celulares económicos suelen ser adecuados para usuarios con necesidades básicas como llamadas, mensajes, navegación por internet y uso de aplicaciones simples.")
        self.ver_comentarios(celulares)

    def mostrar_recomendaciones_gama_media(self):
        celulares = [
            "Xiaomi Redmi Note 10\nProcesador Qualcomm Snapdragon 678\nPantalla AMOLED FHD+ de 6.43 pulgadas\nCámara cuádruple de 48 MP + 8 MP + 2 MP + 2 MP\nBatería de 5000 mAh",
            "Samsung Galaxy A32\nProcesador MediaTek Helio G80\nPantalla AMOLED FHD+ de 6.4 pulgadas\nCámara cuádruple de 64 MP + 8 MP + 5 MP + 5 MP\nBatería de 5000 mAh",
            "Motorola Moto G60\nProcesador Qualcomm Snapdragon 732G\nPantalla FHD+ de 6.8 pulgadas\nCámara triple de 108 MP + 8 MP + 2 MP\nBatería de 6000 mAh",
            "Realme 8\nProcesador MediaTek Helio G95\nPantalla Super AMOLED FHD+ de 6.4 pulgadas\nCámara cuádruple de 64 MP + 8 MP + 2 MP + 2 MP\nBatería de 5000 mAh",
            "Nokia X10\nProcesador Qualcomm Snapdragon 480\nPantalla FHD+ de 6.67 pulgadas\nCámara cuádruple de 48 MP + 5 MP + 2 MP + 2 MP\nBatería de 4470 mAh"
        ]
        print("Recomendaciones de celulares de gama media:")
        for celular in celulares:
            print(f"\n{celular}")
        print("\nLos celulares de gama media suelen ofrecer un buen equilibrio entre precio y prestaciones, siendo adecuados para la mayoría de los usuarios, incluyendo aquellos que utilizan aplicaciones más exigentes y juegos móviles.")
        self.ver_comentarios(celulares)

    def mostrar_recomendaciones_gama_alta(self):
        celulares = [
            "Apple iPhone 13\nProcesador A15 Bionic\nPantalla Super Retina XDR OLED de 6.1 pulgadas\nCámara dual de 12 MP + 12 MP\nBatería con carga rápida y MagSafe",
            "Samsung Galaxy S21 Ultra\nProcesador Exynos 2100 / Snapdragon 888\nPantalla Dynamic AMOLED 2X de 6.8 pulgadas\nCámara cuádruple de 108 MP + 10 MP + 10 MP + 12 MP\nBatería de 5000 mAh",
            "Google Pixel 6 Pro\nProcesador Google Tensor\nPantalla AMOLED de 6.71 pulgadas\nCámara triple de 50 MP + 48 MP + 12 MP\nBatería de 5000 mAh",
            "OnePlus 9 Pro\nProcesador Qualcomm Snapdragon 888\nPantalla Fluid AMOLED de 6.7 pulgadas\nCámara cuádruple de 48 MP + 50 MP + 8 MP + 2 MP\nBatería de 4500 mAh",
            "Xiaomi Mi 11 Ultra\nProcesador Qualcomm Snapdragon 888\nPantalla AMOLED de 6.81 pulgadas\nCámara triple de 50 MP + 48 MP + 48 MP\nBatería de 5000 mAh"
        ]
        print("Recomendaciones de celulares de gama alta:")
        for celular in celulares:
            print(f"\n{celular}")
        print("\nLos celulares de gama alta suelen incluir características premium como resistencia al agua, carga inalámbrica, y otros extras. Son ideales para usuarios que buscan el mejor rendimiento y las últimas innovaciones tecnológicas.")
        self.ver_comentarios(celulares)

    def ver_comentarios(self, celulares):
        print("\n¿Deseas ver comentarios de algunos de los celulares recomendados? (si/no)")
        respuesta = input().lower()
        if respuesta == "si":
            print("Selecciona el número del celular del cual deseas ver comentarios:")
            for i, celular in enumerate(celulares):
                print(f"{i+1}) {celular.split()[0]} {celular.split()[1]}")
            opcion = int(input("Selecciona una opción (1-5): ")) - 1
            self.mostrar_comentarios(opcion)
        else:
            self.despedida()

    def mostrar_comentarios(self, opcion):
        comentarios = [
            ["Excelente relación calidad-precio", "Buena duración de la batería", "Cámara aceptable para el precio", "Rendimiento fluido en tareas básicas", "Diseño atractivo y cómodo"],
            ["Pantalla de gran calidad", "Rápido y eficiente", "Cámara sobresaliente", "Buena duración de batería", "Interfaz de usuario intuitiva"],
            ["Calidad de construcción premium", "Rendimiento excepcional", "Cámara de nivel profesional", "Pantalla impresionante", "Funcionalidades innovadoras"]
        ]
        print("Comentarios sobre el celular seleccionado:")
        for comentario in comentarios[opcion % 3]:
            print(f"- {comentario}")
        self.despedida()

    def despedida(self):
        print("¡Gracias por usar el sistema experto! ¡Hasta la próxima!")

if __name__ == "__main__":
    ExpertSystem()
