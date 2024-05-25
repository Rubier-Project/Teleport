# Teleporter Documention

## import
```python3
from teleporter import TeleporterTime
```
## get stamp time
```python3
from teleporter import TeleporterTime

app = TeleporterTime()
value = app.get_time()
print(value)
```
## get normal time (date)
```python3
from teleporter import TeleporterTime

app = TeleporterTime()
value = app.normal_time()
print(value)
```
## format string
```python3
from teleporter import TeleporterTime

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

## is Objects
+ These are get an input and compare with the system time

## copy
```python3
from teleporter import TeleporterTime

app = TeleporterTime()
value = app.copy(app.format_string("$Y-$M-$D $WD $h:$m:$s"))
print(value) # output: True if data saved in clipboard
```
## all info
```python3
from teleporter import TeleporterTime

app = TeleporterTime()
value = app.getAboutDate
print(value) # JSON / Dictionary outputed
```

# Download With GIT
`git clone https://github.com/Rubier-Project/Teleport`
`cd Teleport`
`touch test.py`
`vim test.py`
+ and enjoy with that
