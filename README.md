ParallelADB
=============
Enable adb command parallel run in all connected devices.


Install
-------
``` sh
$ pip install parallel-adb
```

Example
-------
``` python
from paralleladb import ParallelADB

outputs = ParallelADB.run('pm list packages')

for o in outputs:
    print(o)

# Output: ADBOutputs(serial='emulator-x', results=['...'])

outputs = ParallelADB.run('forward tcp:4274 tcp:4724', is_shell_cmd=False, print_result=True)

for o in outputs:
    print(o)

outputs = ParallelADB.run('cd /sdcard && ls', serials=['emulator-5554'])

for o in outputs:
    print(o)
```