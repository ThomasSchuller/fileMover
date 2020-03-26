import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import json
import os.path


class FileHandler(FileSystemEventHandler):
  i=1
  def on_modified(self, event):
    for filename in os.listdir(folder_tracked):
      src = folder_tracked + "/" + filename
      new_destination = folder_destination + '/' + filename
      os.rename(src, new_destination)

homedir = os.path.expanduser("~")

print(homedir)

folder_tracked = homedir + '/Downloads'
folder_destination = homedir + '/Desktop'

event_handler = FileHandler()
observer = Observer()
observer.schedule(event_handler, folder_tracked, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()