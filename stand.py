class Stand:
    def __init__(self, codice, superficie, padiglione, prezzoBase):
        self.codice = codice
        self.superficie = superficie
        self.padiglione = padiglione
        self.prezzoBase = prezzoBase

    def __str__(self):
        return f'{self.codice}, {self.superficie}, {self.padiglione}, {self.prezzoBase} '

class StandStandard (Stand)
    def __init__(self, codice, superficie, padiglione, prezzoBase):
        super().__init__(codice, superficie, padiglione, prezzoBase)

class StandPreseExtra (Stand):
    def __init__(self, codice, superficie, padiglione, prezzoBase, preseExtra):
        super().__init__(self, codice, superficie, padiglione, prezzoBase)
        self.preseExtra = preseExtra

    def __str__(self):
        return f'{super().__str__()} {self.preseExtra}'

class StandPremium (Stand):
    def __init__(self, codice, superficie, padiglione, prezzoBase, posizione):
        super().__init__(self, codice, superficie, padiglione, prezzoBase)
        self.posizione = posizione

    def __str__(self):
        return f'{super().__str__()} {self.posizione}'