#-*- coding:UTF-8 -*-
__tool_version__ = "1.0.1"

import os

###### GUI Modules
import maya.OpenMayaUI as OpenMayaUI
try:
    from PySide           import QtCore, QtGui
    from PySide.QtUiTools import QUiLoader
    import shiboken
except ImportError:
    from PySide2           import QtCore, QtGui
    from PySide2.QtUiTools import QUiLoader
    import shiboken2 as shiboken   
    
###### Tool Modules
import maya.cmds as cmds

###### Custom Modules
import getVrayID
import logVrayID


class GUI(QtGui.QMainWindow):
    def __init__(self, parent=None):
	super(GUI, self).__init__(parent)
    
	# ui File Road
	loader = QUiLoader()
	
	uiPath = os.path.dirname(os.path.abspath(__file__))
	uiFilePath = uiPath + '/MainWindow.ui'	
	self.UI = loader.load(uiFilePath)
	self.setCentralWidget(self.UI)
	
	self.setWindowTitle("Ts_VrayIDlist {0}".format(__tool_version__))
	self.resize(480, 600) # window Size
	
	self.setupUi()
	self.connectSignals() # set Signals



    def setupUi(self, *args, **kwargs):
	"""
	DESCRIPTION : GUIの処理
	ARGUMENTS : None : None
	RETURN 
	"""
	
	#Set QStandardItemModel
	self.stdItemModel = QtGui.QStandardItemModel( 0, 2, self )
	self.stdItemModel.setHeaderData( 0, QtCore.Qt.Horizontal, 'VrayID' )
	self.stdItemModel.setHeaderData( 1, QtCore.Qt.Horizontal, 'Item Name' )
	self.UI.itemList.setModel( self.stdItemModel )

    
    def connectSignals(self, *args, **kwargs):
	"""
	DESCRIPTION : GUIのシグナル-スロット接続処理
	ARGUMENTS : None : None
	RETURN 
	"""
	self.UI.setList.clicked.connect(self.setItmList)
	self.UI.selectItem.clicked.connect(self.selectItem)
	self.UI.elementList.clicked.connect(self.elementList)
	

    def selectItem(self, *args, **kwargs):
	selList = []

	for item in self.UI.itemList.selectedIndexes():
	    if item.column():
		selList.append( item.data() )

	cmds.select( selList, r=True )
	    
	
    def delItmList(self, *args, **kwargs):
	self.stdItemModel.removeRows(0, self.UI.itemList.model().rowCount() )	
	
    def setItmList(self, *args, **kwargs):
	idType = "vrayObjectID"

	if self.UI.matID.isChecked():
	    idType = "vrayMaterialId"
	
	self.delItmList()
	
	index = 0
	for item in getVrayID.main( idType ):
	    self.stdItemModel.setItem( index, 0, QtGui.QStandardItem( str(item[0]) ) )
	    self.stdItemModel.setItem( index, 1, QtGui.QStandardItem( item[1] ) )
	    index += 1	
	    
    def elementList(self, *args, **kwargs):
	logVrayID.main()



def main():	
    ptr = OpenMayaUI.MQtUtil.mainWindow()
    parent = shiboken.wrapInstance(long(ptr), QtGui.QWidget)
    
    try:
	    view.close()
	    view = GUI(parent)
	    view.show()
    except:	
	    view = GUI(parent)
	    view.show()	

