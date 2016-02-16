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
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import ConfigParser
import os

class Plugin:
    def __init__(self, enabled):
        self.enabled = enabled
        self.object = None

    def Boot(self):
        self.object.boot()
    
class Plugins:
    def __init__(self, plugin_dir):
        self.plugin_dir = plugin_dir
        self.plugins = []
        self.loaded = False
        
    def loadplugins(self):
        loaded_plugins = 0
        pldir = directories['plugins']
        lsdir = directories['data']
        config = ConfigParser.RawConfigParser()
        config.read(lsdir+"ls.conf")
        plulist = os.listdir(pldir)
        for pl in plulist:
            if pl.endswith(".py") or pl.endswith(".pyw"):
                if config.get("Plugins", pl):
                    en_p = config.get("Plugins", pl)
   
                else:
                    config.set("Plugins", pl, "enabled")
                    config.set("Plugins",
                    en_p = '0'

                P = Plugin(en_p)
                #
                #TODO Import CODe
                #
                    
        
    def execPlugins(self):
        for x in self.plugins:
            x.Boot()
            
