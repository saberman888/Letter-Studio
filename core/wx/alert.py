# The MIT License (MIT)
#
# Copyright (c) 2015 saberman888

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import wx


def Show(MSG, title):
	#tkMessageBox.Show(MSG, title)
	m = wx.MessageDialog(None, MSG, title, wx.OK | wx.ICON_INFORMATION)
	m.ShowModal()

def Panic(MSG):
	#tkMessageBox.error(MSG, "Error!")
	m = wx.MessageDialog(None, MSG, "Error!", wx.OK | wx.ICON_ERROR)
	m.ShowModal()


def Ask(MSG, title):
	#tkMessageBox.askquestion(title, MSG)
	pass


def Warn(title, MSG):
	n = wx.MessageDialog(None, MSG, title, wx.OK | wx.ICON_EXCLAMATION)
	n.ShowModal()
