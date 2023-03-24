class Sepeda:
    def __init__(self, jenis, gear, rantai, ban, cakram, velg, rem, pedal, rangka):
        self.name = jenis
        self.gear = gear
        self.rantai = rantai
        self.ban = ban
        self.cakram = cakram
        self.velg = velg
        self.rem = rem
        self.pedal = pedal
        self.rangka = rangka
    
    def berjalan(self):
        print(f'sepeda {self.name} ini berjalan')
    def berhenti(self):
        print(f'sepeda {self.name} ini berhenti')
    def rusak(self):
        print(f'sepeda {self.name} ini rusak')
    def diperbaiki(self):
        print(f'sepeda {self.name} ini diperbaiki')

bmx = Sepeda('bmx', 'dol trap', 'besi', 'karet', '', 'jari-jari', '', 'manual', 'besi')
gunung = Sepeda('gunung', 'normal', 'besi', 'karet', 'cakram', 'jari-jari', 'cakram', 'transmisi', 'besi')
balap = Sepeda('balap', 'torpedo', 'besi', 'cacing', '', 'bintang', 'manual', 'manual', 'besi')

print(f'sepeda bmx memiliki gear {bmx.gear}')
print(f'sepeda gunung memiliki gear {gunung.gear}')
print(f'sepeda balap memiliki gear {balap.gear}')
print('')

bmx.berjalan()
bmx.rusak()
print('')

gunung.berjalan()
gunung.berhenti()
gunung.rusak()
print('')

balap.berjalan()
balap.berhenti()