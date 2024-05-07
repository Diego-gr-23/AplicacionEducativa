import sys
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(940, 599)

        # Etiqueta para el fondo
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 941, 621))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("fotos/Fondo liso pastel.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()  # Enviar al fondo

        # Etiqueta para mostrar ejemplo de operaciones de pila
        self.ejemplo_label = QtWidgets.QLabel('Ejemplo de operaciones de pila:', parent=Form)
        self.ejemplo_label.setGeometry(QtCore.QRect(0, 100, 940, 30))
        self.ejemplo_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ejemplo_label.setStyleSheet("font-size: 16pt;")  # Ajustar el tamaño de la letra
        self.ejemplo_label.hide()

        # Cuadros de texto para mostrar los números en el ejemplo
        self.cuadro_1 = QtWidgets.QLabel('1', parent=Form)
        self.cuadro_1.setGeometry(QtCore.QRect(400, 150, 50, 50))
        self.cuadro_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cuadro_1.setStyleSheet("border: 1px solid black;")
        self.cuadro_1.hide()

        self.cuadro_2 = QtWidgets.QLabel('2', parent=Form)
        self.cuadro_2.setGeometry(QtCore.QRect(480, 150, 50, 50))
        self.cuadro_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cuadro_2.setStyleSheet("border: 1px solid black;")
        self.cuadro_2.hide()

        self.cuadro_3 = QtWidgets.QLabel('3', parent=Form)
        self.cuadro_3.setGeometry(QtCore.QRect(560, 150, 50, 50))
        self.cuadro_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cuadro_3.setStyleSheet("border: 1px solid black;")
        self.cuadro_3.hide()

        # Etiqueta para mostrar la pila
        self.pila_label = QtWidgets.QLabel('Pila:', parent=Form)
        self.pila_label.setGeometry(QtCore.QRect(50, 250, 841, 21))
        self.pila_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.pila_label.setStyleSheet("font-size: 16pt;")  # Ajustar el tamaño de la letra

        # Área de texto para mostrar la pila
        self.pila_txt = QtWidgets.QTextEdit(parent=Form)
        self.pila_txt.setGeometry(QtCore.QRect(50, 280, 841, 151))
        self.pila_txt.setReadOnly(True)

        # Campo de entrada para el elemento a agregar
        self.elemento_txt = QtWidgets.QLineEdit(parent=Form)
        self.elemento_txt.setGeometry(QtCore.QRect(50, 450, 141, 31))

        # Botón para insertar un elemento a la pila
        self.insertar_btn = QtWidgets.QPushButton('Insertar', parent=Form)
        self.insertar_btn.setGeometry(QtCore.QRect(200, 450, 141, 31))
        self.insertar_btn.clicked.connect(self.insertar_elemento)

        # Botón para eliminar el último elemento de la pila
        self.eliminar_btn = QtWidgets.QPushButton('Eliminar (Pop)', parent=Form)
        self.eliminar_btn.setGeometry(QtCore.QRect(350, 450, 141, 31))
        self.eliminar_btn.clicked.connect(self.eliminar_elemento)

        # Botón para buscar un valor en la pila
        self.buscar_btn = QtWidgets.QPushButton('Buscar', parent=Form)
        self.buscar_btn.setGeometry(QtCore.QRect(500, 450, 141, 31))
        self.buscar_btn.clicked.connect(self.buscar_elemento)

        # Etiqueta para la explicación de las pilas
        self.explicacion_label = QtWidgets.QLabel('Las pilas son estructuras de datos que siguen el principio LIFO (Last In, First Out).\n'
                                                'Esto significa que el último elemento en entrar es el primero en salir.\n'
                                                'Las operaciones básicas en una pila son:\n'
                                                '1. Insertar (push)\n'
                                                '2. Eliminar (pop)\n'
                                                '3. Buscar', parent=Form)
        self.explicacion_label.setGeometry(QtCore.QRect(50, 50, 841, 151))
        self.explicacion_label.setStyleSheet("font-size: 14pt;")  # Ajustar el tamaño de la letra
        self.explicacion_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    def insertar_elemento(self):
        # Obtener el texto del campo de entrada
        elemento = self.elemento_txt.text()
        # Si hay texto, agregarlo a la pila
        if elemento:
            # Obtener el texto actual de la pila
            texto_actual = self.pila_txt.toPlainText()
            # Concatenar el nuevo elemento al principio del texto
            nuevo_texto = f"{elemento}\n{texto_actual}"
            # Actualizar el contenido de la pila con el nuevo texto
            self.pila_txt.setPlainText(nuevo_texto)
        # Limpiar el campo de entrada después de agregar el elemento
        self.elemento_txt.clear()

    def eliminar_elemento(self):
        # Obtener el texto de la pila
        texto_pila = self.pila_txt.toPlainText()
        # Separar el texto en líneas
        lineas = texto_pila.split("\n")
        # Eliminar la primera línea (el elemento más reciente)
        if lineas:
            lineas.pop(0)
            # Reconstruir el texto de la pila sin el elemento más reciente
            texto_nuevo = "\n".join(lineas)
            # Actualizar el contenido de la pila
            self.pila_txt.setPlainText(texto_nuevo)

    def buscar_elemento(self):
        # Obtener el texto a buscar
        texto_buscar = self.elemento_txt.text()
        # Obtener todo el texto de la pila
        texto_pila = self.pila_txt.toPlainText()
        # Buscar el texto en la pila
        indice = texto_pila.find(texto_buscar)
        if indice != -1:
            # Se encontró el texto, seleccionarlo
            cursor = self.pila_txt.textCursor()
            cursor.setPosition(indice)
            cursor.movePosition(QtGui.QTextCursor.MoveOperation.Right, QtGui.QTextCursor.MoveMode.KeepAnchor, len(texto_buscar))
            self.pila_txt.setTextCursor(cursor)
        else:
            # No se encontró el texto
            QtWidgets.QMessageBox.warning(None, 'Buscar', 'El valor no se encuentra en la pila.', QtWidgets.QMessageBox.StandardButton.Ok)

class VentanaPrincipal(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana_principal = VentanaPrincipal()
    ventana_principal.show()
    sys.exit(app.exec())
