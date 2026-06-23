from Figuras import *

def desenhar_poligono(self, event):
    self.pontos_poligono.append(event.x)
    self.pontos_poligono.append(event.y)

    coordenadas = int(self.menu_poly.get()) * 2

    if len(self.pontos_poligono) < coordenadas:
            return

    figura_atual = Poligono(self.cor_borda.get(), float(self.espessura.get()), self.cor_preenchimento.get(), self.pontos_poligono.copy())
    self.figuras.append(figura_atual)
    self.pontos_poligono.clear()
    self.redesenhar()
def redesenhar(self):

    self.canvas.delete("all")

    for figura_atual in self.figuras:
        figura_atual.desenhar(self.canvas)

def limpar(self):

    self.figuras.clear()
    self.pontos_poligono.clear()

    self.canvas.delete("all")