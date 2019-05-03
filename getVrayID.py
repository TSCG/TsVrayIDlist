#-*- coding:UTF-8 -*-

import maya.cmds as cmds

def main(idType="vrayObjectID"):
    """
    #arg
    idType = "vrayObjectID" or "vrayMaterialId"
    """
    # 結果を溜め込むリスト
    results = []

    # ノードを取得し、個別にループにかける
    if idType == "vrayMaterialId":
        nodes = cmds.ls(materials=1)
    else:
        nodes = cmds.ls(dag=1)
        
    for node in nodes:
        # vrayObjectIDアトリビュートがなければスキップ
        if not cmds.attributeQuery(idType, node=node, exists=1):
            continue

        vrayID = cmds.getAttr("{0}.{1}".format(node,idType))

        # 結果オブジェクトを溜め込む
        results.append([vrayID,node])

    # 結果を返す
    return results 
