import arcpy
import pythonaddins

#CREATED BY:    Blake Harcourt
#DATE CREATED:  20/11/2015
#DATE LAST UPDATED: 20/01/2016
#VERSION:   0.2
#DESCRIPTION:   This script allows for the table of contents (TOC) to be searched in Arcmap using a keyword.
                #If a layer name matches or contains the keyword it will be turned on and counted.
                #A layer that is in a group layer will also be turned on if it matches the criteria.

class ComboBoxClass1(object):
    """Implementation for Blake_Search_Tool_addin.combobox (ComboBox)"""
    def __init__(self):
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'WWWWWW'       #THE WIDTH OF THE COMBO-BOX
        self.width = 'WWWWWW'               #THE WIDTH OF THE COMBO-BOX
    def onSelChange(self, selection):
        pass
    def onEditChange(self, text):
        pass
    def onFocus(self, focused):
        pass
    def onEnter(self):
        mxd = arcpy.mapping.MapDocument("CURRENT")  #USE THE SCRIPT ON THE CURRENT MAP
        layers = arcpy.mapping.ListLayers(mxd, "*") #SCAN ACROSS ALL LAYERS
        KEYWORD = self.value                        #KEYWORD IS THE STRING ENTERED IN THE COMBO-BOX
        COUNT = 0                                   #RESETS THE COUNT VALUE WHEN THE SCRIPT IS STARTED
        print("Script Created By Blake Harcourt")
        print("Keyword = "+str(KEYWORD))
        print("Searching For Keyword Matches")
        for layer in layers:                        #TURNS OFF VISIBILITY OF ALL LAYERS
            layer.visible = False

        for layer in layers:                        #SEARCHES FOR KEYWORD MATCHES
            if layer.name == KEYWORD:               #Example: A = A
                layer.visible = True
                print("Match Found")
                COUNT = (COUNT + 1)
            elif KEYWORD in layer.name:             #Example: A = Apple
                layer.visible = True
                print("Match Found")
                COUNT = (COUNT + 1)
            elif KEYWORD.lower() == layer.name.lower():     #Example: a = A
                layer.visible = True
                print("Match Found")
                COUNT = (COUNT + 1)
            elif KEYWORD.lower() in layer.name.lower():     #Example: b = aBc
                layer.visible = True
                print("Match Found")
                COUNT = (COUNT + 1)

        for G_layer in layers:                      #SEARCHES FOR KEYWORD MATCHES WITHIN GROUP LAYERS
            if G_layer.isGroupLayer:
                for subLayer in G_layer:
                    if subLayer.name == KEYWORD:
                        G_layer.visible = True
                    elif KEYWORD in subLayer.name:
                        G_layer.visible = True
                    elif KEYWORD.lower() == subLayer.name.lower():
                        G_layer.visible = True
                    elif KEYWORD.lower() in subLayer.name.lower():
                        G_layer.visible = True

        arcpy.RefreshTOC()                          #REFRESH THE TABLE OF CONTENTS
        arcpy.RefreshActiveView()                   #REFRESH THE ACTIVE DATA FRAME
        print ("Number of Matches = "+str(COUNT))   #DISPLAY NUMBER OF MATCHES FOUND
