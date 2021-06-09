import random


class SongLoader:
    """
    This class creates a textual reference to the musical stimuli and orders
    them by class into two lists
    """

    def __init__(self):
        self.playlist_phase_one = []
        self.playlist_phase_two = []
        self.prepare_song_classes()

    def prepare_song_classes(self):
        self.playlist_phase_one.append(['res\\class_1_A.ogg', 'res\\class_1_B.ogg'])
        self.playlist_phase_one.append(['res\\class_2_A.ogg', 'res\\class_2_B.ogg'])
        self.playlist_phase_one.append(['res\\class_3_A.ogg', 'res\\class_3_B.ogg'])
        self.playlist_phase_one.append(['res\\class_4_A.ogg', 'res\\class_4_B.ogg'])

        self.playlist_phase_two.append(['res\\class_1_B.ogg', 'res\\class_1_A.ogg'])
        self.playlist_phase_two.append(['res\\class_2_B.ogg', 'res\\class_2_A.ogg'])
        self.playlist_phase_two.append(['res\\class_3_B.ogg', 'res\\class_3_A.ogg'])
        self.playlist_phase_two.append(['res\\class_4_B.ogg', 'res\\class_4_A.ogg'])

    def generate_shuffle_playlist(self, phase='phase_1'):
        """
        This function generates a copy of one of the two playlists with class conditions
        in random order
        """

        if phase == 'phase_1':
            playlist = self.playlist_phase_one.copy()
            random.shuffle(playlist)
            return playlist
        elif phase == 'phase_2':
            playlist = self.playlist_phase_two.copy()
            random.shuffle(playlist)
            return playlist
        else:
            raise Exception('Please provide a valid argument: {phase_1} or {phase_2} are valid arguments')


song_loader = SongLoader()
print(song_loader.playlist_phase_one)
print(song_loader.playlist_phase_two)
print(song_loader.generate_shuffle_playlist('phase_1'))
print(song_loader.generate_shuffle_playlist('phase_2'))
print(song_loader.playlist_phase_one)
print(song_loader.playlist_phase_two)
