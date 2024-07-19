#!/bin/python3

# import module gtk
import os
import gi
import sys
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# variabel
try :
  text_out = sys.argv[1]
  title = sys.argv[2]
  
except :
  print("program need 1 arguments")
  exit()
  
# text info task
textview1 = Gtk.TextView()
textview1.set_editable(False) # edit text
textview1.set_cursor_visible(False) # garis tulis
textview1.get_buffer().set_text(str(text_out)) # write text

# scroll window
scroll = Gtk.ScrolledWindow()
scroll.add(textview1)

# window
win = Gtk.Window()
win.set_icon_from_file("/usr/share/icons/hicolor/scalable/apps/tools-menu.svg")
win.set_default_size(600, 300)
win.set_title(title + " help")
win.connect("delete-event", Gtk.main_quit)
win.add(scroll)
win.show_all()
Gtk.main()
