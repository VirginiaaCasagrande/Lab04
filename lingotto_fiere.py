from stand import Stand, StandStandard, StandPreseExtra,StandPremium
from espositore import Espositore


class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome=nome
        self.elencoStand=[]
        self.elencoEspositori=[]

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome=nome
        # TODO

    """Aggiungere setter e getter se necessari"""
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""

        try:
            with open(file_path, 'r') as file:
                righe = file.readlines()

                for riga in righe:
                    campi=riga.strip().split(',')

                    if campi[0].startswith('ST'):
                        if len(campi) == 4:
                            stand=StandStandard(campi[0], float(campi[1]), int(campi[2]), campi[3])
                            self.elencoStand.append(stand)

                        elif len(campi) ==5 :
                            if campi[4].isdigit():
                                stand=StandPreseExtra(campi[0], float(campi[1]), int(campi[2]), float(campi[3]), int(campi[4]))
                                self.elencoStand.append(stand)
                            else:
                                stand=StandPremium(campi[0], float(campi[1]), int(campi[2]), float(campi[3]), campi[4])
                                self.elencoStand.append(stand)

                    elif campi[0].startswith('ES'):
                        espositore=Espositore(campi[0], campi[1], campi[2])
                        self.elencoEspositori.append(espositore)

        except FileNotFoundError:
            raise


    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""

        stand_trovato = None
        for stand in self.elencoStand:
            if stand.codice == codice_stand:
                stand_trovato = stand
                break
        if stand_trovato is None:
            raise ValueError ('Il codice non corrisponde a nessuno stand')

        espositore_trovato = None
        for espositore in self.elencoEspositori:
            if espositore.codice == codice_espositore:
                espositore_trovato = espositore
                break

        if espositore_trovato is None:
            raise ValueError ('Il codice non corrisponde a nessun espositore')

        if not stand_trovato.disponibile:
            raise ValueError ('Lo stand non è disponibile')

        for stand in self.elencoStand:
            if stand.espositore == espositore_trovato:
                raise ValueError ('L\'espositore è già associato a un altro stand')

        stand_trovato.espositore = espositore_trovato
        stand_trovato.disponibile = False


    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
