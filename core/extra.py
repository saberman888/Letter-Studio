import wx

def wxprompt(parent=None, message='', default_value=''):
    dialog = wx.TextEntryDialog(parent, message, defaultValue=default_value)
    dialog.ShowModal()
    result = dialog.GetValue()
    return result
