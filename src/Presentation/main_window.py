from .ventana_principal import *
from .ventana_actualizar import Ui_ActualizarWIndow
from .mensaje_exitoso import Ui_Dialog_Success_Message
from .mensaje_error_borrarEquipo import Ui_Dialog_Delete_Message
from ..BusinessLogic.team_controller import TeamController


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.widget = QtWidgets.QMainWindow()

        # Select page from the StackWidget
        self.BtnEquipo.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PaginaEquipos))
        self.BtnTabla.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PaginaTabla))
        self.BtnJornada.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PaginaJornada))

        # CRUD buttons
        self.BtnInsertar.clicked.connect(lambda: self.add_team())
        self.BtnActualizar.clicked.connect(lambda: self.update_team())
        self.btnlistar.clicked.connect(lambda: self.load_teams_table())
        self.BtnBorrar.clicked.connect(lambda: self.delete_team())

    # General methods
    def successful_message_dialog(self):
        successful_message = Ui_Dialog_Success_Message()
        successful_message.setupUi(self.widget)
        self.widget.show()
        successful_message.pushButton.clicked.connect(lambda: self.widget.close())

    def error_message_dialog_for_id(self):
        error_message = Ui_Dialog_Delete_Message()
        error_message.setupUi(self.widget)
        self.widget.show()
        error_message.pushButton.clicked.connect(lambda: self.widget.close())

    # Methods for teams operations
    def add_team(self):
        name = str(self.TxtNombreEquipo.toPlainText())
        manager = str(self.TxtRepresentanteEquipo.toPlainText())
        field = str(self.TxtCampoEquipo.toPlainText())

        TeamController.add_team(name, manager, field)
        self.successful_message_dialog()

    def delete_team(self):
        try:
            id = int(self.tablaEquipos.currentItem().text())
            TeamController.delete_team(id)
            self.successful_message_dialog()
        except ValueError:
            self.error_message_dialog_for_id()
            # raise Exception("You have to select an 'id' cell")

    def update_team(self):
        def set_data(id: int):
            name = str(update_widget.TxtNombre.toPlainText())
            manager = str(update_widget.TxtRepresentante.toPlainText())
            field = str(update_widget.TxtCampo.toPlainText())

            TeamController.update_team(id, name, manager, field)
            self.widget.close()
        try:
            id = int(self.tablaEquipos.currentItem().text())
            update_widget = Ui_ActualizarWIndow()
            update_widget.setupUi(self.widget)
            self.widget.show()
            update_widget.BtnAceptar.clicked.connect(lambda: set_data(id))
        except ValueError:
            self.error_message_dialog_for_id()

    def load_teams_table(self):
        team_list = TeamController.get_all_teams()
        list_size = len(team_list)
        self.tablaEquipos.setRowCount(list_size)
        for i in range(0, list_size):
            row = i
            id = str(team_list[i].id)
            self.tablaEquipos.setItem(row, 0, QtWidgets.QTableWidgetItem(id))
            self.tablaEquipos.setItem(row, 1, QtWidgets.QTableWidgetItem(team_list[i].name))
            self.tablaEquipos.setItem(row, 2, QtWidgets.QTableWidgetItem(team_list[i].manager))
            self.tablaEquipos.setItem(row, 3, QtWidgets.QTableWidgetItem(team_list[i].field))

        self.tablaEquipos.sortItems(0)
