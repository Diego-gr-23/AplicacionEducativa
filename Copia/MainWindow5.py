import sys
from PyQt6 import QtCore, QtGui, QtWidgets

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            nuevo_nodo.siguiente = nuevo_nodo
            self.cabeza = nuevo_nodo
        else:
            ultimo = self.cabeza
            while ultimo.siguiente != self.cabeza:
                ultimo = ultimo.siguiente
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
            ultimo.siguiente = nuevo_nodo

    def insertar_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            nuevo_nodo.siguiente = nuevo_nodo
            self.cabeza = nuevo_nodo
        else:
            ultimo = self.cabeza
            while ultimo.siguiente != self.cabeza:
                ultimo = ultimo.siguiente
            nuevo_nodo.siguiente = self.cabeza
            ultimo.siguiente = nuevo_nodo

    def eliminar_inicio(self):
        if self.cabeza:
            if self.cabeza.siguiente == self.cabeza:
                self.cabeza = None
            else:
                ultimo = self.cabeza
                while ultimo.siguiente != self.cabeza:
                    ultimo = ultimo.siguiente
                ultimo.siguiente = self.cabeza.siguiente
                self.cabeza = self.cabeza.siguiente

    def eliminar_final(self):
        if self.cabeza:
            if self.cabeza.siguiente == self.cabeza:
                self.cabeza = None
            else:
                ultimo_anterior = None
                ultimo = self.cabeza
                while ultimo.siguiente != self.cabeza:
                    ultimo_anterior = ultimo
                    ultimo = ultimo.siguiente
                ultimo_anterior.siguiente = self.cabeza
                ultimo = None

    def buscar(self, valor):
        actual = self.cabeza
        if actual is not None:
            while True:
                if actual.valor == valor:
                    return True
                actual = actual.siguiente
                if actual == self.cabeza:
                    break
        return False

    def rotar_izquierda(self):
        if self.cabeza:
            self.cabeza = self.cabeza.siguiente

    def rotar_derecha(self):
        if self.cabeza:
            ultimo = self.cabeza
            while ultimo.siguiente != self.cabeza:
                ultimo = ultimo.siguiente
            ultimo.siguiente = self.cabeza
            self.cabeza = ultimo

class Ui_VentanaPrincipal2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1500, 700)

        # Fondo
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1501, 701))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("fotos/Fondo liso pastel.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()

        # Explicación
        self.explicacion_label = QtWidgets.QLabel('Las listas circulares son una colección de nodos donde cada nodo\n'
                                                'almacena un valor y una referencia al siguiente nodo en la lista.\n'
                                                'La diferencia con las listas simplemente enlazadas es que el último\n'
                                                'nodo apunta al primer nodo, formando un círculo.\n'
                                                'Las operaciones básicas en una lista circular son:\n'
                                                '1. Insertar al inicio y al final\n'
                                                '2. Eliminar al inicio y al final\n'
                                                '3. Buscar un valor en la lista\n'
                                                '4. Rotar a la izquierda\n'
                                                '5. Rotar a la derecha', parent=Form)
        self.explicacion_label.setGeometry(QtCore.QRect(50, 50, 1500, 200))
        self.explicacion_label.setStyleSheet("font-size: 14pt;")
        self.explicacion_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Ejemplo
        self.ejemplo_label = QtWidgets.QLabel('Ejemplo: Lista: 3 -> 7 -> 2 -> 5 (Circular)', parent=Form)
        self.ejemplo_label.setGeometry(QtCore.QRect(50, 270, 400, 30))
        self.ejemplo_label.setStyleSheet("font-size: 14pt;")

        # Recuadro blanco para la interacción del usuario
        self.recuadro = QtWidgets.QFrame(Form)
        self.recuadro.setGeometry(QtCore.QRect(50, 310, 1400, 300))
        self.recuadro.setStyleSheet("background-color: white; border: 2px solid black;")

        # Números ingresados por el usuario
        self.numeros_label = QtWidgets.QLabel('', self.recuadro)
        self.numeros_label.setGeometry(QtCore.QRect(50, 10, 1300, 30))
        self.numeros_label.setStyleSheet("font-size: 14pt;")

        # Campo de entrada para el valor
        self.valor_txt = QtWidgets.QLineEdit(self.recuadro)
        self.valor_txt.setGeometry(QtCore.QRect(50, 50, 200, 30))

        # Botones
        self.insertar_inicio_btn = QtWidgets.QPushButton('Insertar al inicio', self.recuadro)
        self.insertar_inicio_btn.setGeometry(QtCore.QRect(50, 90, 200, 30))

        self.insertar_final_btn = QtWidgets.QPushButton('Insertar al final', self.recuadro)
        self.insertar_final_btn.setGeometry(QtCore.QRect(300, 90, 200, 30))

        self.eliminar_inicio_btn = QtWidgets.QPushButton('Eliminar al inicio', self.recuadro)
        self.eliminar_inicio_btn.setGeometry(QtCore.QRect(550, 90, 200, 30))

        self.eliminar_final_btn = QtWidgets.QPushButton('Eliminar al final', self.recuadro)
        self.eliminar_final_btn.setGeometry(QtCore.QRect(800, 90, 200, 30))

        self.rotar_izquierda_btn = QtWidgets.QPushButton('Rotar a la izquierda', self.recuadro)
        self.rotar_izquierda_btn.setGeometry(QtCore.QRect(50, 150, 200, 30))

        self.rotar_derecha_btn = QtWidgets.QPushButton('Rotar a la derecha', self.recuadro)
        self.rotar_derecha_btn.setGeometry(QtCore.QRect(300, 150, 200, 30))

        # Campo de entrada para buscar
        self.buscar_txt = QtWidgets.QLineEdit(Form)
        self.buscar_txt.setGeometry(QtCore.QRect(600, 500, 200, 30))

        # Botón para buscar
        self.buscar_btn = QtWidgets.QPushButton('Buscar', Form)
        self.buscar_btn.setGeometry(QtCore.QRect(850, 500, 200, 30))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

class VentanaPrincipal(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.lista_circular = ListaCircular()

        self.ui = Ui_VentanaPrincipal2()
        self.ui.setupUi(self)

        self.ui.insertar_inicio_btn.clicked.connect(self.insertar_inicio)
        self.ui.insertar_final_btn.clicked.connect(self.insertar_final)
        self.ui.eliminar_inicio_btn.clicked.connect(self.eliminar_inicio)
        self.ui.eliminar_final_btn.clicked.connect(self.eliminar_final)
        self.ui.rotar_izquierda_btn.clicked.connect(self.rotar_izquierda)
        self.ui.rotar_derecha_btn.clicked.connect(self.rotar_derecha)
        self.ui.buscar_btn.clicked.connect(self.buscar_valor)

    def insertar_inicio(self):
        valor = self.ui.valor_txt.text()
        if valor:
            self.lista_circular.insertar_inicio(valor)
            self.actualizar_numeros_label(valor)
            self.ui.valor_txt.clear()

    def insertar_final(self):
        valor = self.ui.valor_txt.text()
        if valor:
            self.lista_circular.insertar_final(valor)
            self.actualizar_numeros_label(valor)
            self.ui.valor_txt.clear()

    def eliminar_inicio(self):
        self.lista_circular.eliminar_inicio()
        self.eliminar_numero()

    def eliminar_final(self):
        self.lista_circular.eliminar_final()
        self.eliminar_numero()

    def buscar_valor(self):
        valor = self.ui.buscar_txt.text()
        if valor:
            encontrado = self.lista_circular.buscar(valor)
            if encontrado:
                QtWidgets.QMessageBox.information(self, 'Buscar', f'Se encontró el valor {valor} en la lista.')
            else:
                QtWidgets.QMessageBox.warning(self, 'Buscar', f'El valor {valor} no se encuentra en la lista.')

    def rotar_izquierda(self):
        self.lista_circular.rotar_izquierda()
        self.actualizar_numeros_label()

    def rotar_derecha(self):
        self.lista_circular.rotar_derecha()
        self.actualizar_numeros_label()

    def actualizar_numeros_label(self, nuevo_valor=None):
        numeros_actuales = self.ui.numeros_label.text().split(" -> ")
        if nuevo_valor:
            numeros_actuales.append(nuevo_valor)
        else:
            numeros_actuales.pop()
        nuevo_texto = " -> ".join(numeros_actuales)
        self.ui.numeros_label.setText(nuevo_texto)

    def eliminar_numero(self):
        numeros_actuales = self.ui.numeros_label.text().split(" -> ")
        numeros_actuales.pop(0)
        nuevo_texto = " -> ".join(numeros_actuales)
        self.ui.numeros_label.setText(nuevo_texto)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana_principal = VentanaPrincipal()
    ventana_principal.show()
    sys.exit(app.exec())
