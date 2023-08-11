import window
import fun
import filetype
import os

filePaths = []


def run():
    global filePaths

    if window.svo_selectFolder.get() == "":
        window.messagebox.showinfo("提示", "请选择目录")
        return

    # 状态改变
    window.svo_status.set("状态：运行")

    filePaths = fun.getFilePaths(window.svo_selectFolder.get())

    for filePath in filePaths:
        kind = filetype.guess(filePath)
        suffix = os.path.splitext(filePath)[1]
        if suffix != "." + kind.extension:
            os.rename(filePath, os.path.splitext(filePath)[0] + "." + kind.extension)

    window.messagebox.showinfo("提示", "修复完成！")
    window.svo_status.set("状态：空闲")
    return
