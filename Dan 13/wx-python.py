
# try:
import wx
app = wx.App()
frame = wx.Frame(None, title='Hello wxPython')
frame.Show()
app.MainLoop()

print("WX is available")
# except ImportError:
#     print("WX is NOT available")
    
print("Done")
