import os.path
import pynvim

version = '0.1.0'

@pynvim.plugin
class NoteSave(object):

    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.command(name='NoteWrite')
    def note_save(self):
        directory_to_save_notes = self.nvim.vars.get('note-save-directory', '~/notes')
        first_line = self.nvim.current.buffer[0]
        if first_line:
            file_name = os.path.join(directory_to_save_notes, first_line)
            self.nvim.command('w {}'.format(file_name))
            return True
        return False

    @pynvim.command(name='NoteExit')
    def note_exit(self):
        if self.note_save():
            self.nvim.command('x')
            return True
        else:
            self.nvim.command('q!')
            return False
