# platform_utils.py
# jia change this because we moved platform-specific code (like pythoncom and win32gui) into this separate file to prevent importing Windows libraries on Linux.
import platform
import os
import tkinter as tk

IS_WINDOWS = platform.system() == "Windows"
IS_LINUX = platform.system() == "Linux"

# ---------------- SCREEN SIZE ----------------
def get_screen_size():
    if IS_WINDOWS:
        from win32api import GetSystemMetrics
        return GetSystemMetrics(0), GetSystemMetrics(1)
    else:
        root = tk.Tk()
        root.withdraw()
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        # jia change this because a hidden Tk root window conflicts with main application PhotoImage instances, so we destroy it.
        root.destroy()
        return w, h


# ---------------- SCANNER ----------------
def scan_image():
    if IS_WINDOWS:
        import pythoncom
        from win32com.client import Dispatch

        pythoncom.CoInitialize()
        wia = Dispatch("WIA.CommonDialog")
        dev = wia.ShowSelectDevice()
        return dev

    elif IS_LINUX:
        import sane
        from PIL import Image

        sane.init()
        devices = sane.get_devices()
        if not devices:
            raise RuntimeError("No scanner found")

        dev = sane.open(devices[0][0])
        dev.start()
        img = dev.snap()  # PIL.Image object
        sane.exit()
        return img

def scan_image_to_file(filepath):
    """
    Scans an image from the default/selected scanner and saves it to filepath.
    """
    if IS_WINDOWS:
        import pythoncom
        from win32com.client import Dispatch

        pythoncom.CoInitialize()
        wia_dev_manager = Dispatch("WIA.DeviceManager")
        wia = Dispatch("WIA.CommonDialog")
        dev = wia.ShowSelectDevice()
        if not dev:
            return False

        scanner = dev.Items[1]
        
        # Set resolution
        try:
            scanner.Properties("Vertical Resolution").Value   = 300
            scanner.Properties("Horizontal Resolution").Value = 300
        except:
            pass
            
        WIA_IMG_FORMAT_PNG = "{B96B3CAF-0728-11D3-9D7B-0000F81EF32E}"
        image = scanner.Transfer(WIA_IMG_FORMAT_PNG)
        image.SaveFile(filepath)
        return True

    elif IS_LINUX:
        import sane
        from PIL import Image

        sane.init()
        devices = sane.get_devices()
        if not devices:
            sane.exit()
            raise RuntimeError("No scanner found")

        dev = sane.open(devices[0][0])
        try:
            # Try to set resolution if supported
            dev.resolution = 300
        except:
            pass
            
        dev.start()
        img = dev.snap()
        img.save(filepath)
        sane.exit()
        return True


# ---------------- SCREENSHOT ----------------
def take_screenshot(path):
    if IS_WINDOWS:
        from PIL import ImageGrab
        img = ImageGrab.grab()
    else:
        import pyautogui
        img = pyautogui.screenshot()

    img.save(path)


# ---------------- TKINTER ICON ----------------
def set_tkinter_icon(window, icon_path):
    from PIL import Image, ImageTk
    try:
        if IS_WINDOWS:
            window.iconbitmap(default=icon_path)
        else:
            im = Image.open(icon_path)
            photo = ImageTk.PhotoImage(im)
            window.iconphoto(True, photo)
            window._icon_photo = photo  # keep reference
    except Exception:
        pass