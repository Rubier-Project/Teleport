# Teleporter Documention

## import
```
from teleporter.teleporter import TeleporterTime
```
## get stamp time
```
from teleporter.teleporter import TeleporterTime

app = TeleporterTime()
value = app.get_time()
print(value)
```
## get normal time (date)
```
from teleporter.teleporter import TeleporterTime

app = TeleporterTime()
value = app.normal_time()
print(value)
```
## format string
```
from teleporter.teleporter import TeleporterTime

app = TeleporterTime()
value = app.format_string("$Y-$M-$D $WD $h:$m:$s")
print(value)
```
+ $Y: year
+ $M: month
+ $D: Day (number)
+ $WD: Weak Day
+ $h: hour
+ $m: minute
+ $s: seconds
  
