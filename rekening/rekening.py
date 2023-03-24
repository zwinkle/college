import os, numbers

class Rekening():
    # method init (method otomatis yang langsung berjalan)
    def __init__(self, nama_bank, no_rekening = int, pin_pengguna = int, saldo_pengguna = int):
        # nama bank ditampung pada self.bank
        self.bank = nama_bank

        # mengecek apakah nomor rekening berupa numerik
        chck_no = isinstance(no_rekening, numbers.Number)
        # jika iya
        if chck_no == True:
            if len(str(no_rekening)) < 5:
                os.system('cls')
                # print jika kurang dari 5 angka
                print('Nomor Rekening harus 5 angka!')
            elif len(str(no_rekening)) > 5:
                os.system('cls')
                # print jika lebih dari 5 angka
                print('Nomor Rekening harus 5 angka!')
            else:
                # jika tidak ada kesalahan sama sekali, nomor rekening ditampung pada self.no
                self.no = no_rekening
        # jika tidak
        elif chck_no == False:
            os.system('cls')
            # print jika memasukkan selain angka
            print('Nomor Rekening hanya berisi angka!')

        # mengecek apakah nomor PIN berupa numerik
        chck_pin = isinstance(pin_pengguna, numbers.Number)
        # jika iya
        if chck_pin == True:
            if len(str(pin_pengguna)) < 4:
                os.system('cls')
                # print jika PIN kurang dari 4 angka
                print('PIN harus 4 angka!')
            elif len(str(pin_pengguna)) > 4:
                os.system('cls')
                # print jika PIN lebih dari 4 angka
                print('PIN harus 4 angka!')
            else:
                # jika tidak ada kesalahan sama sekali, PIN ditampung pada self.pin
                self.pin = pin_pengguna
        # jika tidak
        elif chck_pin == False:
            os.system('cls')
            print('PIN Rekening hanya berisi angka!')

        # mengecek apakah saldo berupa numerik
        chck_saldo = isinstance(saldo_pengguna, numbers.Number)
        if chck_saldo == True:
            # jika iya, saldo ditampung pada self.saldo
            self.saldo = saldo_pengguna
        elif chck_saldo == False:
            os.system('cls')
            # print jika saldo tidak berupa numerik
            print('Saldo hanya berisi angka!')
    
    # method login
    def login(self, warn = False):
        print('Apakah anda ingin login dengan nomor rekening :')
        print(f'{self.no}')
        print('')
        # mengecek apakah parameter warn True/False dan menampilkan pesan jika memasukkan pilihan selain yang disediakan/tersedia
        if warn == True:
            print('Masukkan pilihan yang tersedia!')
            print('')
        # mengecek inputan pilihan
        conf = input('Y/n : ')
        # jika iya
        if conf == 'y' or conf == 'Y':
            os.system('cls')
            # lakukan method conf_pin (konfirmasi PIN)
            self.conf_pin()
        # jika tidak
        elif conf == 'n' or conf == 'N':
            os.system('cls')
            # akan keluar aplikasi
            print(f'Terimakasih telah menggunakan layanan {self.bank}')
        # jika memasukkan pilihan selain yang disediakan/tersedia
        else:
            os.system('cls')
            # parameter warn akan menjadi True
            self.login(warn = True)

    # method conf_pin
    def conf_pin(self, warn = False, warn2 = False):
        # mengecek apakah parameter warn True/False dan menampilkan pesan jika memasukkan PIN yang salah
        if warn == True:
            print('Kode PIN anda salah!')
            print('')
        # mengecek apakah parameter warn2 True/False dan menampilkan pesan jika memasukkan PIN selain angka
        if warn2 == True:
            print('Kode PIN harus angka!')
            print('')
        # mengecek inputan pilihan (PIN)
        pin = input('Masukkan pin : ')
        # mengecek apakah PIN berupa numerik
        ispin = pin.isnumeric()
        # jika iya
        if ispin == True:
            # membuat PIN menjadi integer
            intpin = int(pin)
            # mengecek apakah PIN sama dengan PIN yang dibuat
            if intpin == self.pin:
                os.system('cls')
                # jika iya, lakukan method menu (masuk ke menu)
                self.menu()
            elif intpin != self.pin:
                os.system('cls')
                # jika tidak, parameter warn akan menjadi True
                self.conf_pin(warn = True)
        # jika tidak (jika PIN tidak berupa numerik)
        elif ispin == False:
            os.system('cls')
            # parameter warn2 akan menjadi True
            self.conf_pin(warn2 = True)

    # method menu
    def menu(self, warn = False, warn2 = False):
        print('Piih menu : ')
        print('')
        print('1. Info Rekening')
        print('2. Info Saldo')
        print('3. Transfer')
        print('4. Keluar')
        print('')
        # mengecek apakah parameter warn True/False dan menampilkan pesan jika memasukkan pilihan selain yang disediakan/tersedia
        if warn == True:
            print('Masukkan pilihan yang tersedia!')
            print('')
        # mengecek apakah parameter warn2 True/False dan menampilkan pesan jika memasukkan pilihan selain yang disediakan/tersedia (berupa huruf)
        if warn2 == True:
            print('Masukkan angka saja!')
            print('')
        # mengecek inputan pilihan
        menu = input('Masukkan nomor menu : ')
        # mengecek apakah pilihan berupa numerik
        ismenu = menu.isnumeric()
        # jika iya
        if ismenu == True:
            # dan jika inputan pilihan berupa angka 1
            if menu == '1':
                os.system('cls')
                # lakukan method cek_akun (untuk mengecek nomor rekening)
                self.cek_akun()
            # dan jika inputan pilihan berupa angka 2
            elif menu == '2':
                os.system('cls')
                # lakukan method cek_saldo (untuk mengecek saldo)
                self.cek_saldo()
            # dan jika inputan pilihan berupa angka 3
            elif menu == '3':
                os.system('cls')
                # lakukan method tf (untuk melakukan transfer)
                self.tf()
            # dan jika inputan pilihan berupa angka 4
            elif menu == '4':
                os.system('cls')
                # akan keluar dari aplikasi
                print(f'Terimakasih telah menggunakan layanan {self.bank}')
            # dan jika inputan pilihan selain yang disediakan/tersedia (berupa angka)
            else:
                os.system('cls')
                # parameter warn akan menjadi True
                self.menu(warn = True)
        # jika tidak (jika pilihan tidak berupa numerik)
        elif ismenu == False:
            os.system('cls')
            # parameter warn2 akan menjadi True
            self.menu(warn2 = True)

    # method cek_akun
    def cek_akun(self, warn = False):
        print('DETAIL INFORMASI REKENING ANDA ADA DIBAWAH INI')
        print(f'Nomor Rekening : {self.no}')
        print(f'Layanan yang anda gunakan adalah : {self.bank}')
        print('')
        # mengecek apakah parameter warn True/False dan menampilkan pesan jika memasukkan pilihan selain yang disediakan/tersedia
        if warn == True:
            print('Masukkan pilihan yang tersedia!')
            print('')
        # mengecek inputan pilihan
        back = input('Apakah anda ingin kembali? Y/n :')
        # jika iya
        if back == 'y' or back == 'Y':
            os.system('cls')
            # lakukan method menu (kembali ke menu)
            self.menu()
        # jika tidak
        elif back == 'n' or back == 'N':
            os.system('cls')
            # lakukan method cek_akun (tetap pada halaman ini)
            self.cek_akun()
        # jika memasukkan pilihan selain yang disediakan/tersedia
        else:
            os.system('cls')
            # parameter warn akan menjadi True
            self.cek_akun(True)

    # method cek_saldo
    def cek_saldo(self, warn = False):
        print('DETAIL INFORMASI SALDO ANDA ADA DIBAWAH INI')
        print(f'Saldo Rekening : {self.saldo}')
        print(f'Layanan yang anda gunakan adalah : {self.bank}')
        print('')
        # mengecek apakah parameter warn True/False dan menampilkan pesan jika memasukkan pilihan selain yang disediakan/tersedia
        if warn == True:
            print('Masukkan pilihan yang tersedia!')
            print('')
        # mengecek inputan pilihan
        back = input('Apakah anda ingin kembali? Y/n :')
        # jika iya
        if back == 'y' or back == 'Y':
            os.system('cls')
            # lakukan method menu (kembali ke menu)
            self.menu()
        # jika tidak
        elif back == 'n' or back == 'N':
            os.system('cls')
            # lakukan method cek_saldo (tetap pada halaman ini)
            self.cek_saldo()
        # jika memasukkan pilihan selain yang disediakan/tersedia
        else:
            os.system('cls')
            # parameter warn akan menjadi True
            self.cek_saldo(True)

    # method tf
    def tf(self, warnMin = False, warnMax = False, warnTrgt = False):
        # mengecek apakah parameter warnMin True/False dan menampilkan pesan jika memasukkan nomor rekening tujuan kurang dari 5 angka
        if warnMin == True:
            print('Nomor tujuan harus 5 angka!')
            print('')
        # mengecek apakah parameter warnMin True/False dan menampilkan pesan jika memasukkan nomor rekening tujuan lebih dari 5 angka
        if warnMax == True:
            print('Nomor tujuan harus 5 angka!')
            print('')
        # mengecek apakah parameter warnMin True/False dan menampilkan pesan jika memasukkan nomor rekening tidak berupa numerik (berupa huruf)
        if warnTrgt == True:
            print('Nomor tujuan hanya berisi angka!')
            print('')
        # mengecek inputan pilihan (nomor rekening tujuan)
        trgt = input('Masukkan nomor tujuan : ')
        # mengecek apakah nomor rekening tujuan berupa numerik
        istrgt = trgt.isnumeric()
        # jika iya
        if istrgt == True:
            # membuat nomor rekening tujuan menjadi integer
            inttrgt = int(trgt)
            # mengecek apakah panjang dari nomor rekening tujuan kurang dari 5
            if len(str(inttrgt)) < 5:
                os.system('cls')
                # jika iya, parameter warnMin akan menjadi True
                self.tf(warnMin = True)
            # mengecek apakah panjang dari nomor rekening tujuan lebih dari 5
            elif len(str(inttrgt)) > 5:
                os.system('cls')
                # jika iya, parameter warnMax akan menjadi True
                self.tf(warnMax = True)
            # jika tidak ada kesalahan sama sekali
            else:
                os.system('cls')
                # lakukan method tf2 dan memberi value pada parameter no_trgt sama dengan inttrgt (nomor rekening tujuan disamakan dengan nomor rekening tujuan yang telah diinput dan dioper ke method tf2 sehingga bisa digunakan)
                self.tf2(no_trgt = inttrgt)
        # jika tidak (jika nomor rekening tujuan tidak berupa numerik)
        elif istrgt == False:
            os.system('cls')
            # parameter warnTrgt akan menjadi True
            self.tf(warnTrgt = True)

    #  method tf2
    def tf2(self, no_trgt, jml = 0, warnUn = False, warnNum = False, warnBtn = False, scs = False):
        trgt = no_trgt
        # 
        if warnUn == True:
            print('Jumlah uang yang ingin ditransfer melebihi saldo/tidak cukup!')
            print('')
        # 
        if warnNum == True:
            print('Masukkan angka saja pada jumlah uang yang ingin ditransfer!')
            print('')
        # 
        if scs == True:
            print(f'Transfer ke nomor {trgt} sebesar {jml} berhasil!')
            # 
            if warnBtn == True:
                print('Masukkan pilihan yang tersedia!')
                print('')
            # 
            chck_again = input('Apakah anda ingin transfer lagi? Y/n : ')
            # 
            if chck_again == 'Y' or chck_again == 'y':
                os.system('cls')
                # 
                self.tf2(no_trgt = trgt)
            #
            elif chck_again == 'N' or chck_again == 'n':
                os.system('cls')
                self.menu()
            # 
            else:
                os.system('cls')
                # 
                self.tf2(no_trgt = trgt, warnBtn = True, scs = True)
        # 
        if scs == False:
            print(f'Saldo anda sekarang adalah : {self.saldo}')
            nom = input('Masukkan jumlah uang yang ingin ditransfer : ')
            # 
            isnom = nom.isnumeric()
            # 
            if isnom == True:
                # 
                intnom = int(nom)
                # 
                if intnom > self.saldo:
                    os.system('cls')
                    # 
                    self.tf2(no_trgt = trgt, jml = intnom, warnUn = True)
                # 
                else:
                    # 
                    self.saldo = self.saldo-intnom
                    os.system('cls')
                    # 
                    self.tf2(no_trgt = trgt, jml = nom, scs = True)
            # 
            elif isnom == False:
                os.system('cls')
                # 
                self.tf2(no_trgt = trgt, jml = nom, warnNum = True)

os.system('cls')
PenggunaSatu = Rekening('BRI', 55555, 1234, 200000)
PenggunaSatu.login()
PenggunaDua = Rekening('BSI', 88888, 5678, 100000)
PenggunaDua.login()