class Stand:
    def __init__(self, codice, superficie, padiglione, prezzo_base):
        self.codice = codice
        self.superficie = superficie
        self.padiglione = padiglione
        self.prezzo_base = prezzo_base
        self.disponibile = True
        self.espositore = None

    def __str__(self):
        return f'{self.codice}, {self.superficie}, {self.padiglione}, {self.prezzo_base}'

    def __lt__(self, other):
        if not isinstance(other, Stand):
            return NotImplemented
        return self.calcola_prezzo() < other.calcola_prezzo()

class StandStandard(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base):
        super().__init__(codice, superficie, padiglione, prezzo_base)

    def calcola_prezzo(self):
        prezzo_finale=self.prezzo_base
        return prezzo_finale

class StandPreseExtra (Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, prese_extra):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self.prese_extra = prese_extra

    def __str__(self):
        return f'{super().__str__()} {self.prese_extra}'

    def calcola_prezzo(self):
        prezzo_finale= self.prezzo_base * (1+0.07*self.prese_extra)
        return prezzo_finale

class StandPremium (Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, posizione):
        super().__init__( codice, superficie, padiglione, prezzo_base)
        self.posizione = posizione

    def __str__(self):
        return f'{super().__str__()} {self.posizione}'

    def calcola_prezzo(self):
        prezzo_finale=self.prezzo_base * 1.30
        return prezzo_finale
