from scapy.all import *

TYPE_Debug = 0x1212
TYPE_IPV4 = 0x0800

class Debug(Packet):
   name = "Debug"
   fields_desc = [
       ShortField("pid", 0),
        ShortField("debug_field", 0),
    ]
   def mysummary(self):
        return self.sprintf("pid=%pid%, debug_field=%debug_field%")

bind_layers(Ether, Debug, type=TYPE_Debug)
bind_layers(Debug, IP, pid=TYPE_IPV4)