#-*- coding:UTF-8 -*-

import maya.cmds as cmds

def main(idType="vrayObjectID"):
    """
    #arg
    idType = "vrayObjectID" or "vrayMaterialId"
    """
    # ���ʂ𗭂ߍ��ރ��X�g
    results = []

    # �m�[�h���擾���A�ʂɃ��[�v�ɂ�����
    if idType == "vrayMaterialId":
        nodes = cmds.ls(materials=1)
    else:
        nodes = cmds.ls(dag=1)
        
    for node in nodes:
        # vrayObjectID�A�g���r���[�g���Ȃ���΃X�L�b�v
        if not cmds.attributeQuery(idType, node=node, exists=1):
            continue

        vrayID = cmds.getAttr("{0}.{1}".format(node,idType))

        # ���ʃI�u�W�F�N�g�𗭂ߍ���
        results.append([vrayID,node])

    # ���ʂ�Ԃ�
    return results 
