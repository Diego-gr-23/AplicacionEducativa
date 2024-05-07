import sys
from PyQt6 import QtCore, QtGui, QtWidgets


class NodoCircularDoble:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None


class ListaCircularDoble:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, valor):
        nuevo_nodo = NodoCircularDoble(valor)
        if not self.cabeza:
            nuevo_nodo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            nuevo_nodo.anterior = self.cabeza.anterior
            self.cabeza.anterior.siguiente = nuevo_nodo
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

    def insertar_final(self, valor):
        nuevo_nodo = NodoCircularDoble(valor)
        if not self.cabeza:
            nuevo_nodo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            nuevo_nodo.anterior = self.cabeza.anterior
            self.cabeza.anterior.siguiente = nuevo_nodo
            self.cabeza.anterior = nuevo_nodo

    def eliminar_inicio(self):
        if self.cabeza:
            if self.cabeza.siguiente == self.cabeza:
                self.cabeza = None
            else:
                self.cabeza.anterior.siguiente = self.cabeza.siguiente
                self.cabeza.siguiente.anterior = self.cabeza.anterior
                self.cabeza = self.cabeza.siguiente

    def eliminar_final(self):
        if self.cabeza:
            if self.cabeza.siguiente == self.cabeza:
                self.cabeza = None
            else:
                self.cabeza.anterior.anterior.siguiente = self.cabeza
                self.cabeza.anterior = self.cabeza.anterior.anterior

    def buscar(self, valor):
        actual = self.cabeza
        if actual:
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
            self.cabeza = self.cabeza.anterior

    def obtener_lista_en_linea(self):
        lista_en_linea = []
        actual = self.cabeza
        if actual:
            while True:
                lista_en_linea.append(actual.valor)
                actual = actual.siguiente
                if actual == self.cabeza:
                    break
        return lista_en_linea


class Ui_VentanaPrincipal4(object):
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
        self.explicacion_label = QtWidgets.QLabel('Lista Circular Doble: Insertar (Inicio, Final), Eliminar (Inicio, Final), Buscar Valor, Rotar Izquierda, Rotar Derecha',
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

        # Botones
        self.insertar_inicio_btn = QtWidgets.QPushButton('Insertar al inicio', self.recuadro)
        self.insertar_inicio_btn.setGeometry(QtCore.QRect(20, 200, 200, 30))

        self.insertar_final_btn = QtWidgets.QPushButton('Insertar al final', self.recuadro)
        self.insertar_final_btn.setGeometry(QtCore.QRect(240, 200, 200, 30))

        self.eliminar_inicio_btn = QtWidgets.QPushButton('Eliminar al inicio', self.recuadro)
        self.eliminar_inicio_btn.setGeometry(QtCore.QRect(20, 250, 200, 30))

        self.eliminar_final_btn = QtWidgets.QPushButton('Eliminar al final', self.recuadro)
        self.eliminar_final_btn.setGeometry(QtCore.QRect(240, 250, 200, 30))

        self.buscar_txt = QtWidgets.QLineEdit(self.recuadro)
        self.buscar_txt.setGeometry(QtCore.QRect(20, 300, 200, 30))

        self.buscar_btn = QtWidgets.QPushButton('Buscar', self.recuadro)
        self.buscar_btn.setGeometry(QtCore.QRect(240, 300, 200, 30))

        self.rotar_izquierda_btn = QtWidgets.QPushButton('Rotar Izquierda', self.recuadro)
        self.rotar_izquierda_btn.setGeometry(QtCore.QRect(20, 350, 200, 30))

        self.rotar_derecha_btn = QtWidgets.QPushButton('Rotar Derecha', self.recuadro)
        self.rotar_derecha_btn.setGeometry(QtCore.QRect(240, 350, 200, 30))

        self.ver_lista_btn = QtWidgets.QPushButton('Ver Lista', self.recuadro)
        self.ver_lista_btn.setGeometry(QtCore.QRect(460, 350, 200, 30))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


class VentanaPrincipal(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.lista_circular_doble = ListaCircularDoble()

        self.ui = Ui_VentanaPrincipal4()
        self.ui.setupUi(self)

        self.ui.insertar_inicio_btn.clicked.connect(self.insertar_inicio)
        self.ui.insertar_final_btn.clicked.connect(self.insertar_final)
        self.ui.eliminar_inicio_btn.clicked.connect(self.eliminar_inicio)
        self.ui.eliminar_final_btn.clicked.connect(self.eliminar_final)
        self.ui.buscar_btn.clicked.connect(self.buscar_valor)
        self.ui.rotar_izquierda_btn.clicked.connect(self.rotar_izquierda)
        self.ui.rotar_derecha_btn.clicked.connect(self.rotar_derecha)
        self.ui.ver_lista_btn.clicked.connect(self.ver_lista)

    def insertar_inicio(self):
        valor = self.ui.valor_txt.text()
        if valor:
            self.lista_circular_doble.insertar_inicio(valor)
            self.actualizar_texto_recuadro(f'-> {valor}')
            self.ui.valor_txt.clear()

    def insertar_final(self):
        valor = self.ui.valor_txt.text()
        if valor:
            self.lista_circular_doble.insertar_final(valor)
            self.actualizar_texto_recuadro(f'-> {valor}')
            self.ui.valor_txt.clear()

    def eliminar_inicio(self):
        self.lista_circular_doble.eliminar_inicio()
        self.actualizar_texto_recuadro('Se eliminó el primer elemento.')

    def eliminar_final(self):
        self.lista_circular_doble.eliminar_final()
        self.actualizar_texto_recuadro('Se eliminó el último elemento.')

    def buscar_valor(self):
        valor = self.ui.buscar_txt.text()
        if valor:
            encontrado = self.lista_circular_doble.buscar(valor)
            if encontrado:
                self.actualizar_texto_recuadro(f'Se encontró el valor {valor} en la lista.')
            else:
                self.actualizar_texto_recuadro(f'El valor {valor} no se encuentra en la lista.')

    def rotar_izquierda(self):
        self.lista_circular_doble.rotar_izquierda()
        self.actualizar_texto_recuadro('Se rotó la lista a la izquierda.')

    def rotar_derecha(self):
        self.lista_circular_doble.rotar_derecha()
        self.actualizar_texto_recuadro('Se rotó la lista a la derecha.')

    def ver_lista(self):
        lista_en_linea = self.lista_circular_doble.obtener_lista_en_linea()
        texto = "Lista: "
        texto += " -> ".join(lista_en_linea)
        self.actualizar_texto_recuadro(texto)

    def actualizar_texto_recuadro(self, texto):
        texto_actual = self.ui.texto_recuadro.toPlainText()
        nuevo_texto = f"{texto}\n{texto_actual}"
        self.ui.texto_recuadro.setPlainText(nuevo_texto)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana_principal = VentanaPrincipal()
    ventana_principal.show()
    sys.exit(app.exec())
