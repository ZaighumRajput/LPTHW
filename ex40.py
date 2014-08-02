class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line


happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued"])

bulls_on_parade = Song(["They will rally around that family",
                        "With pockets full of shells"])

follow_me_gangster = Song(["Look in my eyes, you see it, I lay it for the cheddar ",
                           "Twice I bet my life, I could 5 or better"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

follow_me_gangster.sing_me_a_song()

hustlersPrayer = "If the game shakes me or breaks me"

skysTheLimit = Song([hustlersPrayer])

skysTheLimit.sing_me_a_song()