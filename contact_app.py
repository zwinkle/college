import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QListWidget, QApplication
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Daftar Kontak')
        self.setGeometry(200, 200, 400, 300)

        # Membuat koneksi database SQLite
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('contact.sqlite')
        if not self.db.open():
            QMessageBox.critical(self, 'Error', 'Tidak dapat terhubung ke database.')
            sys.exit(1)

        # Membuat tabel kontak jika belum ada 
        query = QSqlQuery()
        query.exec_('CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone TEXT, email TEXT)')

        # Membuat widget utama
        widget = QWidget()
        self.setCentralWidget(widget)

        # Membuat layout utama
        layout = QVBoxLayout()
        widget.setLayout(layout)

        # Membuat label dan inputan
        name_label = QLabel('Nama:')
        self.name_input = QLineEdit()
        phone_label = QLabel('Nomor Telepon:')
        self.phone_input = QLineEdit()
        email_label = QLabel('Email:')
        self.email_input = QLineEdit()

        # Membuat tombol-tombol
        button_layout = QHBoxLayout()
        add_button = QPushButton('Tambah')
        add_button.clicked.connect(self.add_contact)
        update_button = QPushButton('Perbarui')
        update_button.clicked.connect(self.update_contact)
        delete_button = QPushButton('Hapus')
        delete_button.clicked.connect(self.delete_contact)
        button_layout.addWidget(add_button)
        button_layout.addWidget(update_button)
        button_layout.addWidget(delete_button)

        # Menambahkan widget ke dalam layout utama
        layout.addWidget(name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(phone_label)
        layout.addWidget(self.phone_input)
        layout.addWidget(email_label)
        layout.addWidget(self.email_input)
        layout.addLayout(button_layout)

        # Menambahkan daftar kontak
        self.contact_list = QListWidget()
        self.contact_list.itemClicked.connect(self.show_contact)
        layout.addWidget(self.contact_list)
       
        # Memuat daftar kontak dari database
        self.load_contacts()

    def load_contacts(self):
        # Mengambil daftar kontak dari database dan menampilkannya
        query = QSqlQuery()
        query.exec_('SELECT name FROM contacts')
        self.contact_list.clear()
        while query.next():
            name = query.value(0)
            self.contact_list.addItem(name)

    def add_contact(self):
        # Menambahkan kontak baru ke database
        name = self.name_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()
        contact = Contact(name, phone, email)

        query = QSqlQuery()
        query.prepare('INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)')
        query.bindValue(0, name)
        query.bindValue(1, phone)
        query.bindValue(2, email)

        if query.exec_():
            self.load_contacts()
            self.clear_inputs()
            QMessageBox.information(self, 'Info', 'Kontak berhasil ditambahkan.')
        else:
            QMessageBox.warning(self, 'Peringatan', 'Gagal menambahkan kontak.')

    def update_contact(self):
        # Mengupdate kontak yang dipilih di database
        current_item = self.contact_list.currentItem()
        if current_item:
            selected_name = current_item.text()
            name = self.name_input.text()
            phone = self.phone_input.text()
            email = self.email_input.text()
            contact = Contact(name, phone, email)
            query = QSqlQuery() 
            query.prepare('UPDATE contacts SET name=?, phone=?, email=? WHERE name=?') 
            query.bindValue(0, name)
            query.bindValue(1, phone)
            query.bindValue(2, email)
            query.bindValue(3, selected_name)

            if query.exec_():
                self.load_contacts()
                self.clear_inputs()
                QMessageBox.information(self, 'Info', 'Kontak berhasil diperbarui.')
            else:
                QMessageBox.warning(self, 'Peringatan', 'Gagal memperbarui kontak.')

        else:
            QMessageBox.warning(self, 'Peringatan', 'Pilih kontak terlebih dahulu.')

    def delete_contact(self):
        # Menghapus kontak yang dipilih dari database
        current_item = self.contact_list.currentItem()
        if current_item:
            selected_name = current_item.text()
            confirm = QMessageBox.question(self, 'Konfirmasi', f'Anda yakin ingin menghapus kontak {selected_name}?', QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                query = QSqlQuery()
                query.prepare('DELETE FROM contacts WHERE name=?')
                query.bindValue(0, selected_name)
                if query.exec_():
                    self.load_contacts()
                    self.clear_inputs()
                    QMessageBox.information(self, 'Info', 'Kontak berhasil dihapus.')
                else:
                    QMessageBox.warning(self, 'Peringatan', 'Gagal menghapus kontak.')
        else:
            QMessageBox.warning(self, 'Peringatan', 'Pilih kontak terlebih dahulu.')

    def show_contact(self, item): 
        # Menampilkan informasi kontak saat diklik
        selected_name = item.text()
        query = QSqlQuery()
        query.prepare('SELECT * FROM contacts WHERE name=?')
        query.bindValue(0, selected_name)

        if query.exec_() and query.next():
            self.name_input.setText(query.value(0))
            self.phone_input.setText(query.value(1))
            self.email_input.setText(query.value(2))

    def clear_inputs(self):
        # Mengosongkan inputan
        self.name_input.clear()
        self.phone_input.clear()
        self.email_input.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ContactApp()
    window.show()
    sys.exit(app.exec_())