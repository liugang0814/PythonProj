# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid


###########################################################################
## Class BugzillaFrame
###########################################################################

class BugzillaFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Bugzilla_V0.3", pos=wx.DefaultPosition,
                          size=wx.Size(600, 380), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(600, 380), wx.Size(600, 380))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_bug_sel = wx.Button(self, wx.ID_ANY, u"BUG List", wx.DefaultPosition, wx.Size(100, 30), 0)
        bSizer4.Add(self.m_bug_sel, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_btn_gen = wx.Button(self, wx.ID_ANY, u"生成文件", wx.DefaultPosition, wx.Size(100, 30), 0)
        bSizer4.Add(self.m_btn_gen, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.m_result_path = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(250, 30),
                                         wx.TE_READONLY)
        bSizer4.Add(self.m_result_path, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_btn_open = wx.Button(self, wx.ID_ANY, u"打开结果文件", wx.Point(-1, -1), wx.Size(100, 30), 0)
        bSizer4.Add(self.m_btn_open, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        bSizer1.Add(bSizer4, 0, wx.EXPAND, 5)

        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_gd_list = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(200, 300), 0)

        # Grid
        self.m_gd_list.CreateGrid(500, 1)
        self.m_gd_list.EnableEditing(True)
        self.m_gd_list.EnableGridLines(True)
        self.m_gd_list.EnableDragGridSize(False)
        self.m_gd_list.SetMargins(0, 0)

        # Columns
        self.m_gd_list.EnableDragColMove(False)
        self.m_gd_list.EnableDragColSize(True)
        self.m_gd_list.SetColLabelSize(30)
        self.m_gd_list.SetColLabelValue(0, u"Bug_ID")
        self.m_gd_list.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.m_gd_list.EnableDragRowSize(True)
        self.m_gd_list.SetRowLabelSize(80)
        self.m_gd_list.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.m_gd_list.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer5.Add(self.m_gd_list, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_text_info = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(360, 300),
                                       wx.TE_MULTILINE | wx.TE_READONLY)
        bSizer5.Add(self.m_text_info, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer1.Add(bSizer5, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.on_close)
        self.m_bug_sel.Bind(wx.EVT_BUTTON, self.on_list_sel)
        self.m_btn_gen.Bind(wx.EVT_BUTTON, self.on_gen)
        self.m_btn_open.Bind(wx.EVT_BUTTON, self.on_open)
        self.m_gd_list.Bind(wx.grid.EVT_GRID_LABEL_LEFT_DCLICK, self.on_list_fill)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def on_close(self, event):
        event.Skip()

    def on_list_sel(self, event):
        event.Skip()

    def on_gen(self, event):
        event.Skip()

    def on_open(self, event):
        event.Skip()

    def on_list_fill(self, event):
        event.Skip()
