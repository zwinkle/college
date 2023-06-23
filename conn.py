from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Contoh PyQt5 dan QtSql")

        # Membuat tampilan
        layout = QVBoxLayout()
        self.name_input = QLineEdit()
        self.salary_input = QLineEdit()
        self.add_button = QPushButton("Tambah Data")
        self.add_button.clicked.connect(self.add_data)
        layout.addWidget(QLabel("Nama:"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Gaji:"))
        layout.addWidget(self.salary_input)
        layout.addWidget(self.add_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Membuat koneksi ke database
        print(QSqlDatabase.drivers())
        self.db = QSqlDatabase.addDatabase('QMYSQL')
        self.db.setHostName('localhost')
        self.db.setPort(3306)
        self.db.setDatabaseName('tapbo_db')
        self.db.setUserName('root')
        self.db.setPassword('')

        if self.db.open():
            print("Berhasil terhubung ke database")
        else:
            print("Gagal terhubung ke database:", self.db.lastError().text())

    def add_data(self):
        # Mendapatkan data dari input pengguna
        name = self.name_input.text()
        salary = float(self.salary_input.text())

        # Membuat objek query
        query = QSqlQuery()

        # Menambahkan data ke tabel employees
        query.prepare("INSERT INTO employees (name, salary) VALUES (?, ?)")
        query.addBindValue(name)
        query.addBindValue(salary)
        if query.exec():
            print("Data berhasil ditambahkan")
        else:
            print("Gagal menambahkan data:", query.lastError().text())

        # Mengosongkan input setelah data ditambahkan
        self.name_input.setText("")
        self.salary_input.setText("")

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()