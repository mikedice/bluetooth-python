import dbus

# attach system dbus
sysBus = dbus.SystemBus()

# attach to bluetooth interface
btobj = sysBus.get_object('org.bluez','/org/bluez/hci0')

# reference to Adapter1 interface on the btobj
adap1=dbus.Interface(btobj, 'org.bluez.Adapter1')

# reference to the Properties interface on btobj
adap1Props=dbus.Interface(btobj, 'org.freedesktop.DBus.Properties')

# get the address property. Returns a dbus.String. Not very useful in your python code
dbusAddress = adap1Props.Get('org.bluez.Adapter1', 'Address')

# convert the address to a python string
address = str(dbusAddress)

# get the Powered property. Returns a dbus.Boolean object. Not very useful in your python code
dbusIsPowered = adap1Props.Get('org.bluez.Adapter1', 'Powered')

# convert dbusIsPowered to python boolean
isPowered = bool(dbusIsPowered)

print("bluetooth address: {0} and is powered on: {1}".format(address, isPowered))

