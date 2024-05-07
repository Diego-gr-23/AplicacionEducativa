import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget, QMessageBox, QInputDialog


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow, data):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(455, 585)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 451, 541))
        self.textEdit.setAutoFormatting(QtWidgets.QTextEdit.AutoFormattingFlag.AutoNone)
        self.textEdit.setTabChangesFocus(False)
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 455, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow, data)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaSimplementeEnlazada:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def insertar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def insertar_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar_inicio(self):
        if self.esta_vacia():
            QMessageBox.warning(None, "Lista vacía", "No se puede eliminar, la lista está vacía.")
            return None
        eliminado = self.cabeza.valor
        self.cabeza = self.cabeza.siguiente
        return eliminado

    def eliminar_final(self):
        if self.esta_vacia():
            QMessageBox.warning(None, "Lista vacía", "No se puede eliminar, la lista está vacía.")
            return None
        elif self.cabeza.siguiente is None:
            eliminado = self.cabeza.valor
            self.cabeza = None
            return eliminado
        else:
            actual = self.cabeza
            while actual.siguiente.siguiente:
                actual = actual.siguiente
            eliminado = actual.siguiente.valor
            actual.siguiente = None
            return eliminado

    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    def mostrar(self):
        valores = []
        actual = self.cabeza
        while actual:
            valores.append(actual.valor)
            actual = actual.siguiente
        return valores

class InterfazGraficaListaSimplementeEnlazada(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lista Simplemente Enlazada")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.central_widget)

        self.lista = ListaSimplementeEnlazada()

        self.etiqueta = QLabel()
        layout.addWidget(self.etiqueta)

        self.btn_insertar_inicio = QPushButton("Insertar al inicio")
        self.btn_insertar_inicio.clicked.connect(self.insertar_inicio)
        layout.addWidget(self.btn_insertar_inicio)

        self.btn_insertar_final = QPushButton("Insertar al final")
        self.btn_insertar_final.clicked.connect(self.insertar_final)
        layout.addWidget(self.btn_insertar_final)

        self.btn_eliminar_inicio = QPushButton("Eliminar al inicio")
        self.btn_eliminar_inicio.clicked.connect(self.eliminar_inicio)
        layout.addWidget(self.btn_eliminar_inicio)

        self.btn_eliminar_final = QPushButton("Eliminar al final")
        self.btn_eliminar_final.clicked.connect(self.eliminar_final)
        layout.addWidget(self.btn_eliminar_final)

        self.btn_buscar = QPushButton("Buscar")
        self.btn_buscar.clicked.connect(self.buscar_valor)
        layout.addWidget(self.btn_buscar)

        self.mostrar_lista()

    def insertar_inicio(self):
        valor, ok = QInputDialog.getText(self, "Insertar al inicio", "Ingrese el valor a insertar al inicio:")
        if ok:
            self.lista.insertar_inicio(valor)
            self.mostrar_lista()

    def insertar_final(self):
        valor, ok = QInputDialog.getText(self, "Insertar al final", "Ingrese el valor a insertar al final:")
        if ok:
            self.lista.insertar_final(valor)
            self.mostrar_lista()

    def eliminar_inicio(self):
        eliminado = self.lista.eliminar_inicio()
        if eliminado is not None:
            QMessageBox.information(None, "Elemento eliminado", f"Se eliminó el elemento: {eliminado}")
            self.mostrar_lista()

    def eliminar_final(self):
        eliminado = self.lista.eliminar_final()
        if eliminado is not None:
            QMessageBox.information(None, "Elemento eliminado", f"Se eliminó el elemento: {eliminado}")
            self.mostrar_lista()

    def buscar_valor(self):
        valor, ok = QInputDialog.getText(self, "Buscar", "Ingrese el valor a buscar:")
        if ok:
            encontrado = self.lista.buscar(valor)
            if encontrado:
                QMessageBox.information(None, "Elemento encontrado", f"El valor {valor} está en la lista.")
            else:
                QMessageBox.information(None, "Elemento no encontrado", f"El valor {valor} no está en la lista.")

    def mostrar_lista(self):
        if self.lista.esta_vacia():
            self.etiqueta.setText("Lista vacía")
        else:
            texto_lista = "\n".join(self.lista.mostrar())
            self.etiqueta.setText(texto_lista)

# Crear aplicación
app = QApplication(sys.argv)

# Crear ventana sin mostrarla
ventana_lista_simp = InterfazGraficaListaSimplementeEnlazada()

# Salir de la aplicación
sys.exit(app.exec())
