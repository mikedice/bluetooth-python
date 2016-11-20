import dbus

#
# attach system bus
bus = dbus.SystemBus()

# reference org.bluez object, hci0 path
btobj = bus.get_object('org.bluez', '/org/bluez/hci0')

# get the introspectable interface and introspect on the bt object.
# will dump out an xml string with all the bluetooth stuff in it
iface = dbus.Interface(btobj, 'org.freedesktop.DBus.Introspectable')
xml_string = iface.Introspect()

# save the XML file. Later you can open it in Chromium to inspect it
f = open('out.xml', 'w')
f.write(xml_string)

