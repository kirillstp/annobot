import os
import subprocess
from time import sleep

LIB_PATH = "./resources/mp3/"
class Speaker:
    def __init__(self):
        self.proc = {}
        self.music_player_args = '-q'

    def _play(self, filename):
        
        filepath = os.path.join(LIB_PATH,filename)
        print(filepath)
        if os.path.exists(filepath):
            print("Playing {}".format(filepath))
            run = subprocess.Popen(['mpg123', self.music_player_args, filepath])
            sleep(3)
            self.proc[filename] = run
            return 0
        else:
            print("Error playing {}".format(filepath))
            return -1
    
    def _stop(self,filename):
        self.proc[filename].terminate()
        del self.proc[filename]

    def toggle(self,filename):
        if self.get_state(filename) == 'ON':
            self._stop(filename)
        else:
            self._play(filename)

    def get_state(self,filename):
        if filename in self.proc.keys():
            return "ON"
        else:
            return "OFF"
            
if __name__ == "__main__":
    filename = "Final.mp3"
    snd = Sound()
    snd._play(filename)
    sleep(10)
    snd._stop(filename)