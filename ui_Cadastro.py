########################################################### codigo ui_Cadastro.py versão 2.0 ######################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolBox,
    QVBoxLayout, QWidget)


import icons_rc



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1083, 753)
        MainWindow.setStyleSheet(u"background-color: rgb(68, 68, 68);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"border:none;\n"
"}\n"
"\n"
"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, -1, 0, -1)
        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_frame.sizePolicy().hasHeightForWidth())
        self.top_frame.setSizePolicy(sizePolicy)
        self.top_frame.setMaximumSize(QSize(16777215, 16777215))
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        
##################### Botão btn_toggle #############################################################################
        self.btn_toggle = QPushButton(self.top_frame)
        self.btn_toggle.setObjectName(u"btn_toggle")
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon)
        self.btn_toggle.setIconSize(QSize(40, 40))
        self.horizontalLayout_2.addWidget(self.btn_toggle, 0, Qt.AlignLeft)
        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.top_frame)
        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy1)
        self.main_frame.setStyleSheet(u"\n"
"background-color: rgb(125, 125, 125);")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.main_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Pages = QStackedWidget(self.main_frame)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setStyleSheet(u"background-color: rgb(125, 125, 125);")

######################### Pagina HOME #############################################################
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_10 = QVBoxLayout(self.pg_home)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.logo = QLabel(self.pg_home)
        self.logo.setObjectName(u"logo")
        self.verticalLayout_10.addWidget(self.logo)
        self.Pages.addWidget(self.pg_home)

############################ tabWidget / TELA= tab / tela= ibs_cadastramento ########################        
        self.pg_cadastrar = QWidget()
        self.pg_cadastrar.setObjectName(u"pg_cadastrar")
        self.verticalLayout_7 = QVBoxLayout(self.pg_cadastrar)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tabWidget = QTabWidget(self.pg_cadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_9 = QVBoxLayout(self.tab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_4 = QFrame(self.tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(193, 193, 193);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ibs_cadastramento = QLabel(self.frame_4)
        self.ibs_cadastramento.setObjectName(u"ibs_cadastramento")
        self.ibs_cadastramento.setStyleSheet(u"font: 75 28pt \"MS Shell Dlg 2\";")
        self.gridLayout.addWidget(self.ibs_cadastramento, 0, 0, 1, 1)
        self.txt_nome = QLineEdit(self.frame_4)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setMinimumSize(QSize(0, 50))
        self.txt_nome.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout.addWidget(self.txt_nome, 1, 0, 1, 1)
        self.txt_cpf = QLineEdit(self.frame_4)
        self.txt_cpf.setObjectName(u"txt_cpf")
        self.txt_cpf.setMinimumSize(QSize(0, 50))
        self.txt_cpf.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.gridLayout.addWidget(self.txt_cpf, 2, 0, 1, 1)
        self.txt_contato = QLineEdit(self.frame_4)
        self.txt_contato.setObjectName(u"txt_contato")
        self.txt_contato.setMinimumSize(QSize(0, 50))
        self.txt_contato.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout.addWidget(self.txt_contato, 3, 0, 1, 1)
        self.txt_email = QLineEdit(self.frame_4)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setMinimumSize(QSize(0, 50))
        self.txt_email.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout.addWidget(self.txt_email, 4, 0, 1, 1)
        self.verticalLayout_9.addWidget(self.frame_4)

################## BOTÀO EXECUTAR = tabWidget / TELA= tab / BOTÃO= btn_executar1 ######################
        self.btn_executar1 = QPushButton(self.tab)
        self.btn_executar1.setObjectName(u"btn_executar")
        self.btn_executar1.setMinimumSize(QSize(160, 40))
        self.btn_executar1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_executar1.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(147, 147, 147)\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(85, 170, 255);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 15pt \"MS Shell Dlg 2\";\n"
"}")
        self.btn_executar1.setIconSize(QSize(40, 40))
        self.verticalLayout_9.addWidget(self.btn_executar1, 0, Qt.AlignHCenter)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.verticalLayout_9.addItem(self.verticalSpacer_3)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout_7.addWidget(self.tabWidget)

############################ tabWidget / TELA= tab_2 / tela= ibs_listadecadastro ########################
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_8 = QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_3 = QFrame(self.tab_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(193, 193, 193);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ibs_listadecadastro = QLabel(self.frame_3)
        self.ibs_listadecadastro.setObjectName(u"ibs_listadecadastro")
        self.gridLayout_2.addWidget(self.ibs_listadecadastro, 0, 0, 1, 1)
        self.verticalLayout_8.addWidget(self.frame_3)
        self.tableWidget = QTableWidget(self.tab_2)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"\n"
"\n"
"QHeaderView::section{\n"
"background-color: rgb(193, 193, 193);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 15pt \"MS Shell Dlg 2\";\n"
"}\n"
"QTableWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_8.addWidget(self.tableWidget)


############################ BOTÃO Excluir = tabWidget / TELA= tab_2 / BOTÃO= btn_excluir ####################
        self.btn_excluir = QPushButton(self.tab_2)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(160, 40))
        self.btn_excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir.setStyleSheet(u"QPushButton:hover{\n"
"	\n"
"	color: rgb(255, 0, 0);\n"
"	background-color: rgb(147, 147, 147)\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(85, 170, 255);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 15pt \"MS Shell Dlg 2\";\n"
"}")
        self.verticalLayout_8.addWidget(self.btn_excluir, 0, Qt.AlignHCenter)

############################ BOTÃO Gerar Excel = tabWidget / TELA= tab_2 / BOTÃO= btn_excel ####################
        self.btn_excel = QPushButton(self.tab_2)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setMinimumSize(QSize(160, 40))
        self.btn_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excel.setStyleSheet(u"QPushButton:hover{\n"
"	\n"
"	color: rgb(85, 255, 0);\n"
"	background-color: rgb(85, 255, 127)\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(85, 170, 255);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 15pt \"MS Shell Dlg 2\";\n"
"}")
        self.verticalLayout_8.addWidget(self.btn_excel, 0, Qt.AlignHCenter)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.verticalLayout_8.addItem(self.verticalSpacer_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_7.addWidget(self.tabWidget)
        
############################ tabWidget2 / TELA= tab_3 / tela= ibs_lancamentoofertas ########################       
        self.pg_lancar = QWidget()
        self.pg_lancar.setObjectName(u"pg_lancar")
        self.pg_lancar.setStyleSheet(u"background-color: rgb(125, 125, 125);")
        self.verticalLayout_2 = QVBoxLayout(self.pg_lancar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget2 = QTabWidget(self.pg_lancar)
        self.tabWidget2.setObjectName(u"tabWidget2")
        self.tabWidget2.setStyleSheet(u"")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_12 = QVBoxLayout(self.tab_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_6 = QFrame(self.tab_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(193, 193, 193);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.ibs_lancamentoofertas = QLabel(self.frame_6)
        self.ibs_lancamentoofertas.setObjectName(u"ibs_lancamentoofertas")
        self.gridLayout_5.addWidget(self.ibs_lancamentoofertas, 0, 0, 1, 1)
        self.txt_nome2 = QLineEdit(self.frame_6)
        self.txt_nome2.setObjectName(u"txt_nome2")
        self.txt_nome2.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.txt_nome2.setFont(font)
        self.txt_nome2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_5.addWidget(self.txt_nome2, 1, 0, 1, 1)
        self.txt_cpf2 = QLineEdit(self.frame_6)
        self.txt_cpf2.setObjectName(u"txt_cpf2")
        self.txt_cpf2.setMinimumSize(QSize(0, 50))
        font1 = QFont()
        font1.setPointSize(10)
        self.txt_cpf2.setFont(font1)
        self.txt_cpf2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_5.addWidget(self.txt_cpf2, 2, 0, 1, 1)
        self.txt_valor2 = QLineEdit(self.frame_6)
        self.txt_valor2.setObjectName(u"txt_valor2")
        self.txt_valor2.setMinimumSize(QSize(0, 50))
        self.txt_valor2.setFont(font1)
        self.txt_valor2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_5.addWidget(self.txt_valor2, 3, 0, 1, 1)
        self.verticalLayout_12.addWidget(self.frame_6)

################## BOTÀO EXECUTAR = tabWidget2 / TELA= tab_3 / BOTÃO= btn_executar2 ######################
        self.btn_executar2 = QPushButton(self.tab_3)
        self.btn_executar2.setObjectName(u"btn_executar2")
        self.btn_executar2.setMinimumSize(QSize(160, 40))
        self.btn_executar2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_executar2.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(147, 147, 147)\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(85, 170, 255);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 15pt \"MS Shell Dlg 2\";\n"
"}")
        
        self.verticalLayout_12.addWidget(self.btn_executar2, 0, Qt.AlignHCenter)
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.verticalLayout_12.addItem(self.verticalSpacer_5)
        self.tabWidget2.addTab(self.tab_3, "")

############################ tabWidget2 / TELA= tab_4 / tela= ibs_consultasalteracoes ########################
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_11 = QVBoxLayout(self.tab_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.ibs_consultasalteracoes = QLabel(self.tab_4)
        self.ibs_consultasalteracoes.setObjectName(u"ibs_consultasalteracoes")
        self.ibs_consultasalteracoes.setStyleSheet(u"background-color: rgb(193, 193, 193);")

        self.verticalLayout_11.addWidget(self.ibs_consultasalteracoes)

        self.tableWidget2 = QTableWidget(self.tab_4)

        if (self.tableWidget2.columnCount() < 3):
            self.tableWidget2.setColumnCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.Dense7Pattern)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setForeground(brush);
        self.tableWidget2.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        self.tableWidget2.setObjectName(u"tableWidget2")
        self.tableWidget2.setStyleSheet(u"\n"
"\n"
"QHeaderView::section{\n"
"background-color: rgb(193, 193, 193);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 15pt \"MS Shell Dlg 2\";\n"
"}\n"
"QTableWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_11.addWidget(self.tableWidget2)

        self.frame_5 = QFrame(self.tab_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")


############################ BOTÃO Excluir = tabWidget2 / TELA= tab_4 / BOTÃO= btn_excluir2 ####################
        self.btn_excluir2 = QPushButton(self.frame_5)
        self.btn_excluir2.setObjectName(u"btn_excluir2")
        self.btn_excluir2.setMinimumSize(QSize(160, 40))
        self.btn_excluir2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir2.setStyleSheet(u"QPushButton:hover{\n"
"	\n"
"	color: rgb(255, 0, 0);\n"
"	background-color: rgb(147, 147, 147)\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(85, 170, 255);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 15pt \"MS Shell Dlg 2\";\n"
"}")

        self.verticalLayout_6.addWidget(self.btn_excluir2, 0, Qt.AlignHCenter)

############################ BOTÃO Gerar Excel = tabWidget2 / TELA= tab_4 / BOTÃO= btn_excel2 ####################
        self.btn_excel2 = QPushButton(self.frame_5)
        self.btn_excel2.setObjectName(u"btn_excel2")
        self.btn_excel2.setMinimumSize(QSize(160, 40))
        self.btn_excel2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excel2.setStyleSheet(u"QPushButton:hover{\n"
"	\n"
"	color: rgb(85, 255, 0);\n"
"	background-color: rgb(85, 255, 127)\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(85, 170, 255);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 15pt \"MS Shell Dlg 2\";\n"
"}")

        self.verticalLayout_6.addWidget(self.btn_excel2, 0, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)


        self.verticalLayout_11.addWidget(self.frame_5)

        self.tabWidget2.addTab(self.tab_4, "")

        self.verticalLayout_2.addWidget(self.tabWidget2)

        self.Pages.addWidget(self.pg_lancar)

################################# Pagina SOBRE ######################################
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.label_8 = QLabel(self.pg_sobre)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(90, 0, 571, 51))
        self.label_9 = QLabel(self.pg_sobre)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 60, 821, 521))
        self.label_9.setStyleSheet(u"background-color: rgb(193, 193, 193);")
        self.label_9.setWordWrap(True)
        self.Pages.addWidget(self.pg_sobre)

        self.verticalLayout_5.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.footer_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footer_frame)


        self.gridLayout_3.addWidget(self.main_container, 0, 1, 1, 1)

        self.left_menu = QFrame(self.centralwidget)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMaximumSize(QSize(9, 16777215))
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.left_menu)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(11, -1, 0, -1)
        self.frame = QFrame(self.left_menu)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(11, -1, 0, 10)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_13.addWidget(self.label_3)


        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.left_menu)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 116, 460))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, -1, -1)

######################## BOTÃO HOME #####################################################
        self.btn_home = QPushButton(self.page)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setEnabled(True)
        self.btn_home.setMinimumSize(QSize(0, 30))
        self.btn_home.setSizeIncrement(QSize(0, 0))
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dlg 2"])
        font2.setPointSize(15)
        font2.setBold(False)
        font2.setItalic(False)
        self.btn_home.setFont(font2)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(147, 147, 147)\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(85, 170, 255);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 15pt \"MS Shell Dlg 2\";\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_home)

##############################  BOTÃO CADASTRAR ###########################################
        self.btn_cadastrar = QPushButton(self.page)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 30))
        self.btn_cadastrar.setSizeIncrement(QSize(0, 0))
        self.btn_cadastrar.setFont(font2)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(147, 147, 147)\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(85, 170, 255);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 15pt \"MS Shell Dlg 2\";\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_cadastrar)

################################## BOTÃO LANCAR ###########################################
        self.btn_lancar = QPushButton(self.page)
        self.btn_lancar.setObjectName(u"btn_lancar")
        self.btn_lancar.setMinimumSize(QSize(0, 30))
        self.btn_lancar.setSizeIncrement(QSize(0, 0))
        self.btn_lancar.setFont(font2)
        self.btn_lancar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_lancar.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(147, 147, 147)\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(85, 170, 255);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 15pt \"MS Shell Dlg 2\";\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_lancar)

####################################### BOTÃO SOBRE ######################################
        self.btn_sobre = QPushButton(self.page)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 30))
        self.btn_sobre.setSizeIncrement(QSize(0, 0))
        self.btn_sobre.setFont(font2)
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sobre.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(147, 147, 147)\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(85, 170, 255);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 15pt \"MS Shell Dlg 2\";\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

####################### PAGINA 2 CONTATOS #################################################

        self.toolBox.addItem(self.page, u"Page 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setEnabled(True)
        self.page_2.setGeometry(QRect(0, 0, 16, 481))
        self.page_2.setMaximumSize(QSize(16777215, 16777215))
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 30, 181, 351))
        self.label_5.setToolTipDuration(5)
        self.label_5.setStyleSheet(u"")
        self.toolBox.addItem(self.page_2, u"Page 2")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.gridLayout_4.addWidget(self.frame_2, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.left_menu, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget2.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
  
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; vertical-align:super;\">Sistema de Cadastro </span></p></body></html>", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/iconeg.png\"/></p></body></html>", None))
        self.ibs_cadastramento.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">Cadastro de Membros Religiosos</span></p></body></html>", None))
        self.txt_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.txt_cpf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.txt_contato.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contato", None))
        self.txt_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.btn_executar1.setText(QCoreApplication.translate("MainWindow", u"Executar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.ibs_listadecadastro.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">Cadastros</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Contato", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Verificar Cadastros", None))
        self.ibs_lancamentoofertas.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">Lançamento Oferta</span></p></body></html>", None))
        self.txt_nome2.setText("")
        self.txt_nome2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.txt_cpf2.setText("")
        self.txt_cpf2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.txt_valor2.setText("")
        self.txt_valor2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Valor", None))
        self.btn_executar2.setText(QCoreApplication.translate("MainWindow", u"Executar", None))
        self.tabWidget2.setTabText(self.tabWidget2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Lançar", None))
        self.ibs_consultasalteracoes.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">Consultar Lançamentos</span></p></body></html>", None))
        ___qtablewidgetitem4 = self.tableWidget2.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem5 = self.tableWidget2.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem6 = self.tableWidget2.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Valor", None));
        self.btn_excluir2.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btn_excel2.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.tabWidget2.setTabText(self.tabWidget2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Cosultar Lançamentos", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">Sobre nossa Historia</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-family:'Arial,sans-serif'; font-size:14pt; font-weight:600; text-decoration: underline; color:#444444;\">Fundada em 1\u00b0 de janeiro de 1923</span><span style=\" font-family:'Arial,sans-serif'; font-size:11pt; font-weight:600; color:#444444;\">, com a inaugura\u00e7\u00e3o de sua sede internacional\u00a0</span><span style=\" font-family:'Arial,sans-serif'; font-size:11pt; font-weight:600; font-style:italic; color:#444444;\">Angelus Temple</span><span style=\" font-family:'Arial,sans-serif'; font-size:11pt; font-weight:600; color:#444444;\">, em Los Angeles, Calif\u00f3rnia; a Igreja do Evangelho nasceu no cora\u00e7\u00e3o de Deus e foi confiada \u00e0s m\u00e3os da evangelista Aim\u00e9e Semple McPherson, conhecida como &quot;Irm\u00e3 Aimee&quot; que, em seu minist\u00e9rio, foi respons\u00e1vel por diversas a\u00e7\u00f5es que resultaram em grandes impactos evangel\u00edsticos, a Igreja formou a Fraternidade Pentecostal da Am\u00e9rica do"
                        " Norte, em 1948, em uma alian\u00e7a com a Assembleia de Deus, a Igreja de Deus, a Open Bible Standard Churches, a Igreja Internacional Pentecostal de Santidade, entre outras. Hoje, j\u00e1 existem igrejas em todos os Estados norte-americanos, al\u00e9m de outras tantas espalhadas por 146 pa\u00edses.</span></p><p><span style=\" font-family:'Arial,sans-serif'; font-size:14pt; font-weight:600; text-decoration: underline; color:#444444;\">Chegada ao Brasil </span><span style=\" font-family:'Arial,sans-serif'; font-size:14pt; font-weight:600; text-decoration: underline; color:#444444;\">No Brasil</span><span style=\" font-family:'Arial,sans-serif'; font-size:12pt; font-weight:600; color:#444444;\">,</span><span style=\" font-family:'Arial,sans-serif'; font-size:11pt; font-weight:600; color:#444444;\"> o Evangelho  teve in\u00edcio com o pastor Harold Williams e sua esposa, Mary Williams, que vieram ao Pa\u00eds inspirados a levar a Palavra de Deus e salvar almas para Cristo. No come\u00e7"
                        "o, n\u00e3o foi f\u00e1cil. Passaram por diversas prova\u00e7\u00f5es e desafios, mas sempre guiados pela luz divina. A primeira parada na Am\u00e9rica do Sul se deu na Bol\u00edvia, onde pregaram os ensinamentos do Senhor por um ano. Por alguma raz\u00e3o, eles sentiam que este n\u00e3o era o lugar onde Deus os desejava.</span></p><p><span style=\" font-family:'Arial,sans-serif'; font-size:14pt; font-weight:600; text-decoration: underline; color:#444444;\">Hoje, </span><span style=\" font-family:'Arial,sans-serif'; font-size:14pt; font-weight:600; color:#444444;\"/><span style=\" font-family:'Arial,sans-serif'; font-size:11pt; font-weight:600; color:#444444;\">Em quase 70 anos de sua funda\u00e7\u00e3o, a Igreja do Evangelho possui mais de 17 mil templos e obras abertas e estruturadas em todo o Pa\u00eds. Mais de 30 mil obreiros est\u00e3o levando os ensinamentos de Jesus a mais de dois milh\u00f5es de pessoas em 22 na\u00e7\u00f5es.</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/icons/iconeP.ico\"/><span style=\" font-size:12pt; font-weight:600; vertical-align:super;\">Sistema de Cadastro</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/icone.ico\"/></p></body></html>", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_lancar.setText(QCoreApplication.translate("MainWindow", u"Lançar", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">D\u00favidas contatos:</span></p><p align=\"center\"><br/></p><p align=\"center\"><img src=\":/icons/icons/whats-app.ico\"/></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; vertical-align:super;\">(19)99750-2687</span></p><p align=\"center\"><br/></p><p align=\"center\"><img src=\":/icons/icons/email.ico\"/></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; vertical-align:super;\">alexandremachadosgj@gmail.com</span></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.Pages.addWidget(self.pg_cadastrar)