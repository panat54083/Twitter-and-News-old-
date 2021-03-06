# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New_data.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TwitterAndNews(object):
    def setupUi(self, TwitterAndNews):
        TwitterAndNews.setObjectName("TwitterAndNews")
        TwitterAndNews.resize(1220, 858)
        font = QtGui.QFont()
        font.setPointSize(11)
        TwitterAndNews.setFont(font)
        self.centralwidget = QtWidgets.QWidget(TwitterAndNews)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.inputTxt_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.inputTxt_2.setMinimumSize(QtCore.QSize(300, 0))
        self.inputTxt_2.setObjectName("inputTxt_2")
        self.gridLayout.addWidget(self.inputTxt_2, 2, 0, 1, 1)
        self.Search_bt_news = QtWidgets.QPushButton(self.centralwidget)
        self.Search_bt_news.setMinimumSize(QtCore.QSize(100, 0))
        self.Search_bt_news.setObjectName("Search_bt_news")
        self.gridLayout.addWidget(self.Search_bt_news, 2, 2, 1, 1)
        self.langBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.langBox_2.setObjectName("langBox_2")
        self.gridLayout.addWidget(self.langBox_2, 2, 1, 1, 1)
        self.Search_bt_tw = QtWidgets.QPushButton(self.centralwidget)
        self.Search_bt_tw.setMinimumSize(QtCore.QSize(100, 0))
        self.Search_bt_tw.setObjectName("Search_bt_tw")
        self.gridLayout.addWidget(self.Search_bt_tw, 1, 2, 1, 1)
        self.inputTxt = QtWidgets.QLineEdit(self.centralwidget)
        self.inputTxt.setMinimumSize(QtCore.QSize(300, 0))
        self.inputTxt.setObjectName("inputTxt")
        self.gridLayout.addWidget(self.inputTxt, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 2)
        self.langBox = QtWidgets.QComboBox(self.centralwidget)
        self.langBox.setObjectName("langBox")
        self.gridLayout.addWidget(self.langBox, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.start_lb = QtWidgets.QLabel(self.centralwidget)
        self.start_lb.setObjectName("start_lb")
        self.horizontalLayout_2.addWidget(self.start_lb)
        self.start_edit = QtWidgets.QDateEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_edit.sizePolicy().hasHeightForWidth())
        self.start_edit.setSizePolicy(sizePolicy)
        self.start_edit.setMinimumSize(QtCore.QSize(100, 0))
        self.start_edit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.start_edit.setCalendarPopup(True)
        self.start_edit.setObjectName("start_edit")
        self.horizontalLayout_2.addWidget(self.start_edit)
        self.end_lb = QtWidgets.QLabel(self.centralwidget)
        self.end_lb.setObjectName("end_lb")
        self.horizontalLayout_2.addWidget(self.end_lb)
        self.end_edit = QtWidgets.QDateEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_edit.sizePolicy().hasHeightForWidth())
        self.end_edit.setSizePolicy(sizePolicy)
        self.end_edit.setMinimumSize(QtCore.QSize(100, 0))
        self.end_edit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.end_edit.setCalendarPopup(True)
        self.end_edit.setObjectName("end_edit")
        self.horizontalLayout_2.addWidget(self.end_edit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 3)
        self.progressBar_news = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_news.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.progressBar_news.setProperty("value", 24)
        self.progressBar_news.setObjectName("progressBar_news")
        self.gridLayout.addWidget(self.progressBar_news, 6, 0, 1, 3)
        self.progressBar_tw = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_tw.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.progressBar_tw.setProperty("value", 24)
        self.progressBar_tw.setObjectName("progressBar_tw")
        self.gridLayout.addWidget(self.progressBar_tw, 5, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.gridLayout_7.addLayout(self.gridLayout, 0, 3, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMaximumSize(QtCore.QSize(200, 200))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../news_icon.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout_7.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMaximumSize(QtCore.QSize(200, 200))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../twitter_icon.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout_7.addWidget(self.label_5, 0, 7, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem1, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem2, 0, 6, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem3, 0, 8, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.stock_lb = QtWidgets.QLabel(self.centralwidget)
        self.stock_lb.setMinimumSize(QtCore.QSize(0, 25))
        self.stock_lb.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.stock_lb.setFont(font)
        self.stock_lb.setObjectName("stock_lb")
        self.gridLayout_5.addWidget(self.stock_lb, 0, 0, 1, 4)
        self.stock_search = QtWidgets.QPushButton(self.centralwidget)
        self.stock_search.setObjectName("stock_search")
        self.gridLayout_5.addWidget(self.stock_search, 1, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem4, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(10, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem5, 3, 3, 1, 1)
        self.stock_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.stock_lineEdit.setObjectName("stock_lineEdit")
        self.gridLayout_5.addWidget(self.stock_lineEdit, 1, 1, 1, 2)
        self.progressBar_stock = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_stock.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.progressBar_stock.setProperty("value", 24)
        self.progressBar_stock.setObjectName("progressBar_stock")
        self.gridLayout_5.addWidget(self.progressBar_stock, 2, 3, 1, 1)
        self.StockView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StockView.sizePolicy().hasHeightForWidth())
        self.StockView.setSizePolicy(sizePolicy)
        self.StockView.setObjectName("StockView")
        self.gridLayout_5.addWidget(self.StockView, 2, 0, 2, 3)
        self.gridLayout_7.addLayout(self.gridLayout_5, 3, 4, 1, 5)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.show_bt = QtWidgets.QPushButton(self.centralwidget)
        self.show_bt.setMaximumSize(QtCore.QSize(100, 16777215))
        self.show_bt.setObjectName("show_bt")
        self.gridLayout_6.addWidget(self.show_bt, 1, 2, 1, 1)
        self.viewGraph = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewGraph.sizePolicy().hasHeightForWidth())
        self.viewGraph.setSizePolicy(sizePolicy)
        self.viewGraph.setMinimumSize(QtCore.QSize(350, 0))
        self.viewGraph.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.viewGraph.setObjectName("viewGraph")
        self.gridLayout_6.addWidget(self.viewGraph, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem6, 1, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 48, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem7, 3, 2, 1, 1)
        self.Graph_lb = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Graph_lb.setFont(font)
        self.Graph_lb.setObjectName("Graph_lb")
        self.gridLayout_6.addWidget(self.Graph_lb, 0, 0, 1, 3)
        self.progressBar_locate = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_locate.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.progressBar_locate.setProperty("value", 24)
        self.progressBar_locate.setObjectName("progressBar_locate")
        self.gridLayout_6.addWidget(self.progressBar_locate, 2, 2, 1, 1)
        self.GraphView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GraphView.sizePolicy().hasHeightForWidth())
        self.GraphView.setSizePolicy(sizePolicy)
        self.GraphView.setObjectName("GraphView")
        self.gridLayout_6.addWidget(self.GraphView, 2, 0, 2, 2)
        self.gridLayout_7.addLayout(self.gridLayout_6, 3, 0, 1, 4)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.list_trend_th = QtWidgets.QListWidget(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_trend_th.sizePolicy().hasHeightForWidth())
        self.list_trend_th.setSizePolicy(sizePolicy)
        self.list_trend_th.setObjectName("list_trend_th")
        self.gridLayout_8.addWidget(self.list_trend_th, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.list_trend_us = QtWidgets.QListWidget(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_trend_us.sizePolicy().hasHeightForWidth())
        self.list_trend_us.setSizePolicy(sizePolicy)
        self.list_trend_us.setObjectName("list_trend_us")
        self.gridLayout_10.addWidget(self.list_trend_us, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.gridLayout_2.addWidget(self.tabWidget_2, 2, 0, 1, 1)
        self.data_lb = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.data_lb.setFont(font)
        self.data_lb.setObjectName("data_lb")
        self.gridLayout_2.addWidget(self.data_lb, 0, 1, 1, 1)
        self.Update_trend_lb = QtWidgets.QLabel(self.centralwidget)
        self.Update_trend_lb.setText("")
        self.Update_trend_lb.setObjectName("Update_trend_lb")
        self.gridLayout_2.addWidget(self.Update_trend_lb, 1, 0, 1, 1)
        self.top_lb = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.top_lb.setFont(font)
        self.top_lb.setObjectName("top_lb")
        self.gridLayout_2.addWidget(self.top_lb, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tw_tab = QtWidgets.QWidget()
        self.tw_tab.setObjectName("tw_tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tw_tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.tw_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1)
        self.SentView_tw = QtWebEngineWidgets.QWebEngineView(self.tw_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SentView_tw.sizePolicy().hasHeightForWidth())
        self.SentView_tw.setSizePolicy(sizePolicy)
        self.SentView_tw.setMinimumSize(QtCore.QSize(250, 200))
        self.SentView_tw.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.SentView_tw.setFont(font)
        self.SentView_tw.setObjectName("SentView_tw")
        self.gridLayout_3.addWidget(self.SentView_tw, 2, 1, 1, 1)
        self.TwView = QtWebEngineWidgets.QWebEngineView(self.tw_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TwView.sizePolicy().hasHeightForWidth())
        self.TwView.setSizePolicy(sizePolicy)
        self.TwView.setObjectName("TwView")
        self.gridLayout_3.addWidget(self.TwView, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tw_tab, "")
        self.news_tab = QtWidgets.QWidget()
        self.news_tab.setObjectName("news_tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.news_tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_3 = QtWidgets.QLabel(self.news_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 1, 1, 1)
        self.NewsView = QtWebEngineWidgets.QWebEngineView(self.news_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NewsView.sizePolicy().hasHeightForWidth())
        self.NewsView.setSizePolicy(sizePolicy)
        self.NewsView.setObjectName("NewsView")
        self.gridLayout_4.addWidget(self.NewsView, 2, 0, 1, 1)
        self.SentView_news = QtWebEngineWidgets.QWebEngineView(self.news_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SentView_news.sizePolicy().hasHeightForWidth())
        self.SentView_news.setSizePolicy(sizePolicy)
        self.SentView_news.setMinimumSize(QtCore.QSize(250, 200))
        self.SentView_news.setMaximumSize(QtCore.QSize(400, 16777215))
        self.SentView_news.setObjectName("SentView_news")
        self.gridLayout_4.addWidget(self.SentView_news, 2, 1, 1, 1)
        self.tabWidget.addTab(self.news_tab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 1, 1, 2, 1)
        self.gridLayout_7.addLayout(self.gridLayout_2, 2, 0, 1, 9)
        TwitterAndNews.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TwitterAndNews)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1220, 21))
        self.menubar.setObjectName("menubar")
        TwitterAndNews.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TwitterAndNews)
        self.statusbar.setObjectName("statusbar")
        TwitterAndNews.setStatusBar(self.statusbar)

        self.retranslateUi(TwitterAndNews)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TwitterAndNews)

    def retranslateUi(self, TwitterAndNews):
        _translate = QtCore.QCoreApplication.translate
        TwitterAndNews.setWindowTitle(_translate("TwitterAndNews", "MainWindow"))
        self.Search_bt_news.setText(_translate("TwitterAndNews", "News"))
        self.Search_bt_tw.setText(_translate("TwitterAndNews", "Twitter"))
        self.start_lb.setText(_translate("TwitterAndNews", "Start"))
        self.end_lb.setText(_translate("TwitterAndNews", "End"))
        self.progressBar_news.setFormat(_translate("TwitterAndNews", "%p% News"))
        self.progressBar_tw.setFormat(_translate("TwitterAndNews", "%p% Twitter"))
        self.label.setText(_translate("TwitterAndNews", "Search"))
        self.stock_lb.setText(_translate("TwitterAndNews", "Stock"))
        self.stock_search.setText(_translate("TwitterAndNews", "Search"))
        self.show_bt.setText(_translate("TwitterAndNews", "Show"))
        self.Graph_lb.setText(_translate("TwitterAndNews", "Graph"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("TwitterAndNews", "TH"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("TwitterAndNews", "US"))
        self.data_lb.setText(_translate("TwitterAndNews", "Data"))
        self.top_lb.setText(_translate("TwitterAndNews", "Top Trend"))
        self.label_2.setText(_translate("TwitterAndNews", "Sentiment"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tw_tab), _translate("TwitterAndNews", "Twitter"))
        self.label_3.setText(_translate("TwitterAndNews", "Sentiment"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.news_tab), _translate("TwitterAndNews", "News"))
from PyQt5 import QtWebEngineWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TwitterAndNews = QtWidgets.QMainWindow()
    ui = Ui_TwitterAndNews()
    ui.setupUi(TwitterAndNews)
    TwitterAndNews.show()
    sys.exit(app.exec_())
