import sys
from PyQt6 import QtCore, QtGui, QtWidgets


class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class ArbolBinario:
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
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        if valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo.derecha, valor)

    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return None
        if valor == nodo.valor:
            if nodo.izquierda is None and nodo.derecha is None:
                return None
            if nodo.izquierda is None:
                return nodo.derecha
            if nodo.derecha is None:
                return nodo.izquierda
            nodo.valor = self._encontrar_menor_valor(nodo.derecha)
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, nodo.valor)
        elif valor < nodo.valor:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, valor)
        else:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, valor)
        return nodo

    def _encontrar_menor_valor(self, nodo):
        while nodo.izquierda is not None:
            nodo = nodo.izquierda
        return nodo.valor


class Ui_VentanaPrincipal5(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 750)

        # Fondo
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1001, 751))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("fotos/Fondo liso pastel.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()

        # Explicación
        self.explicacion_label = QtWidgets.QLabel('Árbol Binario: Insertar, Eliminar, Buscar Valor', parent=Form)
        self.explicacion_label.setGeometry(QtCore.QRect(50, 50, 800, 50))
        self.explicacion_label.setStyleSheet("font-size: 14pt;")
        self.explicacion_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Recuadro blanco para la interacción del usuario
        self.recuadro = QtWidgets.QFrame(Form)
        self.recuadro.setGeometry(QtCore.QRect(50, 150, 500, 500))
        self.recuadro.setStyleSheet("background-color: white; border: 2px solid black;")

        # Texto del recuadro blanco
        self.texto_recuadro = QtWidgets.QTextEdit(self.recuadro)
        self.texto_recuadro.setGeometry(QtCore.QRect(20, 20, 460, 300))
        self.texto_recuadro.setReadOnly(True)

        # Campo de entrada para el valor
        self.valor_txt = QtWidgets.QLineEdit(self.recuadro)
        self.valor_txt.setGeometry(QtCore.QRect(20, 340, 200, 30))

        # Botón de Insertar
        self.insertar_btn = QtWidgets.QPushButton('Insertar', self.recuadro)
        self.insertar_btn.setGeometry(QtCore.QRect(240, 340, 200, 30))

        # Botones
        self.eliminar_btn = QtWidgets.QPushButton('Eliminar', self.recuadro)
        self.eliminar_btn.setGeometry(QtCore.QRect(20, 380, 200, 30))

        self.buscar_txt = QtWidgets.QLineEdit(self.recuadro)
        self.buscar_txt.setGeometry(QtCore.QRect(20, 420, 200, 30))

        self.buscar_btn = QtWidgets.QPushButton('Buscar', self.recuadro)
        self.buscar_btn.setGeometry(QtCore.QRect(240, 420, 200, 30))

        # Botón para ver el árbol
        self.ver_arbol_btn = QtWidgets.QPushButton('Ver Árbol', Form)
        self.ver_arbol_btn.setGeometry(QtCore.QRect(600, 300, 200, 30))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


class VentanaPrincipal(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.arbol_binario = ArbolBinario()

        self.ui = Ui_VentanaPrincipal5()
        self.ui.setupUi(self)

        self.ui.insertar_btn.clicked.connect(self.insertar)
        self.ui.eliminar_btn.clicked.connect(self.eliminar)
        self.ui.buscar_btn.clicked.connect(self.buscar_valor)
        self.ui.ver_arbol_btn.clicked.connect(self.ver_arbol)

    def insertar(self):
        valor = self.ui.valor_txt.text()
        if valor:
            self.arbol_binario.insertar(valor)
            self.actualizar_texto_recuadro(f'Insertado: {valor}')
            self.ui.valor_txt.clear()

    def eliminar(self):
        valor = self.ui.valor_txt.text()
        if valor:
            self.arbol_binario.eliminar(valor)
            self.actualizar_texto_recuadro(f'Elemento eliminado: {valor}')
            self.ui.valor_txt.clear()

    def buscar_valor(self):
        valor = self.ui.buscar_txt.text()
        if valor:
            encontrado = self.arbol_binario.buscar(valor)
            if encontrado:
                self.actualizar_texto_recuadro(f'Se encontró el valor {valor} en el árbol binario.')
            else:
                self.actualizar_texto_recuadro(f'El valor {valor} no se encuentra en el árbol binario.')

    def ver_arbol(self):
        visualizacion_arbol = self.obtener_visualizacion_arbol()
        self.actualizar_texto_recuadro(visualizacion_arbol)

    def obtener_visualizacion_arbol(self):
        return self.obtener_visualizacion_recursiva(self.arbol_binario.raiz)
    
    def obtener_visualizacion_recursiva(self, nodo, nivel=0):
        if nodo is None:
            return ""

        texto = ""
        # Calcular la cantidad de espacios para centrar el texto en función del nivel
        espacios = " " * (nivel * 4)
        # Agregar el valor del nodo actual centrado
        texto += espacios + str(nodo.valor) + "\n"

        # Agregar las divisiones a la izquierda y derecha del nodo
        if nodo.izquierda:
            texto += espacios + " / "
        if nodo.derecha:
            texto += " \\\n"

        # Llamar recursivamente para los nodos izquierdo y derecho
        texto += self.obtener_visualizacion_recursiva(nodo.izquierda, nivel + 1)
        texto += self.obtener_visualizacion_recursiva(nodo.derecha, nivel + 1)

        return texto



    def actualizar_texto_recuadro(self, texto):
        texto_actual = self.ui.texto_recuadro.toPlainText()
        nuevo_texto = f"{texto}\n{texto_actual}"
        self.ui.texto_recuadro.setPlainText(nuevo_texto)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana_principal = VentanaPrincipal()
    ventana_principal.show()
    sys.exit(app.exec())
    
