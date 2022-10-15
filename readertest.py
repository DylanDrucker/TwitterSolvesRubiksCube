counter = 0
modified = os.stat("cubeStatus.txt").st_mtime

while counter < 5:
    stamp = os.stat("cubeStatus.txt").st_mtime
    if stamp != self._cached_stamp:
        self._cached_stamp = stamp

        print("changed")
        counter += 1