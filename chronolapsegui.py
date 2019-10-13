#!/usr/bin/env python
# -*- coding: ISO-8859-15 -*-
#
# generated by wxGlade 0.6.8 (standalone edition) on Sun Oct 02 12:29:06 2016
#

import wx

# begin wxGlade: dependencies
import gettext
from gettext import gettext as _
# end wxGlade

# begin wxGlade: extracode
class ProgressPanel(wx.Panel):

    def __init__(self, *args, **kwds):
        wx.Panel.__init__(self, *args, **kwds)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.progress = 0

    def setProgress(self, progress):
        self.progress = progress

        dc = wx.WindowDC(self)
        dc.SetPen(wx.Pen(wx.Colour(0,0,255,255)))
        dc.SetBrush(wx.Brush(wx.Colour(0,0,255,220)))

        # build rect
        width,height = self.GetSize()
        size = max(2, (width-10)*self.progress)
        rect = wx.Rect(5,8, size ,5)

        # draw rect
        dc.Clear()
        dc.DrawRoundedRectangle(rect, 2)

    def OnPaint(self, evt):
        # this doesnt appear to work at all...

        width,height = self.GetSize()

        # get drawing shit
        dc = wx.PaintDC(self)

        dc.SetPen(wx.Pen(wx.Colour(0,0,255,255)))
        dc.SetBrush(wx.Brush(wx.Colour(0,0,255,220)))

        # build rect
        size = max(2, (width-10)*self.progress)
        rect = wx.Rect(5,8, size ,5)

        # draw rect
        dc.Clear()
        #dc.BeginDrawing()
        dc.DrawRoundedRectangle(rect, 2)
        #dc.EndDrawing()
# end wxGlade


class chronoFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: chronoFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        
        # Menu Bar
        self.chronoframe_menubar = wx.MenuBar()
        self.file = wx.Menu()
        self.exitmenuitem = wx.MenuItem(self.file, wx.ID_EXIT, _("Exit Chronolapse"), "", wx.ITEM_NORMAL)
        self.file.Append(self.exitmenuitem)
        self.chronoframe_menubar.Append(self.file, _("File"))
        self.aboutmenu = wx.Menu()
        self.aboutmenuitem = wx.MenuItem(self.aboutmenu, wx.ID_ANY, _("About"), _("About Chronolapse"), wx.ITEM_NORMAL)
        self.aboutmenu.Append(self.aboutmenuitem)
        self.chronoframe_menubar.Append(self.aboutmenu, _("About"))
        self.SetMenuBar(self.chronoframe_menubar)
        # Menu Bar end
        self.notebook_1 = wx.Notebook(self, wx.ID_ANY, style=0)
        self.notebook_1_capturepane = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.label_3 = wx.StaticText(self.notebook_1_capturepane, wx.ID_ANY, _("Capture:"))
        self.screenshotcheck = wx.CheckBox(self.notebook_1_capturepane, wx.ID_ANY, _("Screenshots"))
        self.screenshotconfigurebutton = wx.Button(self.notebook_1_capturepane, wx.ID_ANY, _("Configure"))
        self.webcamcheck = wx.CheckBox(self.notebook_1_capturepane, wx.ID_ANY, _("Camera"))
        self.configurewebcambutton = wx.Button(self.notebook_1_capturepane, wx.ID_ANY, _("Configure"))
        self.filename_format_timestamp = wx.RadioButton(self.notebook_1_capturepane, wx.ID_ANY, _("Timestamp Filenames"), style=wx.RB_GROUP)
        self.filename_format_sequential = wx.RadioButton(self.notebook_1_capturepane, wx.ID_ANY, _("Sequential Filenames"))
        self.label_2 = wx.StaticText(self.notebook_1_capturepane, wx.ID_ANY, _("Seconds Between Captures:"))
        self.frequencytext = wx.TextCtrl(self.notebook_1_capturepane, wx.ID_ANY, _("60"))
        self.ignoreidlecheck = wx.CheckBox(self.notebook_1_capturepane, wx.ID_ANY, _("Skip Capture if Idle"))
        self.startbutton = wx.Button(self.notebook_1_capturepane, wx.ID_ANY, _("Start Capture"))
        self.forcecapturebutton = wx.Button(self.notebook_1_capturepane, wx.ID_ANY, _("Force Capture"))
        self.progresspanel = ProgressPanel(self.notebook_1_capturepane, wx.ID_ANY)
        self.notebook_1_pippane = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.label_1 = wx.StaticText(self.notebook_1_pippane, wx.ID_ANY, _("Picture in Picture:"))
        self.label_4 = wx.StaticText(self.notebook_1_pippane, wx.ID_ANY, _("Main Image Folder:"))
        self.pipmainimagefoldertext = wx.TextCtrl(self.notebook_1_pippane, wx.ID_ANY, "")
        self.pipmainimagefolderbrowse = wx.Button(self.notebook_1_pippane, wx.ID_ANY, _("..."))
        self.label_12 = wx.StaticText(self.notebook_1_pippane, wx.ID_ANY, _("PIP Image Folder:"))
        self.pippipimagefoldertext = wx.TextCtrl(self.notebook_1_pippane, wx.ID_ANY, "")
        self.pippipimagefolderbrowse = wx.Button(self.notebook_1_pippane, wx.ID_ANY, _("..."))
        self.label_13 = wx.StaticText(self.notebook_1_pippane, wx.ID_ANY, _("Output Folder:"))
        self.pipoutputimagefoldertext = wx.TextCtrl(self.notebook_1_pippane, wx.ID_ANY, "")
        self.pipoutputimagefolderbrowse = wx.Button(self.notebook_1_pippane, wx.ID_ANY, _("..."))
        self.label_14 = wx.StaticText(self.notebook_1_pippane, wx.ID_ANY, _("PIP Size:"))
        self.pipsizecombo = wx.ComboBox(self.notebook_1_pippane, wx.ID_ANY, choices=[_("Small"), _("Medium"), _("Large")], style=wx.CB_DROPDOWN)
        self.label_15 = wx.StaticText(self.notebook_1_pippane, wx.ID_ANY, _("PIP Position:"))
        self.pippositioncombo = wx.ComboBox(self.notebook_1_pippane, wx.ID_ANY, choices=[_("Top"), _("Top-Right"), _("Right"), _("Bottom-Right"), _("Bottom"), _("Bottom-Left"), _("Left"), _("Top-Left")], style=wx.CB_DROPDOWN)
        self.pipignoreunmatchedcheck = wx.CheckBox(self.notebook_1_pippane, wx.ID_ANY, _("Ignore un-matched images"))
        self.pipcreatebutton = wx.Button(self.notebook_1_pippane, wx.ID_ANY, _("Create PIP"))
        self.notebook_1_videopane = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.VideoLabel = wx.StaticText(self.notebook_1_videopane, wx.ID_ANY, _("Video:"))
        self.label_22 = wx.StaticText(self.notebook_1_videopane, wx.ID_ANY, _("Source Images:"))
        self.videosourcetext = wx.TextCtrl(self.notebook_1_videopane, wx.ID_ANY, "")
        self.videosourcebrowse = wx.Button(self.notebook_1_videopane, wx.ID_ANY, _("..."))
        self.label_23 = wx.StaticText(self.notebook_1_videopane, wx.ID_ANY, _("Destination Folder:"))
        self.videodestinationtext = wx.TextCtrl(self.notebook_1_videopane, wx.ID_ANY, "")
        self.videodestinationbrowse = wx.Button(self.notebook_1_videopane, wx.ID_ANY, _("..."))
        self.label_26 = wx.StaticText(self.notebook_1_videopane, wx.ID_ANY, _("MEncoder Path:"))
        self.mencoderpathtext = wx.TextCtrl(self.notebook_1_videopane, wx.ID_ANY, "")
        self.mencoderpathbrowse = wx.Button(self.notebook_1_videopane, wx.ID_ANY, _("..."))
        self.label_25 = wx.StaticText(self.notebook_1_videopane, wx.ID_ANY, _("Video Codec:"))
        self.videocodeccombo = wx.ComboBox(self.notebook_1_videopane, wx.ID_ANY, choices=[_("mpeg4"), _("mpeg2video"), _("wmv1"), _("wmv2")], style=wx.CB_DROPDOWN)
        self.randomname = wx.StaticText(self.notebook_1_videopane, wx.ID_ANY, _("Frame Rate:"))
        self.videoframeratetext = wx.TextCtrl(self.notebook_1_videopane, wx.ID_ANY, _("25"))
        self.movielengthlabel = wx.StaticText(self.notebook_1_videopane, wx.ID_ANY, _("Estimated Movie Length: 0 m 0 s"))
        self.videocreatebutton = wx.Button(self.notebook_1_videopane, wx.ID_ANY, _("Encode Video"))
        self.static_line_1 = wx.StaticLine(self.notebook_1_videopane, wx.ID_ANY)
        self.AudioLabel = wx.StaticText(self.notebook_1_videopane, wx.ID_ANY, _("Audio:"))
        self.label_22_copy = wx.StaticText(self.notebook_1_videopane, wx.ID_ANY, _("Video Source:"))
        self.audiosourcevideotext = wx.TextCtrl(self.notebook_1_videopane, wx.ID_ANY, "")
        self.audiosourcevideobrowse = wx.Button(self.notebook_1_videopane, wx.ID_ANY, _("..."))
        self.label_23_copy = wx.StaticText(self.notebook_1_videopane, wx.ID_ANY, _("Audio Source:"))
        self.audiosourcetext = wx.TextCtrl(self.notebook_1_videopane, wx.ID_ANY, "")
        self.audiosourcebrowse = wx.Button(self.notebook_1_videopane, wx.ID_ANY, _("..."))
        self.label_26_copy = wx.StaticText(self.notebook_1_videopane, wx.ID_ANY, _("Output Folder:"))
        self.audiooutputfoldertext = wx.TextCtrl(self.notebook_1_videopane, wx.ID_ANY, "")
        self.audiooutputfolderbrowse = wx.Button(self.notebook_1_videopane, wx.ID_ANY, _("..."))
        self.createaudiobutton = wx.Button(self.notebook_1_videopane, wx.ID_ANY, _("Add Audio"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.exitMenuClicked, self.exitmenuitem)
        self.Bind(wx.EVT_MENU, self.aboutMenuClicked, self.aboutmenuitem)
        self.Bind(wx.EVT_BUTTON, self.screenshotConfigurePressed, self.screenshotconfigurebutton)
        self.Bind(wx.EVT_BUTTON, self.webcamConfigurePressed, self.configurewebcambutton)
        self.Bind(wx.EVT_BUTTON, self.startCapturePressed, self.startbutton)
        self.Bind(wx.EVT_BUTTON, self.forceCapturePressed, self.forcecapturebutton)
        self.Bind(wx.EVT_BUTTON, self.pipMainImageBrowsePressed, self.pipmainimagefolderbrowse)
        self.Bind(wx.EVT_BUTTON, self.pipPipImageBrowsePressed, self.pippipimagefolderbrowse)
        self.Bind(wx.EVT_BUTTON, self.pipOutputBrowsePressed, self.pipoutputimagefolderbrowse)
        self.Bind(wx.EVT_BUTTON, self.createPipPressed, self.pipcreatebutton)
        self.Bind(wx.EVT_BUTTON, self.videoSourceBrowsePressed, self.videosourcebrowse)
        self.Bind(wx.EVT_BUTTON, self.videoDestinationBrowsePressed, self.videodestinationbrowse)
        self.Bind(wx.EVT_BUTTON, self.mencoderPathBrowsePressed, self.mencoderpathbrowse)
        self.Bind(wx.EVT_TEXT, self.framerateTextChanged, self.videoframeratetext)
        self.Bind(wx.EVT_BUTTON, self.createVideoPressed, self.videocreatebutton)
        self.Bind(wx.EVT_BUTTON, self.audioSourceVideoBrowsePressed, self.audiosourcevideobrowse)
        self.Bind(wx.EVT_BUTTON, self.audioSourceBrowsePressed, self.audiosourcebrowse)
        self.Bind(wx.EVT_BUTTON, self.audioOutputFolderBrowsePressed, self.audiooutputfolderbrowse)
        self.Bind(wx.EVT_BUTTON, self.createAudioPressed, self.createaudiobutton)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: chronoFrame.__set_properties
        self.SetTitle(_("ChronoLapse by Keeyai"))
        self.SetSize((511, 438))
        self.label_3.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.screenshotcheck.SetToolTip(_("Check this to capture screenshots"))
        self.screenshotcheck.SetValue(1)
        self.screenshotconfigurebutton.SetToolTip(_("Click to configure screenshot captures"))
        self.webcamcheck.SetToolTip(_("Check to enable webcam captures"))
        self.webcamcheck.SetValue(1)
        self.configurewebcambutton.SetToolTip(_("Click to configure camera captures"))
        self.filename_format_timestamp.SetToolTip(_("Saves screenshots and camera captures with the timestamp in the filename."))
        self.filename_format_timestamp.SetValue(1)
        self.filename_format_sequential.SetToolTip(_("Saves screenshots and camera captures as sequential numbers. Required by some external encoding libraries."))
        self.frequencytext.SetToolTip(_("The number of seconds in between captures. Set to 0 for no automatic capturing."))
        self.ignoreidlecheck.SetToolTip(_("Check this to skip capturing if no recent activity detected"))
        self.startbutton.SetToolTip(_("Click to start/stop capturing"))
        self.forcecapturebutton.SetToolTip(_("Click to force CL to capture right now. Use for important frames or for creating stop motions."))
        self.label_1.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.pipmainimagefoldertext.SetMinSize((200, -1))
        self.pipmainimagefolderbrowse.SetMinSize((25, -1))
        self.pipmainimagefolderbrowse.SetToolTip(_("Click to Browse"))
        self.pippipimagefoldertext.SetMinSize((200, -1))
        self.pippipimagefolderbrowse.SetMinSize((25, -1))
        self.pippipimagefolderbrowse.SetToolTip(_("Click to Browse"))
        self.pipoutputimagefoldertext.SetMinSize((25, -1))
        self.pipoutputimagefolderbrowse.SetMinSize((25, -1))
        self.pipoutputimagefolderbrowse.SetToolTip(_("Click to Browse"))
        self.pipsizecombo.SetToolTip(_("Select the size of the smaller image"))
        self.pipsizecombo.SetSelection(0)
        self.pippositioncombo.SetToolTip(_("Select the position of the smaller image"))
        self.pippositioncombo.SetSelection(1)
        self.pipignoreunmatchedcheck.SetToolTip(_("Check to ignore image names that are in one folder but not the other"))
        self.pipignoreunmatchedcheck.Hide()
        self.pipignoreunmatchedcheck.SetValue(1)
        self.pipcreatebutton.SetToolTip(_("Create PIP"))
        self.VideoLabel.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.videosourcetext.SetMinSize((200, -1))
        self.videosourcebrowse.SetMinSize((25, -1))
        self.videosourcebrowse.SetToolTip(_("Click to Browse"))
        self.videodestinationtext.SetMinSize((200, -1))
        self.videodestinationbrowse.SetMinSize((25, -1))
        self.videodestinationbrowse.SetToolTip(_("Click to Browse"))
        self.mencoderpathtext.SetMinSize((200, -1))
        self.mencoderpathtext.SetToolTip(_("Set this to the MEncoder executable"))
        self.mencoderpathbrowse.SetMinSize((25, -1))
        self.mencoderpathbrowse.SetToolTip(_("Click to Browse"))
        self.videocodeccombo.SetToolTip(_("Select which codec to use when encoding your video"))
        self.videocodeccombo.SetSelection(0)
        self.videoframeratetext.SetMinSize((25, -1))
        self.videoframeratetext.SetToolTip(_("Set how many images per second you want to show in your movie"))
        self.videocreatebutton.SetToolTip(_("Create the Video"))
        self.AudioLabel.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.audiosourcevideotext.SetMinSize((200, -1))
        self.audiosourcevideobrowse.SetMinSize((25, -1))
        self.audiosourcevideobrowse.SetToolTip(_("Click to Browse"))
        self.audiosourcetext.SetMinSize((200, -1))
        self.audiosourcebrowse.SetMinSize((25, -1))
        self.audiosourcebrowse.SetToolTip(_("Click to Browse"))
        self.audiooutputfoldertext.SetMinSize((200, -1))
        self.audiooutputfoldertext.SetToolTip(_("Set this to the folder where you want the finished video"))
        self.audiooutputfolderbrowse.SetMinSize((25, -1))
        self.audiooutputfolderbrowse.SetToolTip(_("Click to Browse"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: chronoFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_18 = wx.FlexGridSizer(10, 1, 0, 0)
        grid_sizer_18_copy_copy = wx.FlexGridSizer(5, 2, 0, 0)
        grid_sizer_34 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_35 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_31 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_23 = wx.FlexGridSizer(1, 3, 0, 5)
        grid_sizer_4 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_3 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_18_copy = wx.FlexGridSizer(3, 2, 0, 0)
        grid_sizer_30 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_28 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_27 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_5 = wx.FlexGridSizer(5, 1, 0, 0)
        grid_sizer_13 = wx.FlexGridSizer(3, 2, 0, 0)
        grid_sizer_17 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_14 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_12 = wx.FlexGridSizer(5, 2, 0, 0)
        grid_sizer_25 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_22 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_21 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_1 = wx.FlexGridSizer(4, 1, 0, 0)
        grid_sizer_26 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_15 = wx.FlexGridSizer(4, 2, 0, 0)
        grid_sizer_20 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_16 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_1.Add(self.label_3, 0, 0, 0)
        grid_sizer_16.Add(self.screenshotcheck, 0, 0, 0)
        grid_sizer_16.Add(self.screenshotconfigurebutton, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_16.AddGrowableCol(0)
        grid_sizer_16.AddGrowableCol(1)
        grid_sizer_15.Add(grid_sizer_16, 1, wx.EXPAND, 0)
        grid_sizer_20.Add(self.webcamcheck, 0, 0, 0)
        grid_sizer_20.Add(self.configurewebcambutton, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_20.AddGrowableCol(0)
        grid_sizer_20.AddGrowableCol(1)
        grid_sizer_15.Add(grid_sizer_20, 1, wx.EXPAND, 0)
        grid_sizer_15.Add(self.filename_format_timestamp, 0, 0, 0)
        grid_sizer_15.Add(self.filename_format_sequential, 0, 0, 0)
        grid_sizer_15.Add(self.label_2, 0, 0, 0)
        grid_sizer_15.Add(self.frequencytext, 0, 0, 0)
        grid_sizer_15.Add(self.ignoreidlecheck, 0, 0, 0)
        grid_sizer_15.Add((20, 20), 0, 0, 0)
        grid_sizer_15.AddGrowableCol(0)
        grid_sizer_15.AddGrowableCol(1)
        grid_sizer_1.Add(grid_sizer_15, 1, wx.EXPAND, 0)
        grid_sizer_26.Add(self.startbutton, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_26.Add(self.forcecapturebutton, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_26.AddGrowableCol(0)
        grid_sizer_26.AddGrowableCol(1)
        grid_sizer_1.Add(grid_sizer_26, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(self.progresspanel, 1, wx.EXPAND, 0)
        self.notebook_1_capturepane.SetSizer(grid_sizer_1)
        grid_sizer_1.AddGrowableRow(2)
        grid_sizer_1.AddGrowableCol(0)
        grid_sizer_5.Add(self.label_1, 0, 0, 0)
        grid_sizer_12.Add(self.label_4, 0, 0, 0)
        grid_sizer_21.Add(self.pipmainimagefoldertext, 0, wx.EXPAND, 0)
        grid_sizer_21.Add(self.pipmainimagefolderbrowse, 0, 0, 0)
        grid_sizer_21.AddGrowableCol(0)
        grid_sizer_12.Add(grid_sizer_21, 1, wx.EXPAND, 0)
        grid_sizer_12.Add(self.label_12, 0, 0, 0)
        grid_sizer_22.Add(self.pippipimagefoldertext, 0, wx.EXPAND, 0)
        grid_sizer_22.Add(self.pippipimagefolderbrowse, 0, 0, 0)
        grid_sizer_22.AddGrowableCol(0)
        grid_sizer_12.Add(grid_sizer_22, 1, wx.EXPAND, 0)
        grid_sizer_12.Add(self.label_13, 0, 0, 0)
        grid_sizer_25.Add(self.pipoutputimagefoldertext, 0, wx.EXPAND, 0)
        grid_sizer_25.Add(self.pipoutputimagefolderbrowse, 0, 0, 0)
        grid_sizer_25.AddGrowableCol(0)
        grid_sizer_12.Add(grid_sizer_25, 1, wx.EXPAND, 0)
        grid_sizer_12.AddGrowableCol(0)
        grid_sizer_12.AddGrowableCol(1)
        grid_sizer_5.Add(grid_sizer_12, 1, wx.EXPAND, 0)
        grid_sizer_14.Add(self.label_14, 0, 0, 0)
        grid_sizer_14.Add(self.pipsizecombo, 0, 0, 0)
        grid_sizer_14.AddGrowableCol(0)
        grid_sizer_14.AddGrowableCol(1)
        grid_sizer_13.Add(grid_sizer_14, 1, wx.EXPAND, 0)
        grid_sizer_17.Add(self.label_15, 0, 0, 0)
        grid_sizer_17.Add(self.pippositioncombo, 0, 0, 0)
        grid_sizer_17.AddGrowableCol(0)
        grid_sizer_17.AddGrowableCol(1)
        grid_sizer_13.Add(grid_sizer_17, 1, wx.EXPAND, 0)
        grid_sizer_13.AddGrowableCol(0)
        grid_sizer_13.AddGrowableCol(1)
        grid_sizer_5.Add(grid_sizer_13, 1, wx.EXPAND, 0)
        grid_sizer_5.Add(self.pipignoreunmatchedcheck, 0, 0, 0)
        grid_sizer_5.Add(self.pipcreatebutton, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.notebook_1_pippane.SetSizer(grid_sizer_5)
        grid_sizer_5.AddGrowableRow(4)
        grid_sizer_5.AddGrowableCol(0)
        grid_sizer_18.Add(self.VideoLabel, 0, 0, 0)
        grid_sizer_18_copy.Add(self.label_22, 0, 0, 0)
        grid_sizer_27.Add(self.videosourcetext, 0, wx.EXPAND, 0)
        grid_sizer_27.Add(self.videosourcebrowse, 0, 0, 0)
        grid_sizer_27.AddGrowableCol(0)
        grid_sizer_18_copy.Add(grid_sizer_27, 1, wx.EXPAND, 0)
        grid_sizer_18_copy.Add(self.label_23, 0, 0, 0)
        grid_sizer_28.Add(self.videodestinationtext, 0, wx.EXPAND, 0)
        grid_sizer_28.Add(self.videodestinationbrowse, 0, 0, 0)
        grid_sizer_28.AddGrowableCol(0)
        grid_sizer_18_copy.Add(grid_sizer_28, 1, wx.EXPAND, 0)
        grid_sizer_18_copy.Add(self.label_26, 0, 0, 0)
        grid_sizer_30.Add(self.mencoderpathtext, 0, wx.EXPAND, 0)
        grid_sizer_30.Add(self.mencoderpathbrowse, 0, 0, 0)
        grid_sizer_30.AddGrowableCol(0)
        grid_sizer_18_copy.Add(grid_sizer_30, 1, wx.EXPAND, 0)
        grid_sizer_18_copy.AddGrowableRow(2)
        grid_sizer_18_copy.AddGrowableCol(1)
        grid_sizer_18.Add(grid_sizer_18_copy, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.label_25, 0, 0, 0)
        grid_sizer_3.Add(self.videocodeccombo, 0, 0, 0)
        grid_sizer_3.AddGrowableCol(1)
        grid_sizer_23.Add(grid_sizer_3, 1, wx.EXPAND, 0)
        grid_sizer_4.Add(self.randomname, 0, 0, 0)
        grid_sizer_4.Add(self.videoframeratetext, 0, 0, 0)
        grid_sizer_4.AddGrowableCol(1)
        grid_sizer_23.Add(grid_sizer_4, 1, wx.EXPAND, 0)
        grid_sizer_23.Add(self.movielengthlabel, 0, 0, 0)
        grid_sizer_23.AddGrowableCol(0)
        grid_sizer_23.AddGrowableCol(1)
        grid_sizer_23.AddGrowableCol(2)
        grid_sizer_18.Add(grid_sizer_23, 1, wx.EXPAND, 0)
        grid_sizer_18.Add(self.videocreatebutton, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_18.Add((20, 20), 0, 0, 0)
        grid_sizer_18.Add(self.static_line_1, 0, wx.EXPAND, 0)
        grid_sizer_18.Add(self.AudioLabel, 0, 0, 0)
        grid_sizer_18_copy_copy.Add(self.label_22_copy, 0, 0, 0)
        grid_sizer_31.Add(self.audiosourcevideotext, 0, wx.EXPAND, 0)
        grid_sizer_31.Add(self.audiosourcevideobrowse, 0, 0, 0)
        grid_sizer_31.AddGrowableCol(0)
        grid_sizer_18_copy_copy.Add(grid_sizer_31, 1, wx.EXPAND, 0)
        grid_sizer_18_copy_copy.Add(self.label_23_copy, 0, 0, 0)
        grid_sizer_35.Add(self.audiosourcetext, 0, wx.EXPAND, 0)
        grid_sizer_35.Add(self.audiosourcebrowse, 0, 0, 0)
        grid_sizer_35.AddGrowableCol(0)
        grid_sizer_18_copy_copy.Add(grid_sizer_35, 1, wx.EXPAND, 0)
        grid_sizer_18_copy_copy.Add(self.label_26_copy, 0, 0, 0)
        grid_sizer_34.Add(self.audiooutputfoldertext, 0, wx.EXPAND, 0)
        grid_sizer_34.Add(self.audiooutputfolderbrowse, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_34.AddGrowableCol(0)
        grid_sizer_18_copy_copy.Add(grid_sizer_34, 1, wx.EXPAND, 0)
        grid_sizer_18_copy_copy.AddGrowableRow(3)
        grid_sizer_18_copy_copy.AddGrowableCol(1)
        grid_sizer_18.Add(grid_sizer_18_copy_copy, 1, wx.EXPAND, 0)
        grid_sizer_18.Add(self.createaudiobutton, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.notebook_1_videopane.SetSizer(grid_sizer_18)
        grid_sizer_18.AddGrowableRow(7)
        grid_sizer_18.AddGrowableCol(0)
        self.notebook_1.AddPage(self.notebook_1_capturepane, _("Capture"))
        self.notebook_1.AddPage(self.notebook_1_pippane, _("PIP"))
        self.notebook_1.AddPage(self.notebook_1_videopane, _("Video"))
        sizer_1.Add(self.notebook_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def exitMenuClicked(self, event):  # wxGlade: chronoFrame.<event_handler>
        print("Event handler 'exitMenuClicked' not implemented!")
        event.Skip()

    def aboutMenuClicked(self, event):  # wxGlade: chronoFrame.<event_handler>
        print("Event handler 'aboutMenuClicked' not implemented!")
        event.Skip()

    def screenshotConfigurePressed(self, event):  # wxGlade: chronoFrame.<event_handler>
        print("Event handler 'screenshotConfigurePressed' not implemented!")
        event.Skip()

    def webcamConfigurePressed(self, event):  # wxGlade: chronoFrame.<event_handler>
        print("Event handler 'webcamConfigurePressed' not implemented!")
        event.Skip()

    def startCapturePressed(self, event):  # wxGlade: chronoFrame.<event_handler>
        print("Event handler 'startCapturePressed' not implemented!")
        event.Skip()

    def forceCapturePressed(self, event):  # wxGlade: chronoFrame.<event_handler>
        print("Event handler 'forceCapturePressed' not implemented!")
        event.Skip()

    def pipMainImageBrowsePressed(self, event):  # wxGlade: chronoFrame.<event_handler>
        print("Event handler 'pipMainImageBrowsePressed' not implemented!")
        event.Skip()

    def pipPipImageBrowsePressed(self, event):  # wxGlade: chronoFrame.<event_handler>
        print("Event handler 'pipPipImageBrowsePressed' not implemented!")
        event.Skip()

    def pipOutputBrowsePressed(self, event):  # wxGlade: chronoFrame.<event_handler>
        print("Event handler 'pipOutputBrowsePressed' not implemented!")
        event.Skip()

    def createPipPressed(self, event):  # wxGlade: chronoFrame.<event_handler>
        print("Event handler 'createPipPressed' not implemented!")
        event.Skip()

    def videoSourceBrowsePressed(self, event):  # wxGlade: chronoFrame.<event_handler>
        print("Event handler 'videoSourceBrowsePressed' not implemented!")
        event.Skip()

    def videoDestinationBrowsePressed(self, event):  # wxGlade: chronoFrame.<event_handler>
        print("Event handler 'videoDestinationBrowsePressed' not implemented!")
        event.Skip()

    def mencoderPathBrowsePressed(self, event):  # wxGlade: chronoFrame.<event_handler>
        print("Event handler 'mencoderPathBrowsePressed' not implemented!")
        event.Skip()

    def framerateTextChanged(self, event):  # wxGlade: chronoFrame.<event_handler>
        print("Event handler 'framerateTextChanged' not implemented!")
        event.Skip()

    def createVideoPressed(self, event):  # wxGlade: chronoFrame.<event_handler>
        print("Event handler 'createVideoPressed' not implemented!")
        event.Skip()

    def audioSourceVideoBrowsePressed(self, event):  # wxGlade: chronoFrame.<event_handler>
        print("Event handler 'audioSourceVideoBrowsePressed' not implemented!")
        event.Skip()

    def audioSourceBrowsePressed(self, event):  # wxGlade: chronoFrame.<event_handler>
        print("Event handler 'audioSourceBrowsePressed' not implemented!")
        event.Skip()

    def audioOutputFolderBrowsePressed(self, event):  # wxGlade: chronoFrame.<event_handler>
        print("Event handler 'audioOutputFolderBrowsePressed' not implemented!")
        event.Skip()

    def createAudioPressed(self, event):  # wxGlade: chronoFrame.<event_handler>
        print("Event handler 'createAudioPressed' not implemented!")
        event.Skip()

# end of class chronoFrame

class screenshotConfigDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: screenshotConfigDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.dualmonitorscheck = wx.CheckBox(self, wx.ID_ANY, _("Capture Dual Monitors"))
        self.timestampcheck = wx.CheckBox(self, wx.ID_ANY, _("Show Timestamp"))
        self.label_16 = wx.StaticText(self, wx.ID_ANY, _("Format:"))
        self.screenshot_timestamp_format = wx.TextCtrl(self, wx.ID_ANY, _("%Y-%m-%d %H:%M:%S"))
        self.subsectioncheck = wx.CheckBox(self, wx.ID_ANY, _("Subsection"))
        self.label36 = wx.StaticText(self, wx.ID_ANY, _("Top:"))
        self.subsectiontop = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_36 = wx.StaticText(self, wx.ID_ANY, _("Left:"))
        self.subsectionleft = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_37 = wx.StaticText(self, wx.ID_ANY, _("Width:"))
        self.subsectionwidth = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_38 = wx.StaticText(self, wx.ID_ANY, _("Height:"))
        self.subsectionheight = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_5 = wx.StaticText(self, wx.ID_ANY, _("File Prefix:"))
        self.screenshotprefixtext = wx.TextCtrl(self, wx.ID_ANY, _("screen_"))
        self.label_6 = wx.StaticText(self, wx.ID_ANY, _("Save Folder:"))
        self.screenshotsavefoldertext = wx.TextCtrl(self, wx.ID_ANY, "")
        self.screenshotsavefolderbrowse = wx.Button(self, wx.ID_ANY, _("..."))
        self.label_7 = wx.StaticText(self, wx.ID_ANY, _("File Format:"))
        self.screenshotformatcombo = wx.ComboBox(self, wx.ID_ANY, choices=[_("jpg"), _("png"), _("gif")], style=wx.CB_DROPDOWN | wx.CB_DROPDOWN)
        self.screenshotconfigsave = wx.Button(self, wx.ID_OK, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.screenshotSaveFolderBrowse, self.screenshotsavefolderbrowse)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: screenshotConfigDialog.__set_properties
        self.SetTitle(_("Configure Screenshots"))
        self.dualmonitorscheck.SetToolTip(_("Check to capture images from 2 monitors"))
        self.timestampcheck.SetToolTip(_("Check to have CL write a timestamp on each capture"))
        self.timestampcheck.SetValue(1)
        self.screenshot_timestamp_format.SetMinSize((150, -1))
        self.screenshot_timestamp_format.SetToolTip(_("The timestamp format. Passed directly to python's time.strftime function."))
        self.subsectioncheck.SetToolTip(_("Check to have CL write a timestamp on each capture"))
        self.screenshotprefixtext.SetToolTip(_("The file prefix every screenshot should start with"))
        self.screenshotsavefoldertext.SetMinSize((250, -1))
        self.screenshotsavefolderbrowse.SetMinSize((20, -1))
        self.screenshotsavefolderbrowse.SetToolTip(_("Click to browse directories"))
        self.screenshotformatcombo.SetToolTip(_("Select the file format in which screen captures will be saved"))
        self.screenshotformatcombo.SetSelection(0)
        self.screenshotconfigsave.SetToolTip(_("Save this configuration"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: screenshotConfigDialog.__do_layout
        grid_sizer_2 = wx.FlexGridSizer(6, 1, 10, 0)
        grid_sizer_8 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_7 = wx.FlexGridSizer(3, 3, 0, 0)
        grid_sizer_32 = wx.FlexGridSizer(2, 4, 0, 0)
        grid_sizer_6 = wx.FlexGridSizer(3, 2, 0, 0)
        grid_sizer_29 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_6.Add(self.dualmonitorscheck, 0, 0, 0)
        grid_sizer_6.Add((20, 20), 0, 0, 0)
        grid_sizer_6.Add(self.timestampcheck, 0, 0, 0)
        grid_sizer_29.Add(self.label_16, 0, 0, 0)
        grid_sizer_29.Add(self.screenshot_timestamp_format, 0, 0, 0)
        grid_sizer_29.AddGrowableCol(1)
        grid_sizer_6.Add(grid_sizer_29, 1, wx.EXPAND, 0)
        grid_sizer_6.Add(self.subsectioncheck, 0, 0, 0)
        grid_sizer_6.Add((20, 20), 0, 0, 0)
        grid_sizer_2.Add(grid_sizer_6, 1, wx.EXPAND, 0)
        grid_sizer_32.Add(self.label36, 0, 0, 0)
        grid_sizer_32.Add(self.subsectiontop, 0, 0, 0)
        grid_sizer_32.Add(self.label_36, 0, 0, 0)
        grid_sizer_32.Add(self.subsectionleft, 0, 0, 0)
        grid_sizer_32.Add(self.label_37, 0, 0, 0)
        grid_sizer_32.Add(self.subsectionwidth, 0, 0, 0)
        grid_sizer_32.Add(self.label_38, 0, 0, 0)
        grid_sizer_32.Add(self.subsectionheight, 0, 0, 0)
        grid_sizer_2.Add(grid_sizer_32, 1, wx.EXPAND, 0)
        grid_sizer_7.Add(self.label_5, 0, 0, 0)
        grid_sizer_7.Add(self.screenshotprefixtext, 0, 0, 0)
        grid_sizer_7.Add((20, 20), 0, 0, 0)
        grid_sizer_7.Add(self.label_6, 0, 0, 0)
        grid_sizer_7.Add(self.screenshotsavefoldertext, 0, 0, 0)
        grid_sizer_7.Add(self.screenshotsavefolderbrowse, 0, 0, 0)
        grid_sizer_7.Add(self.label_7, 0, 0, 0)
        grid_sizer_7.Add(self.screenshotformatcombo, 0, 0, 0)
        grid_sizer_7.Add((20, 20), 0, 0, 0)
        grid_sizer_2.Add(grid_sizer_7, 1, wx.EXPAND, 0)
        grid_sizer_8.Add(self.screenshotconfigsave, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_8.AddGrowableCol(0)
        grid_sizer_8.AddGrowableCol(1)
        grid_sizer_2.Add(grid_sizer_8, 1, wx.EXPAND, 0)
        self.SetSizer(grid_sizer_2)
        grid_sizer_2.Fit(self)
        grid_sizer_2.AddGrowableCol(0)
        self.Layout()
        self.Centre()
        # end wxGlade

    def screenshotSaveFolderBrowse(self, event):  # wxGlade: screenshotConfigDialog.<event_handler>
        print("Event handler 'screenshotSaveFolderBrowse' not implemented!")
        event.Skip()

# end of class screenshotConfigDialog

class webcamConfigDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: webcamConfigDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.testwebcambutton = wx.Button(self, wx.ID_ANY, _("Test Webcam"))
        self.webcamtimestampcheck = wx.CheckBox(self, wx.ID_ANY, _("Show Timestamp"))
        self.label_16 = wx.StaticText(self, wx.ID_ANY, _("Format:"))
        self.webcam_timestamp_format = wx.TextCtrl(self, wx.ID_ANY, _("%Y-%m-%d %H:%M:%S"))
        self.label_9 = wx.StaticText(self, wx.ID_ANY, _("File Prefix:"))
        self.webcamprefixtext = wx.TextCtrl(self, wx.ID_ANY, _("cam_"))
        self.label_10 = wx.StaticText(self, wx.ID_ANY, _("Save Folder:"))
        self.webcamsavefoldertext = wx.TextCtrl(self, wx.ID_ANY, "")
        self.webcamsavefolderbrowse = wx.Button(self, wx.ID_ANY, _("..."))
        self.label_11 = wx.StaticText(self, wx.ID_ANY, _("File Format:"))
        self.webcamformatcombo = wx.ComboBox(self, wx.ID_ANY, choices=[_("jpg"), _("png"), _("gif")], style=wx.CB_DROPDOWN | wx.CB_DROPDOWN)
        self.webcamsavebutton = wx.Button(self, wx.ID_OK, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.testWebcamPressed, self.testwebcambutton)
        self.Bind(wx.EVT_BUTTON, self.webcamSaveFolderBrowse, self.webcamsavefolderbrowse)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: webcamConfigDialog.__set_properties
        self.SetTitle(_("Configure Webcam"))
        self.testwebcambutton.SetToolTip(_("Click to test your webcam"))
        self.webcamtimestampcheck.SetToolTip(_("Check to write a timestamp on each webcam capture"))
        self.webcam_timestamp_format.SetMinSize((150, -1))
        self.webcam_timestamp_format.SetToolTip(_("The timestamp format. Passed directly to python's time.strftime function."))
        self.webcamsavefoldertext.SetMinSize((250, -1))
        self.webcamsavefolderbrowse.SetMinSize((20, -1))
        self.webcamformatcombo.SetToolTip(_("Select the file format in which webcam captures will be saved"))
        self.webcamformatcombo.SetSelection(0)
        self.webcamsavebutton.SetToolTip(_("Save this configuration"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: webcamConfigDialog.__do_layout
        grid_sizer_9 = wx.FlexGridSizer(4, 1, 10, 0)
        grid_sizer_11 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_10 = wx.FlexGridSizer(4, 3, 0, 0)
        grid_sizer_19 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_29 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_9.Add(self.testwebcambutton, 0, 0, 0)
        grid_sizer_19.Add(self.webcamtimestampcheck, 0, 0, 0)
        grid_sizer_29.Add(self.label_16, 0, 0, 0)
        grid_sizer_29.Add(self.webcam_timestamp_format, 0, 0, 0)
        grid_sizer_29.AddGrowableCol(1)
        grid_sizer_19.Add(grid_sizer_29, 1, wx.EXPAND, 0)
        grid_sizer_19.AddGrowableCol(0)
        grid_sizer_19.AddGrowableCol(1)
        grid_sizer_9.Add(grid_sizer_19, 1, wx.EXPAND, 0)
        grid_sizer_10.Add(self.label_9, 0, 0, 0)
        grid_sizer_10.Add(self.webcamprefixtext, 0, 0, 0)
        grid_sizer_10.Add((20, 20), 0, 0, 0)
        grid_sizer_10.Add(self.label_10, 0, 0, 0)
        grid_sizer_10.Add(self.webcamsavefoldertext, 0, 0, 0)
        grid_sizer_10.Add(self.webcamsavefolderbrowse, 0, 0, 0)
        grid_sizer_10.Add(self.label_11, 0, 0, 0)
        grid_sizer_10.Add(self.webcamformatcombo, 0, 0, 0)
        grid_sizer_10.Add((20, 20), 0, 0, 0)
        grid_sizer_9.Add(grid_sizer_10, 1, wx.EXPAND, 0)
        grid_sizer_11.Add(self.webcamsavebutton, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_11.AddGrowableCol(0)
        grid_sizer_11.AddGrowableCol(1)
        grid_sizer_9.Add(grid_sizer_11, 1, wx.EXPAND, 0)
        self.SetSizer(grid_sizer_9)
        grid_sizer_9.Fit(self)
        grid_sizer_9.AddGrowableCol(0)
        self.Layout()
        self.Centre()
        # end wxGlade

    def testWebcamPressed(self, event):  # wxGlade: webcamConfigDialog.<event_handler>
        print("Event handler 'testWebcamPressed' not implemented!")
        event.Skip()

    def webcamSaveFolderBrowse(self, event):  # wxGlade: webcamConfigDialog.<event_handler>
        print("Event handler 'webcamSaveFolderBrowse' not implemented!")
        event.Skip()

# end of class webcamConfigDialog

class webcamPreviewDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: webcamPreviewDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER# | wx.THICK_FRAME
        wx.Dialog.__init__(self, *args, **kwds)
        self.panel_1 = wx.ScrolledWindow(self, wx.ID_ANY, style=wx.TAB_TRAVERSAL)
        self.previewbitmap = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.NullBitmap)
        self.previewokbutton = wx.Button(self, wx.ID_OK, "")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: webcamPreviewDialog.__set_properties
        self.SetTitle(_("Webcam Preview"))
        self.SetSize((500, 400))
        self.previewbitmap.SetMinSize((-1, -1))
        self.panel_1.SetScrollRate(10, 10)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: webcamPreviewDialog.__do_layout
        grid_sizer_24 = wx.FlexGridSizer(2, 1, 0, 0)
        sizer_3 = wx.FlexGridSizer(1, 1, 0, 0)
        sizer_3.Add(self.previewbitmap, 0, wx.EXPAND, 0)
        self.panel_1.SetSizer(sizer_3)
        sizer_3.AddGrowableRow(0)
        sizer_3.AddGrowableCol(0)
        grid_sizer_24.Add(self.panel_1, 1, wx.EXPAND, 0)
        grid_sizer_24.Add(self.previewokbutton, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.SetSizer(grid_sizer_24)
        grid_sizer_24.AddGrowableRow(0)
        grid_sizer_24.AddGrowableCol(0)
        self.Layout()
        # end wxGlade

# end of class webcamPreviewDialog
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.App(0)
    wx.InitAllImageHandlers()
    chronoframe = chronoFrame(None, wx.ID_ANY, "")
    app.SetTopWindow(chronoframe)
    chronoframe.Show()
    app.MainLoop()
