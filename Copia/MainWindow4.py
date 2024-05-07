import sys
from PyQt6 import QtCore, QtGui, QtWidgets

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def insertar_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar_inicio(self):
        if self.cabeza:
            self.cabeza = self.cabeza.siguiente

    def eliminar_final(self):
        if self.cabeza:
            if not self.cabeza.siguiente:
                self.cabeza = None
            else:
                anterior = None
                actual = self.cabeza
                while actual.siguiente:
                    anterior = actual
                    actual = actual.siguiente
                anterior.siguiente = None

    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

class Ui_VentanaPrincipal(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1400, 500)

        # Fondo
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1401, 501))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("fotos/Fondo liso pastel.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()

        # Explicación
        self.explicacion_label = QtWidgets.QLabel('Las listas simplemente enlazadas son una colección de nodos donde cada nodo\n'
                                                'almacena un valor y una referencia al siguiente nodo en la lista.\n'
                                                'Las operaciones básicas en una lista simplemente enlazada son:\n'
                                                '1. Insertar al inicio y al final\n'
                                                '2. Eliminar al inicio y al final\n'
                                                '3. Buscar un valor en la lista', parent=Form)
        self.explicacion_label.setGeometry(QtCore.QRect(50, 50, 1300, 150))
        self.explicacion_label.setStyleSheet("font-size: 14pt;")
        self.explicacion_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Ejemplo
        self.ejemplo_label = QtWidgets.QLabel('Ejemplo: Lista: 3 -> 7 -> 2 -> 5', parent=Form)
        self.ejemplo_label.setGeometry(QtCore.QRect(50, 220, 300, 30))
        self.ejemplo_label.setStyleSheet("font-size: 14pt;")

        # Recuadro blanco para la interacción del usuario
        self.recuadro = QtWidgets.QFrame(Form)
        self.recuadro.setGeometry(QtCore.QRect(50, 270, 1300, 200))
        self.recuadro.setStyleSheet("background-color: white; border: 2px solid black;")

        # Números ingresados por el usuario
        self.numeros_label = QtWidgets.QLabel('', self.recuadro)
        self.numeros_label.setGeometry(QtCore.QRect(50, 10, 1100, 30))
        self.numeros_label.setStyleSheet("font-size: 14pt;")

        # Campo de entrada para el valor
        self.valor_txt = QtWidgets.QLineEdit(self.recuadro)
        self.valor_txt.setGeometry(QtCore.QRect(50, 50, 200, 30))

        # Botones
        self.insertar_inicio_btn = QtWidgets.QPushButton('Insertar al inicio', self.recuadro)
        self.insertar_inicio_btn.setGeometry(QtCore.QRect(270, 50, 200, 30))

        self.insertar_final_btn = QtWidgets.QPushButton('Insertar al final', self.recuadro)
        self.insertar_final_btn.setGeometry(QtCore.QRect(500, 50, 200, 30))

        self.eliminar_inicio_btn = QtWidgets.QPushButton('Eliminar al inicio', self.recuadro)
        self.eliminar_inicio_btn.setGeometry(QtCore.QRect(730, 50, 200, 30))

        self.eliminar_final_btn = QtWidgets.QPushButton('Eliminar al final', self.recuadro)
        self.eliminar_final_btn.setGeometry(QtCore.QRect(960, 50, 200, 30))

        # Campo de entrada para buscar
        self.buscar_txt = QtWidgets.QLineEdit(Form)
        self.buscar_txt.setGeometry(QtCore.QRect(600, 400, 200, 30))

        # Botón para buscar
        self.buscar_btn = QtWidgets.QPushButton('Buscar', Form)
        self.buscar_btn.setGeometry(QtCore.QRect(850, 400, 200, 30))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

class VentanaPrincipal(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.lista_enlazada = ListaEnlazada()

        self.ui = Ui_VentanaPrincipal()
        self.ui.setupUi(self)

        self.ui.insertar_inicio_btn.clicked.connect(self.insertar_inicio)
        self.ui.insertar_final_btn.clicked.connect(self.insertar_final)
        self.ui.eliminar_inicio_btn.clicked.connect(self.eliminar_inicio)
        self.ui.eliminar_final_btn.clicked.connect(self.eliminar_final)
        self.ui.buscar_btn.clicked.connect(self.buscar_valor)

    def insertar_inicio(self):
        valor = self.ui.valor_txt.text()
        if valor:
            self.lista_enlazada.insertar_inicio(valor)
            self.actualizar_numeros_label(valor)
            self.ui.valor_txt.clear()

    def insertar_final(self):
        valor = self.ui.valor_txt.text()
        if valor:
            self.lista_enlazada.insertar_final(valor)
            self.actualizar_numeros_label(valor)
            self.ui.valor_txt.clear()

    def eliminar_inicio(self):
        if self.lista_enlazada.cabeza:
            valor_eliminado = self.lista_enlazada.cabeza.valor
            self.lista_enlazada.eliminar_inicio()
            self.eliminar_numero(valor_eliminado)

    def eliminar_final(self):
        if self.lista_enlazada.cabeza:
            if not self.lista_enlazada.cabeza.siguiente:
                valor_eliminado = self.lista_enlazada.cabeza.valor
                self.lista_enlazada.eliminar_final()
                self.eliminar_numero(valor_eliminado)
            else:
                actual = self.lista_enlazada.cabeza
                while actual.siguiente.siguiente:
                    actual = actual.siguiente
                valor_eliminado = actual.siguiente.valor
                actual.siguiente = None
                self.eliminar_numero(valor_eliminado)

    def buscar_valor(self):
        valor = self.ui.buscar_txt.text()
        if valor:
            encontrado = self.lista_enlazada.buscar(valor)
            if encontrado:
                QtWidgets.QMessageBox.information(self, 'Buscar', f'Se encontró el valor {valor} en la lista.')
            else:
                QtWidgets.QMessageBox.warning(self, 'Buscar', f'El valor {valor} no se encuentra en la lista.')

    def actualizar_numeros_label(self, valor):
        numeros_actuales = self.ui.numeros_label.text()
        nuevo_texto = f"{numeros_actuales} -> {valor}" if numeros_actuales else f"{valor}"
        self.ui.numeros_label.setText(nuevo_texto)

    def eliminar_numero(self, valor):
        numeros_actuales = self.ui.numeros_label.text().split(" -> ")
        numeros_actuales.remove(valor)
        nuevo_texto = " -> ".join(numeros_actuales)
        self.ui.numeros_label.setText(nuevo_texto)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana_principal = VentanaPrincipal()
    ventana_principal.show()
    sys.exit(app.exec())
