import mobase 
from ..shared.shared_plugin import SharedPlugin
from .shortcutter import Shortcutter

class ShortcutterPlugin(SharedPlugin):

    def __init__(self):
        super().__init__("Shortcutter", "Shortcutter", mobase.VersionInfo(1,0,5, mobase.ReleaseType.ALPHA))

    def init(self, organiser=mobase.IOrganizer):
        self.shortcutter = Shortcutter(organiser)
        return super().init(organiser)
    
        