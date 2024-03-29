'''Tk module'''

from tkinter import SUNKEN, Frame, Label

from config.constants import BACKGROUND_COLOR, FOREGROUND_COLOR


class FrameTop:
    '''Frame for top window of Dathomir'''

    @classmethod
    def create(cls, gui):
        '''Setup title for window'''
        frame: Frame = Frame(gui.window, background=BACKGROUND_COLOR,
                             border=1, relief=SUNKEN)
        label_title: Label = Label(frame,
                                   text="HORUS",
                                   font=("Arial", 20),
                                   background=BACKGROUND_COLOR,
                                   foreground=FOREGROUND_COLOR
                                   )
        label_title.pack()
        label_text: str = "Backup manager for Github and \
Gitlab repositories"
        label_subtitle: Label = Label(frame,
                                      text=label_text,
                                      font=("Courrier", 12),
                                      background=BACKGROUND_COLOR,
                                      foreground=FOREGROUND_COLOR
                                      )
        label_subtitle.pack()
        frame.pack()
