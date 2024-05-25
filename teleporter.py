import time
import pkg_resources
import os
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])
if not "pyperclip==1.8.2" in installed_packages_list:
    os.system("pip install pyperclip==1.8.2")
else:pass
import pyperclip

class TeleporterTime(object):
    def __init__(self):
        pass

    def get_time(self) -> str:
        return time.time()
    
    def normal_time(self) -> str:
        return time.ctime(time.time())

    def format_string(self, text: str):
        data = self.normal_time().split()
        return text.replace("$Y", data[-1]).replace("$D", data[2]).replace("$M", data[1]).replace("$WD", data[0]).replace("$h", data[3].split(":")[0]).replace("$m",  data[3].split(":")[1]).replace("$s",  data[3].split(":")[2])
    
    def copy(self, obj: str):
        try:
            pyperclip.copy(obj)
            return True
        except:
            return False
        
    def is_weak_day(self, inp: str = ""):
        day = self.format_string("$WD")
        if inp == day:return True
        else:return False

    def is_day(self, inp: str = ""):
        day = self.format_string("$D")
        if inp == day:return True
        else:return False

    def is_month(self, inp: str = ""):
        month = self.format_string("$M")
        if inp == month:return True
        else:return False

    def is_year(self, inp: str = ""):
        year = self.format_string("$Y")
        if inp == year:return True
        else:return False

    def is_hour(self, inp: str = ""):
        hour = self.format_string("$h")
        if inp == hour:return True
        else:return False

    def is_minute(self, inp: str = ""):
        minute = self.format_string("$m")
        if inp == minute:return True
        else:return False

    def is_sec(self, inp: str = ""):
        sec = self.format_string("$s")
        if inp == sec:return True
        else:return False

    @property
    def getAboutDate(self) -> dict:
        app = self.format_string("$Y $M $D $WD $h $m $s").split()
        return {
            "raw_time": self.get_time(),
            "raw_time_hr": self.normal_time(),
            "year": app[0],
            "month": app[1],
            "day": app[2],
            "week_day": app[3],
            "hour": app[4],
            "minutes": app[5],
            "seconds": app[6]
        }