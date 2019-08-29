import tkinter as tk
import tkinter.filedialog
import adb_utils
from tkinter import W
import mycheckbox


class App:

    def __init__(self, root):
        self.file_paths = []
        self.adb = adb_utils.AdbUtils()
        frame = tk.Frame(root)
        frame.pack()
        self.btn = tk.Button(frame, text="选择要安装的文件夹", fg="blue", command=self.choice_btn_click)
        self.start_btn = tk.Button(frame, text="开始", fg="red", command=self.start)
        self.btn.pack(side=tk.LEFT)
        self.start_btn.pack(side=tk.RIGHT)

        self.logLabel = tk.Label(root)
        self.logLabel.pack(side=tk.BOTTOM)

        self.btn_refresh_devices = tk.Button(frame, text="刷新链接的手机", command=self.refresh_devices_label)
        self.btn_refresh_devices.pack()

        self.checkbox_arr = []
        self.refresh_devices_label()

    def choice_btn_click(self):
        self.file_paths = tkinter.filedialog.askopenfilenames()
        text = ""
        for item in self.file_paths:
            text += item + "\n"
        self.logLabel["text"] = text

    def start(self):
        self.adb.set_pre_install_apk_path(self.file_paths)
        choice_devices = []
        for dev in self.checkbox_arr:
            if dev.isCheck():
                choice_devices.append(dev["text"])
        print(choice_devices)
        self.adb.set_devices(choice_devices)
        self.adb.start()

    def refresh_devices_label(self):
        self.adb.refreshDevices()
        for view in self.checkbox_arr:
            view.pack_forget()
        self.checkbox_arr.clear()
        print(self.checkbox_arr)
        for dev in self.adb.devices:
            ck = mycheckbox.MyCheckBox(text=dev)
            ck.pack(anchor=W)
            self.checkbox_arr.append(ck)


root = tk.Tk()
root.title("自动安装")
app = App(root)
root.mainloop()
