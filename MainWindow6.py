import sys
from PyQt6 import QtCore, QtGui, QtWidgets


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None


class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
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
            nuevo_nodo.anterior = actual

    def insertar_por_posicion(self, valor, posicion):
        nuevo_nodo = Nodo(valor)
        if posicion <= 0:
            self.insertar_inicio(valor)
        else:
            actual = self.cabeza
            contador = 0
            while actual and contador < posicion:
                actual = actual.siguiente
                contador += 1
            if actual:
                nuevo_nodo.siguiente = actual
                nuevo_nodo.anterior = actual.anterior
                actual.anterior.siguiente = nuevo_nodo
                actual.anterior = nuevo_nodo

    def eliminar_inicio(self):
        if self.cabeza:
            self.cabeza = self.cabeza.siguiente
            if self.cabeza:
                self.cabeza.anterior = None

    def eliminar_final(self):
        if self.cabeza:
            if not self.cabeza.siguiente:
                self.cabeza = None
            else:
                actual = self.cabeza
                while actual.siguiente:
                    actual = actual.siguiente
                actual.anterior.siguiente = None

    def eliminar_por_posicion(self, posicion):
        if self.cabeza:
            if posicion <= 0:
                self.eliminar_inicio()
            else:
                actual = self.cabeza
                contador = 0
                while actual and contador < posicion:
                    actual = actual.siguiente
                    contador += 1
                if actual:
                    actual.anterior.siguiente = actual.siguiente
                    if actual.siguiente:
                        actual.siguiente.anterior = actual.anterior

    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False


class Ui_VentanaPrincipal3(object):
    def __init__(self):
        super().__init__()

        self.lista_doble_enlazada = ListaDobleEnlazada()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1400, 750)

        # Fondo
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1401, 751))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("fotos/Fondo liso pastel.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()

        # Explicación
        self.explicacion_label = QtWidgets.QLabel('Lista Doblemente Enlazada: Insertar (Inicio, Final, por Posición), Eliminar (Inicio, Final, por Posición), Buscar Valor',
                                                   parent=Form)
        self.explicacion_label.setGeometry(QtCore.QRect(50, 50, 1300, 50))
        self.explicacion_label.setStyleSheet("font-size: 14pt;")
        self.explicacion_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Recuadro blanco para la interacción del usuario
        self.recuadro = QtWidgets.QFrame(Form)
        self.recuadro.setGeometry(QtCore.QRect(50, 150, 1300, 400))
        self.recuadro.setStyleSheet("background-color: white; border: 2px solid black;")

        # Texto del recuadro blanco
        self.texto_recuadro = QtWidgets.QTextEdit(self.recuadro)
        self.texto_recuadro.setGeometry(QtCore.QRect(20, 20, 1260, 100))
        self.texto_recuadro.setReadOnly(True)

        # Campo de entrada para el valor
        self.valor_txt = QtWidgets.QLineEdit(self.recuadro)
        self.valor_txt.setGeometry(QtCore.QRect(20, 150, 200, 30))

        # Campo de entrada para la posición
        self.posicion_txt = QtWidgets.QLineEdit(self.recuadro)
        self.posicion_txt.setGeometry(QtCore.QRect(300, 150, 200, 30))

        # Botones
        self.insertar_inicio_btn = QtWidgets.QPushButton('Insertar al inicio', self.recuadro)
        self.insertar_inicio_btn.setGeometry(QtCore.QRect(20, 200, 200, 30))

        self.insertar_final_btn = QtWidgets.QPushButton('Insertar al final', self.recuadro)
        self.insertar_final_btn.setGeometry(QtCore.QRect(240, 200, 200, 30))

        self.insertar_posicion_btn = QtWidgets.QPushButton('Insertar por posición', self.recuadro)
        self.insertar_posicion_btn.setGeometry(QtCore.QRect(460, 200, 200, 30))

        self.eliminar_inicio_btn = QtWidgets.QPushButton('Eliminar al inicio', self.recuadro)
        self.eliminar_inicio_btn.setGeometry(QtCore.QRect(20, 240, 200, 30))

        self.eliminar_final_btn = QtWidgets.QPushButton('Eliminar al final', self.recuadro)
        self.eliminar_final_btn.setGeometry(QtCore.QRect(240, 240, 200, 30))

        self.eliminar_posicion_btn = QtWidgets.QPushButton('Eliminar por posición', self.recuadro)
        self.eliminar_posicion_btn.setGeometry(QtCore.QRect(460, 240, 200, 30))

        self.buscar_txt = QtWidgets.QLineEdit(self.recuadro)
        self.buscar_txt.setGeometry(QtCore.QRect(20, 280, 200, 30))

        self.buscar_btn = QtWidgets.QPushButton('Buscar', self.recuadro)
        self.buscar_btn.setGeometry(QtCore.QRect(240, 280, 200, 30))

        self.ver_lista_btn = QtWidgets.QPushButton('Ver Lista', self.recuadro)
        self.ver_lista_btn.setGeometry(QtCore.QRect(460, 280, 200, 30))

        self.insertar_inicio_btn.clicked.connect(self.insertar_inicio)
        self.insertar_final_btn.clicked.connect(self.insertar_final)
        self.insertar_posicion_btn.clicked.connect(self.insertar_por_posicion)
        self.eliminar_inicio_btn.clicked.connect(self.eliminar_inicio)
        self.eliminar_final_btn.clicked.connect(self.eliminar_final)
        self.eliminar_posicion_btn.clicked.connect(self.eliminar_por_posicion)
        self.buscar_btn.clicked.connect(self.buscar_valor)
        self.ver_lista_btn.clicked.connect(self.ver_lista)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    # Functions
    def insertar_inicio(self):
        valor = self.valor_txt.text()
        if valor:
            self.lista_doble_enlazada.insertar_inicio(valor)
            self.actualizar_texto_recuadro(f' {valor} ->')

    def insertar_final(self):
        valor = self.valor_txt.text()
        if valor:
            self.lista_doble_enlazada.insertar_final(valor)
            self.actualizar_texto_recuadro(f' {valor} ->')

    def insertar_por_posicion(self):
        valor = self.valor_txt.text()
        posicion = int(self.posicion_txt.text())
        if valor:
            self.lista_doble_enlazada.insertar_por_posicion(valor, posicion)
            self.actualizar_texto_recuadro(f' {valor} ->')

    def eliminar_inicio(self):
        self.lista_doble_enlazada.eliminar_inicio()
        self.actualizar_texto_recuadro('Se eliminó el primer elemento.')

    def eliminar_final(self):
        self.lista_doble_enlazada.eliminar_final()
        self.actualizar_texto_recuadro('Se eliminó el último elemento.')

    def eliminar_por_posicion(self):
        posicion = int(self.posicion_txt.text())
        self.lista_doble_enlazada.eliminar_por_posicion(posicion)
        self.actualizar_texto_recuadro(f'Se eliminó el elemento en la posición {posicion}.')

    def buscar_valor(self):
        valor = self.buscar_txt.text()
        if valor:
            encontrado = self.lista_doble_enlazada.buscar(valor)
            if encontrado:
                self.actualizar_texto_recuadro(f'Se encontró el valor {valor} en la lista.')
            else:
                self.actualizar_texto_recuadro(f'El valor {valor} no se encuentra en la lista.')

    def ver_lista(self):
        texto_lista = self.generar_texto_lista()
        self.actualizar_texto_recuadro(texto_lista)

    def generar_texto_lista(self):
        texto = ""
        actual = self.lista_doble_enlazada.cabeza
        while actual:
            texto += f" {actual.valor} ->"
            actual = actual.siguiente
        return texto

    def actualizar_texto_recuadro(self, texto):
        self.texto_recuadro.setText(texto)


class VentanaPrincipal(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_VentanaPrincipal3()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana_principal = VentanaPrincipal()
    ventana_principal.show()
    sys.exit(app.exec())

