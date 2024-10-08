# main_window.py

"""Main window-style application."""
import sys

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
    QTabWidget,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
    QListWidget,
    QListWidgetItem,
)

class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.setStyleSheet("background-color: #B5CFEE;")  # Azul oscuro serio
        self.setWindowTitle("Rocket Simulator")
        self.setCentralWidget(QTabWidget())
        self._createTabs()
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    def _createTabs(self):
        tabs = self.centralWidget()
        design_tab = QWidget()
        components_tab = QWidget()
        motor_curve_tab = QWidget()
        mass_var_tab = QWidget()
        graphics_tab = QWidget()
        atmosphere_tab = QWidget()
        simulation_tab = QWidget()

        tabs.addTab(design_tab, "Diseño")
        tabs.addTab(components_tab, "Componentes")
        tabs.addTab(motor_curve_tab, "Curva de Motor")
        tabs.addTab(mass_var_tab, "Variacion de Masa")
        
        tabs.addTab(atmosphere_tab, "Atmósfera-Viento")
        tabs.addTab(simulation_tab, "Simulacion")
        tabs.addTab(graphics_tab, "Gráficas")

        self._createDesignTab(design_tab)
        self._createComponentsTab(components_tab)
        self._createMotorCurveTab(motor_curve_tab)
        self._createGraphicsTab(graphics_tab)
        #self._createAtmosphereTab(atmosphere_tab)
        self._createSimulationTab(simulation_tab)
        #self._createMassVarTab(mass_var_tab)

##Design Tab
    def _createDesignTab(self, tab):
        layout = QVBoxLayout()
        tab.setLayout(layout)

        # Título
        title_label = QLabel("<h2>Simulador de trayectoria</h2>")
        layout.addWidget(title_label)

        # Campos de entrada
        input_layout = QVBoxLayout()
        input_layout.addWidget(QLabel("Nombre:"))
        self.name_input = QLineEdit()
        input_layout.addWidget(self.name_input)

        input_layout.addWidget(QLabel("Diámetro externo:"))
        self.diameter_input = QLineEdit()
        input_layout.addWidget(self.diameter_input)

        input_layout.addWidget(QLabel("Espesor:"))
        self.thickness_input = QLineEdit()
        input_layout.addWidget(self.thickness_input)

        input_layout.addWidget(QLabel("Otras dimensiones:"))
        self.dimensions_input = QLineEdit()
        input_layout.addWidget(self.dimensions_input)

        input_layout.addWidget(QLabel("Otras dimensiones:"))
        self.dimensions_input = QLineEdit()
        input_layout.addWidget(self.dimensions_input)

        input_layout.addWidget(QLabel("Otras dimensiones:"))
        self.dimensions_input = QLineEdit()
        input_layout.addWidget(self.dimensions_input)

        layout.addLayout(input_layout)

        # Botón para guardar
        save_button = QPushButton("Guardar")
        save_button.clicked.connect(self.saveDesignData)
        layout.addWidget(save_button)

        # Mensaje de continuar
        self.continue_message = QLabel("Continua en la siguiente pestaña")
        layout.addWidget(self.continue_message)

    def saveDesignData(self):
        name = self.name_input.text()
        diameter = self.diameter_input.text()
        thickness = self.thickness_input.text()
        dimensions = self.dimensions_input.text()
        # Aquí puedes guardar los datos en variables o en una base de datos
        print(f"Guardando datos")
        self.continue_message.setText("Valores guardados correctamente. Continuar...")


##Components Tab
    def _createComponentsTab(self, tab):
        layout = QVBoxLayout()
        tab.setLayout(layout)

        # Lista de componentes
        components_list = QListWidget()
        components_list.addItem(QListWidgetItem("Nariz"))
        components_list.addItem(QListWidgetItem("Fuselaje"))
        components_list.addItem(QListWidgetItem("Motor"))
        components_list.addItem(QListWidgetItem("Tanque de Combustible"))
        components_list.addItem(QListWidgetItem("Aletas"))
        components_list.addItem(QListWidgetItem("Paracaídas"))

        layout.addWidget(components_list)

        # Campos de entrada
        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("Valor:"))
        self.value_input = QLineEdit()
        input_layout.addWidget(self.value_input)

        layout.addLayout(input_layout)

        # Botones
        button_layout = QHBoxLayout()
        save_button = QPushButton("Guardar")
        save_button.clicked.connect(self.saveDesignData)
        button_layout.addWidget(save_button)
        clear_button = QPushButton("Limpiar")
        clear_button.clicked.connect(self.clearDesignData)
        button_layout.addWidget(clear_button)

        layout.addLayout(button_layout)

    def saveDesignData(self):
        component = self.components_list.currentItem().text()
        value = self.value_input.text()
        # Aquí puedes guardar los datos en variables o en una base de datos
        print(f"Guardando datos: Componente={component}, Valor={value}")

    def clearDesignData(self):
        self.value_input.clear()

##Motor curve Tab
    def _createMotorCurveTab(self, tab):
        layout = QVBoxLayout()
        tab.setLayout(layout)

        # Campos de entrada
        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("Motor:"))
        self.motor_input = QLineEdit()
        input_layout.addWidget(self.motor_input)
        input_layout.addWidget(QLabel("Curva:"))
        self.curve_input = QLineEdit()
        input_layout.addWidget(self.curve_input)

        layout.addLayout(input_layout)

        # Botones
        button_layout = QHBoxLayout()
        save_button = QPushButton("Guardar")
        save_button.clicked.connect(self.saveMotorCurveData)
        button_layout.addWidget(save_button)
        clear_button = QPushButton("Limpiar")
        clear_button.clicked.connect(self.clearMotorCurveData)
        button_layout.addWidget(clear_button)

        layout.addLayout(button_layout)

##Graphics Tab
    def _createGraphicsTab(self, tab):
        layout = QVBoxLayout()
        tab.setLayout(layout)

        # Tabla
        self.graphics_table = QTableWidget()
        self.graphics_table.setRowCount(5)
        self.graphics_table.setColumnCount(2)
        self.graphics_table.setHorizontalHeaderItem(0, QTableWidgetItem("X"))
        self.graphics_table.setHorizontalHeaderItem(1, QTableWidgetItem("Y"))
        layout.addWidget(self.graphics_table)

    def saveMotorCurveData(self):
        motor = self.motor_input.text()
        curve = self.curve_input.text()
        # Aquí puedes guardar los datos en variables o en una base de datos
        print(f"Guardando datos: Motor={motor}, Curva={curve}")

    def clearMotorCurveData(self):
        self.motor_input.clear()
        self.curve_input.clear()

##Simulation Tab
    def _createSimulationTab(self,tab):
        layout = QVBoxLayout()
        tab.setLayout(layout)
    

##Menu Tab
    def _createMenu(self):
        menu = self.menuBar().addMenu("&Menu")
        menu.addAction("&Exit", self.close)

    def _createToolBar(self):
        tools = QToolBar()
        tools.addAction("Exit", self.close)
        self.addToolBar(tools)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("Estas diseñando un COHETE :)")
        self.setStatusBar(status)

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())