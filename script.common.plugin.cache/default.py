'''
    Cache service for XBMC
    Copyright (C) 2010-2011 Tobias Ussing And Henrik Mosgaard Jensen

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    Version 0.8
'''
import sys
import xbmc
import xbmcaddon
try:
    import xbmcvfs
except:
    import xbmcvfsdummy as xbmcvfs

settings = xbmcaddon.Addon(id='script.common.plugin.cache')
language = settings.getLocalizedString
dbg = settings.getSetting("debug") == "true"
dbglevel = 3


def run():
    s = StorageServer.StorageServer(False)
    print " StorageServer Module loaded RUN"
    print s.plugin + " Starting server"
    s.run()
    return True

if __name__ == "__main__":
    if not xbmc.getCondVisibility('system.platform.ios') and settings.getSetting("autostart") == "true":
        sys.path = [settings.getAddonInfo('path') + "/lib"] + sys.path
        import StorageServer
        run()
