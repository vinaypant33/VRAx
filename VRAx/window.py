import ctypes
import sys
from ctypes import wintypes
import win32gui
import win32con

class Window:
    def __init__(self, title="Vrax Window", width=800, height=600):
        self.title = title
        self.width = width
        self.height = height
        self.hwnd = None

    def create_window(self):
        wc = win32gui.WNDCLASS()
        wc.lpfnWndProc = self.window_proc
        wc.lpszClassName = "VraxWindowClass"
        wc.hInstance = win32gui.GetModuleHandle(None)
        wc.hbrBackground = win32con.COLOR_WINDOW

        class_atom = win32gui.RegisterClass(wc)

        self.hwnd = win32gui.CreateWindow(
            class_atom,
            self.title,
            win32con.WS_OVERLAPPEDWINDOW,
            win32con.CW_USEDEFAULT,
            win32con.CW_USEDEFAULT,
            self.width,
            self.height,
            0, 0, wc.hInstance, None
        )

        win32gui.ShowWindow(self.hwnd, win32con.SW_SHOW)
        self.run_message_loop()

    def window_proc(self, hwnd, msg, wparam, lparam):
        if msg == win32con.WM_DESTROY:
            win32gui.PostQuitMessage(0)
            return 0
        return win32gui.DefWindowProc(hwnd, msg, wparam, lparam)

    def run_message_loop(self):
        msg = wintypes.MSG()
        while win32gui.GetMessage(msg, 0, 0):
            win32gui.TranslateMessage(msg)
            win32gui.DispatchMessage(msg)

# Example Usage
if __name__ == "__main__":
    app = Window("Vrax UI Window", 800, 600)
    app.create_window()
