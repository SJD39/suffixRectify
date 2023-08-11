import main
import os
import tkinter
import tkinter.ttk
from tkinter import messagebox
from tkinter import filedialog


# 联系
def contact():
    messagebox.showinfo("保持联系", "建议与我们保持联系以及时获得新的内容或BUG修复\rQ群：609062643\rQQ：3069935480")


# 选择输出文件夹
def selectFolder():
    folder = filedialog.askdirectory()
    if folder == "":
        return
    svo_selectFolder.set(folder)
    return


# 打开图片文件夹
def openFolder():
    path = svo_selectFolder.get()
    if path == "":
        return
    os.system("start " + path)
    return


window = tkinter.Tk()
window.title("文件后缀更正1.0")

svo_selectFolder = tkinter.StringVar()
svo_status = tkinter.StringVar(value="状态：空闲")

lbl_selectFolder = tkinter.ttk.Label(window, text="目标文件夹：")
lbl_status = tkinter.ttk.Label(window, textvariable=svo_status)

txt_selectFolder = tkinter.ttk.Entry(window, textvariable=svo_selectFolder, width=48)

btn_run = tkinter.ttk.Button(window, text="运行", command=main.run)
btn_contact = tkinter.ttk.Button(window, text="保持联系", command=contact)
btn_selectFolder = tkinter.ttk.Button(window, text="选择文件夹", command=selectFolder)
btn_openFolder = tkinter.ttk.Button(window, text="打开文件夹", command=openFolder)

prg_progressbar = tkinter.ttk.Progressbar(window, length=560)

btn_selectFolder.grid(row=0, column=0, padx=5, pady=5)
btn_openFolder.grid(row=0, column=1, padx=5, pady=5)
btn_run.grid(row=0, column=2, padx=5, pady=5)
lbl_status.grid(row=0, column=3, padx=5, pady=5)
btn_contact.grid(row=0, column=4, padx=5, pady=5)

lbl_selectFolder.grid(row=1, column=0, padx=5, pady=5)
txt_selectFolder.grid(row=1, column=1, columnspan=4, padx=5, pady=5)

prg_progressbar.grid(row=2, column=0, columnspan=5, padx=5, pady=5)

window.mainloop()
