import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QDateEdit
from PyQt5.QtCore import QDate, Qt

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Membuat tata letak utama
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        # Membuat tata letak untuk bagian kanan
        right_layout = QVBoxLayout()
        main_layout.addLayout(right_layout)

        # Membuat label dan text edit untuk menampilkan catatan
        saved_text_label = QLabel("Catatan:")
        self.saved_text_edit = QTextEdit()
        self.saved_text_edit.setReadOnly(True)
        right_layout.addWidget(saved_text_label)
        right_layout.addWidget(self.saved_text_edit)

        # Membuat tata letak untuk bagian kiri
        left_layout = QVBoxLayout()
        main_layout.addLayout(left_layout)

        # Membuat label dan line edit untuk memasukkan catatan
        text_label = QLabel("Masukkan Catatan:")
        self.text_edit = QLineEdit()
        left_layout.addWidget(text_label)
        left_layout.addWidget(self.text_edit)

        # Membuat date edit untuk memilih tanggal
        date_label = QLabel("Pilih tanggal:")
        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDate(QDate.currentDate())  # Untuk set tanggal default ke tanggal sekarang
        left_layout.addWidget(date_label)
        left_layout.addWidget(self.date_edit)

        # Membuat tombol untuk menyimpan catatan
        save_button = QPushButton("Simpan")
        save_button.clicked.connect(self.saveText)
        left_layout.addWidget(save_button)

        # Menampilkan program CatatanKu
        self.setWindowTitle("CatatanKu")
        self.setGeometry(100, 100, 400, 300)
        self.show()

    def saveText(self):
        # Mengambil teks dari tempat kita memasukkan catatan [baris 30]
        text = self.text_edit.text()

        # Mengambil tanggal dari tempat kita mengambil tanggal [baris 36]
        date = self.date_edit.date().toString("dd/MM/yyyy")

        # Menyimpan catatan dan tanggal untuk ditampilkan
        self.saved_text_edit.append(f"Catatan: {text}\nTanggal: {date}\n")

        # Mengosongkan tempat memasukkan catatan setelah catatan dimasukkan ke data
        self.text_edit.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    sys.exit(app.exec_())