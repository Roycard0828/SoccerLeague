from .ventana_principal import *
from .ventana_actualizar import Ui_ActualizarWIndow
from .mensaje_exitoso import Ui_Dialog_Success_Message
from .mensaje_error_borrarEquipo import Ui_Dialog_Delete_Message
from ..BusinessLogic.team_controller import TeamController
from ..BusinessLogic.match_controller import MatchController
from ..BusinessLogic.positions_table_controller import PositionsTableController
from ..BusinessLogic.positions_table_logic import start_season, end_soccer_day


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.widget = QtWidgets.QMainWindow()
        self.load_positions_table()

        # Select page from the StackWidget
        self.BtnEquipo.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PaginaEquipos))
        self.BtnTabla.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PaginaTabla))
        self.BtnJornada.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PaginaJornada))

        # CRUD buttons
        self.BtnInsertar.clicked.connect(lambda: self.add_team())
        self.BtnActualizar.clicked.connect(lambda: self.update_team())
        self.btnlistar.clicked.connect(lambda: self.load_teams_table())
        self.BtnBorrar.clicked.connect(lambda: self.delete_team())

        # Match buttons
        self.BtnBuscarJornada.clicked.connect(lambda: self.load_match_table())
        self.BtnAsignarResultado.clicked.connect(lambda: self.write_result())
        self.BtnActualizarDatos.clicked.connect(lambda: self.update_results())

        # Start season buttons
        self.BtnEmpezarTorneo.clicked.connect(lambda: self.start_season())
        # End the soccer day
        self.BtnTerminarJornada.clicked.connect(lambda: self.end_soccer_day())

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

    # Methods for match operations
    def load_match_table(self):
        soccer_day_number = int(self.NumJornada.text())
        match_list = MatchController.get_all_matches_by_day_number(soccer_day_number)
        self.TablaPartidos.setRowCount(len(match_list))
        for i in range(0, len(match_list)):
            self.TablaPartidos.setItem(i, 0, QtWidgets.QTableWidgetItem(match_list[i].local_team.name))
            self.TablaPartidos.setItem(i, 1, QtWidgets.QTableWidgetItem(match_list[i].visiting_team.name))
            self.TablaPartidos.setItem(i, 2, QtWidgets.QTableWidgetItem(match_list[i].field))
            self.TablaPartidos.setItem(i, 3, QtWidgets.QTableWidgetItem(match_list[i].result))

    def write_result(self):
        result = self.TxtResultado.toPlainText()
        self.TablaPartidos.currentItem().setText(result)

    def update_results(self):
        soccer_day_number = int(self.NumJornada.text())
        match_list = MatchController.get_all_matches_by_day_number(soccer_day_number)
        for i in range(0, len(match_list)):
            id = match_list[i].id
            result = self.TablaPartidos.item(i, 3).text()
            MatchController.update_result(id, result)

        self.successful_message_dialog()

    # Positions table methods
    def load_positions_table(self):
        team_list = PositionsTableController.read_all_teams()
        self.TablaGeneral.setRowCount(len(team_list))
        for i in range(0, len(team_list)):
            self.TablaGeneral.setItem(i, 0, QtWidgets.QTableWidgetItem(team_list[i].team.name))
            self.TablaGeneral.setItem(i, 1, QtWidgets.QTableWidgetItem(str(team_list[i].matches_played)))
            self.TablaGeneral.setItem(i, 2, QtWidgets.QTableWidgetItem(str(team_list[i].matches_lost)))
            self.TablaGeneral.setItem(i, 3, QtWidgets.QTableWidgetItem(str(team_list[i].tied_matches)))
            self.TablaGeneral.setItem(i, 4, QtWidgets.QTableWidgetItem(str(team_list[i].matches_won)))
            self.TablaGeneral.setItem(i, 5, QtWidgets.QTableWidgetItem(str(team_list[i].goals)))
            self.TablaGeneral.setItem(i, 6, QtWidgets.QTableWidgetItem(str(team_list[i].points)))

    def start_season(self):
        start_season()
        self.load_positions_table()
        self.successful_message_dialog()

    def end_soccer_day(self):
        soccer_day_number = int(self.NumJornada.text())
        end_soccer_day(soccer_day_number)
        self.load_positions_table()
        self.successful_message_dialog()

