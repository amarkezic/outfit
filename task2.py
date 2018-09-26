import maya.cmds as cmds

file_path = cmds.fileDialog2(fm=3)
result = cmds.ls(sl=True)
for fileName in result:
    path = str(file_path[0]+"/"+fileName+".fbx")
    cmds.file(path, es = True, force=True, type = "FBX export", options="v=0;", pr=True)