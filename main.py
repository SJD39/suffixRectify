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
        if kind is None:
            continue

        suffix = os.path.splitext(filePath)[1]
        
        if suffix != "." + kind.extension:
            # 补丁：zip文件后缀带z都算正确格式
            if kind.extension == 'zip' and 'z' in suffix:
                continue

            os.rename(filePath, os.path.splitext(filePath)[0] + "." + kind.extension)

    window.messagebox.showinfo("提示", "修复完成！")
    window.svo_status.set("状态：空闲")
    return
