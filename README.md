# NeoVim note save
Automatically saves a file in the `~/notes/` directory using the content of the first non empty line as the name of the file.

This is intended for uses of NewVim as a sticky notes editor for the desktop.

# Install

Use your favorite Plug-In manager for NeoVim to add 'camilotorresf/neovim-note-save':

```
Plug 'camilotorresf/neovim-note-save'
```

Restart NeoVim then run these 2 commands:

```
:PlugInstall
:UpdateRemotePlugins
```

# Usage

This adds 2 commands:

* `:NoteWrite` - To automatically save the content of the file in the `~/notes/` directory, using the first line as the name of the file.
* `:NoteExcit` - To exit the editor trying to save the file first.

# Configuration

To save the notes to a different directory, add this to your `.config/nvim/init.vim`:

```
set note-save-directory=/home/camilo/mynotes
```

You can map your favorite keystrokes sequence to these commands:

```
nnoremap <Leader>nw :NoteWrite<CR>
nnoremap <Leader>nx :NoteExit<CR>
```

# Attribution

By Camilo Torres (https://github.com/camilotorresf/neovim-note-save)
