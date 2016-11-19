# top level dbus objects
qdbus

# system dbus objects
qdbus --system

# the org.bluez objects
qdbus --system org.bluez

# the hci0 bluetooth device. Shows the APi of the hci0 device
qdbus --system org.bluez /org/bluez/hci0

# the hci0 bluetooth device's adapter address
qdbus --system org.bluez /org/bluez/hci0 org.bluez.Adapter1.Address

