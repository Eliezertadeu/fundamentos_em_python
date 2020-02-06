class Televisao:
    def __init__(self):
        self.ligado = False
        self.canal = 5
    def power(self):
        if self.ligado:
            self.ligado = False
        else:
            self.ligado = True

    def aumenta_canal(self):
        self.canal+=1

    def diminui_canal(self):
        self.canal-=1