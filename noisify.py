import rumps
from rumps import *
import vlc


class Noisify(rumps.App):

    def __init__(self):
        super(Noisify, self).__init__(name="Noisify")
        self.template = True
        self.icon = "whiteNoise.icns"
        self.player = vlc.Instance()
        self.media_list = self.player.media_list_new()
        self.media_player = self.player.media_list_player_new()
        self.media = self.player.media_new("noise.webm")
        self.media_list.add_media(self.media)
        self.media_player.set_media_list(self.media_list)
        self.menu = [
            rumps.MenuItem(title="About Noisify"),
            None,
            rumps.MenuItem(title="Play", icon='playPadded.png', template=True, key="P", callback=self.playAudio),
            None,
        ]
        self.playing = self.media_player.is_playing()

    @rumps.clicked("About Noisify")
    def aboutWindow(self, _):
        """Show a simple 'about' window."""
        rumps.alert(title="Noisify", ok="Close",
                    message="© 2021 Danny Taylor\nVersion: 0.1.0\nContact: hello@dannytaylor.se")

    def playAudio(self, sender):
        if sender.title == "Play":
            self.media_player.play()
            sender.title = "Stop"
            sender.icon = "stopPadded.png"
            self.icon = "playing.png"
        else:
            self.media_player.stop()
            sender.title = "Play"
            sender.icon = "playPadded.png"
            self.icon = "whiteNoise.icns"


if __name__ == "__main__":
    Noisify().run()
