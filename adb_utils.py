""" 支持多设备的自动adb安装 """
import os


class AdbUtils:

    def __init__(self):
        self.refreshDevices()

    def refreshDevices(self):
        devices_file = os.popen("adb devices")
        devices_str = devices_file.read()
        devices_str = devices_str.replace("\n", " ")
        devices_str = devices_str.replace("\t", " ")
        devices_arr = devices_str.split(" ")
        self.devices = []
        for i in range(len(devices_arr)):
            item = devices_arr[i].strip()
            if item == "List" or item == "of" or item == "devices" or item == "device" or item == "attached" or item == "":
                continue
            self.devices.append(item)

    def set_pre_install_apk_path(self, arr):
        self.pre_path = arr

    def set_devices(self, install_device):
        self.devices = install_device

    def start(self):
        for dev in self.devices:
            for i in self.pre_path:
                print("device:" + dev + "正在安装" + i)
                commend = "adb -s " + dev + " install -r " + i
                print("commend:" + commend)
                os.system(commend)
