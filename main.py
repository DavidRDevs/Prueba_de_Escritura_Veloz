"""La idea de este proyecto es crear un programa que evalúe cuan rápido puedes escribir una
    oración de manera precisa."""

from tkinter import Tk
from tkinter import ttk
import random
import timeit


class CronometrarEntradaDeTexto:
    """Inicializa la clase Cronometrar_Entrada_De_Texto."""

    def __init__(self, windows):
        """
        Parameters:
        ventana (tkinter.Tk): La ventana principal de la aplicación.
        """
        self.ventana = windows
        self.frases = [
            "El secreto de la felicidad es querer lo que se hace.",
            "El éxito es ir de fracaso en fracaso sin perder la fe.",
            "La grandeza no se mide por triunfos, sino por caídas.",
            "Ama lo que haces para hacer un gran trabajo.",
            "La vida es cambio, elige sabiamente tu crecimiento.",
            "La vida es una sucesión de lecciones aprendidas.",
            "Arriesga para no conformarte con lo ordinario.",
            "No juzgues por lo que cosechas, sino por lo que siembras.",
            "No sobrevive la especie más fuerte, sino la más adaptable.",
            "Nuestra gloria está en levantarnos tras cada caída.",
        ]
        self.resultado = ""
        self.iniciado = False
        self.start_time = 0.0
        self.ventana.title("Test de escritura")
        self.crear_ventana()

    def tiempo_inicio(self, event):
        """
        Registra el tiempo de inicio del cronómetro al comenzar a escribir.
        """
        if not self.iniciado:
            self.start_time = timeit.default_timer()
            self.iniciado = True
            self.entrada_texto.bind("<Return>", self.tiempo_fin)

    def calcular_precision(self):
        """
        Calcula la precisión de la escritura en relación con la frase aleatoria.

        Returns:
        tuple: Una tupla que contiene la precisión (en porcentaje) y la cantidad de errores.
        """
        frase = (self.frase_aleatoria.replace(" ", "")).lower()
        tipeo = self.entrada_texto.get().replace(" ", "").lower()

        caracteres_correctos = sum(1 for original, entrada in zip(
            frase, tipeo) if original == entrada)

        precision = (caracteres_correctos / len(frase)) * 100
        errores = len(frase) - caracteres_correctos

        return round(precision, 2), errores

    def tiempo_fin(self, event):
        """
        Registra el tiempo final y muestra los resultados al finalizar la escritura.
        """
        end_time = timeit.default_timer()
        texto = self.entrada_texto.get()
        numero_caracteres = len(texto.replace(" ", ""))
        tiempo_total = end_time - self.start_time
        precision, errores = self.calcular_precision()
        numero_palabras = (len(texto.split()) / tiempo_total) * 60

        self.resultado = numero_caracteres / tiempo_total
        mensaje = f"""
            Tiempo total:{round(tiempo_total, 2)} segs.
            Letras promedio: {
            round(self.resultado, 2)} x seg.
            Palabras por minuto: {round(numero_palabras, 2)}
            precision: {precision}%
            Errores encontrados: {errores}
"""

        ttk.Label(self.ventana, text=mensaje,
                  font=("Helvetica", 15)).grid(column=0, row=1)

    def crear_ventana(self):
        """
        Crea la interfaz gráfica de la aplicación.
        """
        self.ventana = ttk.Frame(self.ventana, padding=10)

        self.ventana.grid()

        self.frase_aleatoria = self.frases[random.randint(
            0, len(self.frases)-1)]
        ttk.Label(self.ventana,
                  text="Evalúe cuan rápido puede escribir una oración de manera precisa.:\n").grid(
            column=0, row=0)

        ttk.Label(self.ventana, text=self.frase_aleatoria).grid(
            column=0, row=2)

        self.entrada_texto = ttk.Entry(self.ventana, font="Arial")
        self.entrada_texto.grid(column=0, row=3)
        # Detecta cuando se presiona una tecla

        self.entrada_texto.bind("<Key>", self.tiempo_inicio)

        ttk.Label(self.ventana, text="Pulsar ENTER al terminar").grid(
            column=0, row=4)

        self.ventana.mainloop()


if __name__ == "__main__":
    ventana = Tk()
    app = CronometrarEntradaDeTexto(ventana)
    ventana.mainloop()
