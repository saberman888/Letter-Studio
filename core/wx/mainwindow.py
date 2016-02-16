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
from core.ctools import *
from core.wx.frames import *
class MainWindow(wx.Frame):
	def __init__(self, parent, title):
		super(MainWindow, self).__init__(parent, title=title, size=(900,600))
		panel = wx.Panel(self)
		nb = wx.Notebook(panel)

                #Load MenuBar
		menubar = wx.MenuBar()
		fm = wx.Menu() #Filemenu
		fm.Append(wx.ID_NEW, "&New")
		fm.Append(wx.ID_OPEN, "&Open")
		fm.Append(wx.ID_SAVE, "&Save")
		fm.Append(wx.ID_SAVE, "&Save As..")
		fm.Append(wx.ID_EXIT, "&Quit Letter Studio")
		#fm.AppendSeparator()

		menubar.Append(fm, "&File")
		self.SetMenuBar(menubar)

                #Load Tabs
		cp = ConlangPage(nb)
		dp = DialectPage(nb)
		dip = DictionaryPage(nb)

		nb.AddPage(cp, "Conlang")
		nb.AddPage(dp, "Dialects")
		nb.AddPage(dip, "Dictionary")

		sizer = wx.BoxSizer()
		sizer.Add(nb, 2, wx.EXPAND)
		panel.SetSizer(sizer)
		self.Centre()
		self.Show(True)

