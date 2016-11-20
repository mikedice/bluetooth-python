from gi.repository import GObject
import dbus
import dbus.mainloop.glib

devices = {}

def interfaces_removed(path, interfaces):
    #print "Interface removed! :{}".format(interfaces)
    print "interfaces removed"

def interfaces_added(path, inter):
    print "Interfaces added"
    properties = inter["org.bluez.Device1"]
    for key in properties:
        printNameValue(key, properties[key])
    print

def properties_changed(interface, changed, invalidated, path):
    print "properties changed on interface {0} at path {1}".format(interface,path)
    print u"properties changed:" 
    for key in changed:
        printNameValue(key, changed[key])
    print

def property_changed(name, value):
    #print "property changed {}".format(name)
    print "property changed"

def printArray(value):
    outStr = "array:\n"
    for item in value:
        outStr += u"\t{0}\n".format(item)
    return outStr

def printValue(value):
    if isinstance(value, dbus.Array):
        return printArray(value)
    return value

def printNameValue(name, value):
    valuestr = repr(value)
    print u"{0} {1}".format(name, printValue(value))

# attach system dbus
dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

bus = dbus.SystemBus()

# attach to bluetooth interface
btobj = bus.get_object('org.bluez', '/org/bluez/hci0')

# reference to Adapter1 interface on the btobj
adapter=dbus.Interface(btobj, 'org.bluez.Adapter1')

bus.add_signal_receiver(interfaces_added,
    dbus_interface="org.freedesktop.DBus.ObjectManager",
    signal_name="InterfacesAdded")

bus.add_signal_receiver(interfaces_removed,
    dbus_interface="org.freedesktop.DBus.ObjectManager",
    signal_name="InterfacesRemoved")

bus.add_signal_receiver(properties_changed,
    dbus_interface="org.freedesktop.DBus.Properties",
    signal_name="PropertiesChanged",
    arg0="org.bluez.Device1",
    path_keyword="path")

bus.add_signal_receiver(property_changed,
    dbus_interface="org.bluez.Adapter1",
    signal_name="PropertyChanged")

om = dbus.Interface(bus.get_object("org.bluez", "/"),
    "org.freedesktop.DBus.ObjectManager")

objects = om.GetManagedObjects()

for path, interfaces in objects.iteritems():
    if "org.bluez.Device1" in interfaces:
        print "discovered device on startup at path: {0}".format(path)
        devices[path] = interfaces["org.bluez.Device1"]
        for key in devices[path]:
           printNameValue(key, devices[path][key]) 
        print

adapter.StartDiscovery()

mainLoop = GObject.MainLoop()
mainLoop.run()

