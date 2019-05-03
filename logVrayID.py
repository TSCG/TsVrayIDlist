#-*- coding:UTF-8 -*-

###### Tool Modules
import maya.cmds as cmds

def main():
    list = cmds.ls(type="VRayRenderElement")
    
    print "----- Element Multimatte List -----" 
    for i in list:
        if cmds.getAttr("{0}.vrayClassType".format(i)) == "MultiMatteElement":
            
            if cmds.getAttr("{0}.vray_usematid_multimatte".format(i)):
                type = "Mat ID"
            else:
                type = "Obj ID"
                
            name = cmds.getAttr("{0}.vray_name_multimatte".format(i))
            R_ID = cmds.getAttr("{0}.vray_redid_multimatte".format(i))
            G_ID = cmds.getAttr("{0}.vray_greenid_multimatte".format(i))
            B_ID = cmds.getAttr("{0}.vray_blueid_multimatte".format(i))
            
            print "[{0}]".format( i )
            print "  type : {0}".format( type )
            print "  name : {0}".format( name )
            print "  R_ID : {0}".format( R_ID )
            print "  G_ID : {0}".format( G_ID )
            print "  B_ID : {0}\n".format( B_ID )
            
    print "-----------------------------------"
