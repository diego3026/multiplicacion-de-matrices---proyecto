import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

class Ventana(QMainWindow):
    rows1 = 0
    cols1 = 0
    rows2 = 0
    cols2 = 0
    
    def __init__(self, padre=None):
        super().__init__(padre)
        uic.loadUi("uis/matrix1.ui",self)
        
        self.setWindowTitle("Multiplicacion de matrices")
        
        self.pushButton.clicked.connect(self.agregarMatrix1)

    def agregarMatrix1(self):
        filas1_texto = self.row1.text()
        columnas1_texto = self.cols1.text()
        filas2_texto = self.rows2.text()
        columnas2_texto = self.cols2.text()

        if (filas1_texto!='' and columnas1_texto!='' and filas2_texto!='' and columnas2_texto!=''):
            if int(columnas1_texto) == int(filas2_texto):
                filas1 = int(filas1_texto)
                columnas1 = int(columnas1_texto)
                filas2 = int(filas2_texto)
                columnas2 = int(columnas2_texto)

                self.rows1 = filas1
                self.cols1 = columnas1   
                self.rows2 = filas2
                self.cols2 = columnas2   

                self.ventanaPrincipal = InsercionVentana()               
                self.ventanaPrincipal.setDatos(self.rows1, self.cols1, self.rows2, self.cols2)
                self.ventanaPrincipal.show()                        
                self.hide()
            else:
                self.info.setText("columnas 1 y filas 2 es diferente")
        else:
            self.info.setText("Rellena los campos")


    def closeEvent(self, event):
        sys.exit()

class InsercionVentana(QWidget):
    rows1 = 0
    cols1 = 0
    rows2 = 0
    cols2 = 0

    def __init__(self, padre=None):
        super().__init__(padre)
        uic.loadUi("uis/insercion1.ui", self)
        self.guardar.clicked.connect(self.multiplicar_matrices)
        self.setWindowTitle("Grid Layout con Filas y Columnas Específicas")

    def setDatos(self, rows1, cols1, rows2, cols2):
        self.rows1 = rows1
        self.rows2 = rows2
        self.cols1 = cols1
        self.cols2 = cols2
        self.matrix1 = [[None] * cols1 for _ in range(rows1)]
        self.matrix2 = [[None] * cols2 for _ in range(rows2)]

        for fila in range(rows1):
            for columna in range(cols1):
                line_edit1 = QLineEdit()
                line_edit1.setFixedSize(41, 31) 
                line_edit1.setStyleSheet("border: 1px solid black;")  
                self.gridLayout_2.addWidget(line_edit1, fila, columna)
                self.matrix1[fila][columna] = line_edit1

        for fila in range(rows2):
            for columna in range(cols2):
                line_edit2 = QLineEdit()
                line_edit2.setFixedSize(41, 31) 
                line_edit2.setStyleSheet("border: 1px solid black;")  
                self.gridLayout_3.addWidget(line_edit2, fila, columna)
                self.matrix2[fila][columna] = line_edit2

    def obtener_datos(self):
        # Recuperar los datos ingresados en la primera matriz
        print("Datos de la primera matriz:")
        for fila in self.matrix1:
            fila_datos = []
            for linea_edit in fila:
                fila_datos.append(linea_edit.text())
            print(fila_datos)

        # Recuperar los datos ingresados en la segunda matriz
        print("Datos de la segunda matriz:")
        for fila in self.matrix2:
            fila_datos = []
            for linea_edit in fila:
                fila_datos.append(linea_edit.text())
            print(fila_datos)

    def multiplicar_matrices(self):
        self.obtener_datos()

        if self.cols1 != self.rows2:
            print("No se pueden multiplicar las matrices: el número de columnas de la primera matriz no coincide con el número de filas de la segunda matriz.")
            return

        result = [[0] * self.cols2 for _ in range(self.rows1)]

        for i in range(self.rows1):
            for j in range(self.cols2):
                for k in range(self.cols1):
                    result[i][j] += int(self.matrix1[i][k].text()) * int(self.matrix2[k][j].text())

        print("Resultado de la multiplicación de matrices:")
        for fila in result:
            print(fila)

        for fila in range(len(result)):
            for columna in range(len(result[fila])):
                line_edit3 = QLineEdit()
                line_edit3.setFixedSize(41, 31) 
                line_edit3.setStyleSheet("border: 1px solid black;")  
                self.gridLayout.addWidget(line_edit3, fila, columna)
                line_edit3.setText(str(result[fila][columna]))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())
