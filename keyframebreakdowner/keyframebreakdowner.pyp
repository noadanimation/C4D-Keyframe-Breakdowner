"""
#Copyright (c) 2020-2021, Noad Animation Limited
#All rights reserved.
#
#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are met:
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of Noad Animation Limited nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#DISCLAIMED. IN NO EVENT SHALL CURIOUS ANIMAL LIMITED BE LIABLE FOR ANY
#DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import c4d
import os

# Be sure to use a unique ID obtained from www.plugincafe.com
PLUGIN_ID = 1056197

# Container ids
CVAL = 1000

# About
ABOUT = {"id": 1026, "name": "About"}

class KFBDDlg(c4d.gui.GeDialog):
    customid = 1001
    btn15id = 2001
    btn33id = 2002
    btn50id = 2003
    btn67id = 2004
    btn85id = 2005
    btncustomid = 2006
    ##
    btnadd1 = 3001
    btnadd2 = 3002
    btnsub1 = 3101
    btnsub2 = 3102
    ##
    btnswap = 4001

    def __init__(self):
        self.KFBDData = None
        self.CustomValue = 0.5
        #
            

    def CreateLayout(self):
        """
        This Method is called automatically when Cinema 4D Create the Layout (display) of the Dialog.
        """
        # Defines the title
        self.SetTitle("Keyframe Breakdowner")
        
        startid=0
        customwidth = 60

        self.GroupBegin(startid+0,
            c4d.BFH_SCALEFIT|c4d.BFV_SCALEFIT,
            6, 
            4,
            '',
            c4d.BFV_GRIDGROUP_EQUALCOLS|c4d.BFV_GRIDGROUP_EQUALROWS
            )
        #####row 1
        self.AddStaticText(startid+1,
            c4d.BFH_CENTER,
            name=" ")
        self.AddStaticText(startid+2,
            c4d.BFH_CENTER,
            name=" ")
        self.AddStaticText(startid+3,
            c4d.BFH_CENTER,
            name=" ")
        self.AddStaticText(startid+4,
            c4d.BFH_CENTER,
            name=" ")
        self.AddStaticText(startid+5,
            c4d.BFH_CENTER,
            name=" ")
        #
        self.AddEditNumberArrows(self.customid,
            c4d.BFH_CENTER,
            customwidth,
            )
        #####row 2
        self.AddButton(self.btn15id,
            c4d.BFH_CENTER,
            name="15")
        self.AddButton(self.btn33id,
            c4d.BFH_CENTER,
            name="33")
        self.AddButton(self.btn50id,
            c4d.BFH_CENTER,
            name="50")
        self.AddButton(self.btn67id,
            c4d.BFH_CENTER,
            name="67")
        self.AddButton(self.btn85id,
            c4d.BFH_CENTER,
            name="85")
        #
        self.AddButton(self.btncustomid,
            c4d.BFH_CENTER,
            customwidth,
            name="Go")
        #
        ######row 3
        self.AddStaticText(startid+6,
            c4d.BFH_CENTER,
            name=" ")
        self.AddStaticText(startid+7,
            c4d.BFH_CENTER,
            name=" ")
        self.AddStaticText(startid+8,
            c4d.BFH_CENTER,
            name=" ")
        self.AddStaticText(startid+9,
            c4d.BFH_CENTER,
            name=" ")
        self.AddStaticText(startid+10,
            c4d.BFH_CENTER,
            name=" ")
        self.AddStaticText(startid+11,
            c4d.BFH_CENTER,
            name=" ")
        #######row 4
        self.AddButton(self.btnsub2,
            c4d.BFH_CENTER,
            name="--")
        self.AddButton(self.btnsub1,
            c4d.BFH_CENTER,
            name="-")
        self.AddButton(self.btnadd1,
            c4d.BFH_CENTER,
            name="+")
        self.AddButton(self.btnadd2,
            c4d.BFH_CENTER,
            name="++")
        #
        self.AddStaticText(startid+12,
            c4d.BFH_CENTER,
            name=" ")
        self.AddButton(self.btnswap,
            c4d.BFH_CENTER,
            name="Swap")
        #
        self.GroupEnd()
        
        #
        #
        return True
    
    def InitValues(self):
        """
        Called after CreateLayout being called to define the values in the UI
        :return: 	True if successful, or False to signalize an error.
        :rtype: bool
        """
        # Retrieves saved values from the world container of this plugin
        self.KFBDData = c4d.plugins.GetWorldPluginData(PLUGIN_ID)
        if self.KFBDData:
            self.CustomValue = self.KFBDData[CVAL]
        else:
            self.KFBDData = c4d.BaseContainer()

        self.SetPercent(self.customid, self.CustomValue)

        return True
    
    def Command(self, id, msg):
        """
         This Method is called automatically when the user clicks on a gadget and/or changes its value this function will be called.
         It is also called when a string menu item is selected.
        :param id: The ID of the gadget that triggered the event.
        :param msg: The original message container
        :return: False if there was an error, otherwise True.
        """
        
        val = None
        add = None

        if id == self.btn15id:
            val = 0.15
        elif id == self.btn33id:
            val = 0.33333333
        elif id == self.btn50id:
            val = 0.5
        elif id == self.btn67id:
            val = 0.66666667
        elif id == self.btn85id:
            val = 0.85
        elif id == self.btncustomid:
            val = self.GetFloat(self.customid)
            self.CustomValue = val

        elif id == self.customid:
            self.CustomValue = self.GetFloat(self.customid)

        elif id == self.btnsub2:
            add = -0.04
        elif id == self.btnsub1:
            add = -0.01
        elif id == self.btnadd1:
            add = 0.01
        elif id == self.btnadd2:
            add = 0.04

        elif id == self.btnswap:
            self.ActionSwap()

        # Clicks on About entry of Cineversity RSS
        elif id == ABOUT["id"]:
            self.About()
        
        
        if val!=None:
            self.Action(val)
        elif add!=None:
            self.ActionInplace(add)

        return True
    
    def GetCurveKeys(self, ctime, curve):
        keyexact = curve.FindKey(ctime, c4d.FINDANIM_EXACT)
        
        keyleft = curve.FindKey(ctime-c4d.BaseTime(0.0025), c4d.FINDANIM_LEFT)
        keyright = curve.FindKey(ctime+c4d.BaseTime(0.0025), c4d.FINDANIM_RIGHT)

        if keyleft and keyright:
            if keyexact:
                curve.DelKey(keyexact["idx"], True)
            return {"left":keyleft, "right":keyright}
        return None

    def Interpolate(self, ctime, track, val):
        did = track.GetDescriptionID()
        if (did[did.GetDepth()-1].dtype != c4d.DTYPE_REAL):
            return

        curve = track.GetCurve(c4d.CCURVE_CURVE, False)
        if not curve:
            return
        keys = self.GetCurveKeys(ctime, curve)
        if not keys:
            return

        valleft = keys["left"]["key"].GetValue()
        valright = keys["right"]["key"].GetValue()

        newval = valleft + ((valright-valleft) * val)

        newkey = curve.AddKey(ctime, True)
        if newkey:
            newkey = newkey["key"]
            newkey.SetValue(curve, newval)
            newkey.SetInterpolation(curve, keys["left"]["key"].GetInterpolation())
        
    def Action(self, val):
        doc = c4d.documents.GetActiveDocument()
        ctime = doc.GetTime()
        objects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
        tags = doc.GetActiveTags()
        #
        c4d.StopAllThreads()
        doc.StartUndo()
        for obj in objects:
            tracks = obj.GetCTracks()
            for tr in tracks:
                self.Interpolate(ctime, tr, val)
        for tag in tags:
            tracks = tag.GetCTracks()
            for tr in tracks:
                self.Interpolate(ctime, tr, val)
        doc.EndUndo()
        c4d.EventAdd(c4d.EVENT_FORCEREDRAW|c4d.EVENT_ANIMATE)

    def InterpolateInplace(self, ctime, track, val):
        did = track.GetDescriptionID()
        if (did[did.GetDepth()-1].dtype != c4d.DTYPE_REAL):
            return

        curve = track.GetCurve(c4d.CCURVE_CURVE, False)
        if not curve:
            return
        #keys = self.GetCurveKeys(ctime, curve)
        keycurrent = curve.FindKey(ctime, c4d.FINDANIM_EXACT)
        keyother = None
        if val > 0:
            keyother = curve.FindKey(ctime + c4d.BaseTime(0.0025), c4d.FINDANIM_RIGHT)
        else:
            keyother = curve.FindKey(ctime - c4d.BaseTime(0.0025), c4d.FINDANIM_LEFT)
        if not (keycurrent and keyother):
            return

        valleft = keycurrent["key"].GetValue()
        valright = keyother["key"].GetValue()

        val = abs(val)

        newval = valleft + ((valright-valleft) * val)

        #newkey = curve.AddKey(ctime, True)
        #if newkey:
        newkey = keycurrent["key"]
        newkey.SetValue(curve, newval)
        #newkey.SetInterpolation(curve, keyother["key"].GetInterpolation())

    def ActionInplace(self, val):
        doc = c4d.documents.GetActiveDocument()
        ctime = doc.GetTime()
        objects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
        tags = doc.GetActiveTags()
        #
        c4d.StopAllThreads()
        doc.StartUndo()
        for obj in objects:
            tracks = obj.GetCTracks()
            for tr in tracks:
                doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)
                self.InterpolateInplace(ctime, tr, val)
        for tag in tags:
            tracks = tag.GetCTracks()
            for tr in tracks:
                doc.AddUndo(c4d.UNDOTYPE_CHANGE, tag)
                self.InterpolateInplace(ctime, tr, val)
        doc.EndUndo()
        c4d.EventAdd(c4d.EVENT_FORCEREDRAW|c4d.EVENT_ANIMATE)

    def SwapKeys(self, ctime, track):
        did = track.GetDescriptionID()
        if (did[did.GetDepth()-1].dtype != c4d.DTYPE_REAL):
            return

        curve = track.GetCurve(c4d.CCURVE_CURVE, False)
        if not curve:
            return

        keyleft = curve.FindKey(ctime, c4d.FINDANIM_LEFT)
        keyright = curve.FindKey(ctime + c4d.BaseTime(0.0025), c4d.FINDANIM_RIGHT)

        if not (keyleft and keyright):
            return

        valleft = keyleft["key"].GetValue()
        valright = keyright["key"].GetValue()

        keyleft["key"].SetValue(curve, valright)
        keyright["key"].SetValue(curve, valleft)

    def ActionSwap(self):
        doc = c4d.documents.GetActiveDocument()
        ctime = doc.GetTime()
        objects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
        tags = doc.GetActiveTags()
        #
        c4d.StopAllThreads()
        doc.StartUndo()
        for obj in objects:
            tracks = obj.GetCTracks()
            for tr in tracks:
                doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)
                self.SwapKeys(ctime, tr)
        for tag in tags:
            tracks = tag.GetCTracks()
            for tr in tracks:
                doc.AddUndo(c4d.UNDOTYPE_CHANGE, tag)
                self.SwapKeys(ctime, tr)
        doc.EndUndo()
        c4d.EventAdd(c4d.EVENT_FORCEREDRAW|c4d.EVENT_ANIMATE)

    def About(self):
        """
        Opens the About dialog
        """
        c4d.gui.MessageDialog("Keyframe Breakdowner\nNoad Animation", c4d.GEMB_OK)
        return True
        
    def UpdatePrefs(self):
        """
        Updates the data stored in the world container (used to retrieve settings when Cinema 4D leaves)
        """
        self.KFBDData.SetFloat(CVAL, self.CustomValue)
        c4d.plugins.SetWorldPluginData(PLUGIN_ID, self.KFBDData)


class KFBD(c4d.plugins.CommandData):
    """
    Command Data class that holds the CVRssDialog instance.
    """
    dialog = None
    
    def Execute(self, doc):
        """
        Called when the user Execute the command (CallCommand or a clicks on the Command from the plugin menu)
        :param doc: the current active document
        :type doc: c4d.documents.BaseDocument
        :return: True if the command success
        """
        # Creates the dialog if its not already exists
        if self.dialog is None:
            self.dialog = KFBDDlg()

        # Opens the dialog
        return self.dialog.Open(dlgtype=c4d.DLG_TYPE_ASYNC, pluginid=PLUGIN_ID, defaultw=200, defaulth=32)

    def RestoreLayout(self, sec_ref):
        """
        Used to restore an asynchronous dialog that has been placed in the users layout.
        :param sec_ref: The data that needs to be passed to the dlg (almost no use of it).
        :type sec_ref: PyCObject
        :return: True if the restore success
        """
        # Creates the dialog if its not already exists
        if self.dialog is None:
            self.dialog = KFBDDlg()

        # Restores the layout
        return self.dialog.Restore(pluginid=PLUGIN_ID, secret=sec_ref)


# main
if __name__ == "__main__":
    # Retrieves the icon path
    directory, _ = os.path.split(__file__)
    fn = os.path.join(directory, "res", "icon.tif")

    # Creates a BaseBitmap
    bmp = c4d.bitmaps.BaseBitmap()
    if bmp is None:
        raise MemoryError("Failed to create a BaseBitmap.")

    # Init the BaseBitmap with the icon
    if bmp.InitWith(fn)[0] != c4d.IMAGERESULT_OK:
        raise MemoryError("Failed to initialize the BaseBitmap.")

    # Registers the plugin
    c4d.plugins.RegisterCommandPlugin(id=PLUGIN_ID,
                                      str="Keyframe Breakdowner",
                                      info=0,
                                      help="Displays a chosen RSS feed",
                                      dat=KFBD(),
                                      icon=bmp)

    print("Keyframe Breakdowner, (c)2020 Noad Animation Limited")
