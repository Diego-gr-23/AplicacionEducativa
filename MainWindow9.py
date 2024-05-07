import sys
from PyQt6 import QtCore, QtGui, QtWidgets

class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if not self.raiz:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)

    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, valor)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            nodo.valor = self._min_valor(nodo.derecha)
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, nodo.valor)
        return nodo

    def _min_valor(self, nodo):
        while nodo.izquierda is not None:
            nodo = nodo.izquierda
        return nodo.valor

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo.derecha, valor)

    def generar_texto_arbol(self):
        texto = ""
        if self.raiz:
            texto = self._generar_texto_arbol_recursivo(self.raiz)
        return texto

    def _generar_texto_arbol_recursivo(self, nodo):
        if nodo is None:
            return ""
        texto_izquierda = self._generar_texto_arbol_recursivo(nodo.izquierda)
        texto_derecha = self._generar_texto_arbol_recursivo(nodo.derecha)
        return f"({texto_izquierda}) {nodo.valor} ({texto_derecha})"

class Ui_VentanaPrincipal6(object):
    def __init__(self):
        super().__init__()

        self.arbol_busqueda = ArbolBinarioBusqueda()

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
        self.explicacion_label = QtWidgets.QLabel('Árbol de Búsqueda Binario: Insertar, Eliminar, Buscar Valor',
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
        self.insertar_btn = QtWidgets.QPushButton('Insertar', self.recuadro)
        self.insertar_btn.setGeometry(QtCore.QRect(20, 200, 200, 30))

        self.eliminar_btn = QtWidgets.QPushButton('Eliminar', self.recuadro)
        self.eliminar_btn.setGeometry(QtCore.QRect(240, 200, 200, 30))

        self.buscar_btn = QtWidgets.QPushButton('Buscar', self.recuadro)
        self.buscar_btn.setGeometry(QtCore.QRect(460, 200, 200, 30))

        self.ver_arbol_btn = QtWidgets.QPushButton('Ver Árbol', self.recuadro)
        self.ver_arbol_btn.setGeometry(QtCore.QRect(680, 200, 200, 30))

        self.insertar_btn.clicked.connect(self.insertar)
        self.eliminar_btn.clicked.connect(self.eliminar)
        self.buscar_btn.clicked.connect(self.buscar)
        self.ver_arbol_btn.clicked.connect(self.ver_arbol)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    # Functions
    def insertar(self):
        valor = self.valor_txt.text()
        if valor:
            self.arbol_busqueda.insertar(int(valor))
            texto_arbol = self.arbol_busqueda.generar_texto_arbol()
            self.actualizar_texto_recuadro(f'Insertado: {valor}\nÁrbol: {texto_arbol}')
            self.valor_txt.clear()

    def eliminar(self):
        valor = self.valor_txt.text()
        if valor:
            self.arbol_busqueda.eliminar(int(valor))
            texto_arbol = self.arbol_busqueda.generar_texto_arbol()
            self.actualizar_texto_recuadro(f'Eliminado: {valor}\nÁrbol: {texto_arbol}')
            self.valor_txt.clear()

    def buscar(self):
        valor = self.valor_txt.text()
        if valor:
            encontrado = self.arbol_busqueda.buscar(int(valor))
            estado = "encontrado" if encontrado else "no encontrado"
            texto_arbol = self.arbol_busqueda.generar_texto_arbol()
            self.actualizar_texto_recuadro(f'Valor {valor} {estado}\nÁrbol: {texto_arbol}')

    def ver_arbol(self):
        texto_arbol = self.arbol_busqueda.generar_texto_arbol()
        self.actualizar_texto_recuadro(f'Árbol: {texto_arbol}')

    def actualizar_texto_recuadro(self, texto):
        texto_actual = self.texto_recuadro.toPlainText()
        nuevo_texto = f"{texto}\n{texto_actual}"
        self.texto_recuadro.setPlainText(nuevo_texto)


class VentanaPrincipal(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_VentanaPrincipal6()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana_principal = VentanaPrincipal()
    ventana_principal.show()
    sys.exit(app.exec())
