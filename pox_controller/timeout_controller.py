from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpid_to_str
from pox.lib.recoco import Timer

log = core.getLogger()

blocked = False

def toggle_block():
    global blocked
    blocked = not blocked
    if blocked:
        log.info("Blocking traffic")
    else:
        log.info("Allowing traffic")

class TimeoutSwitch(object):
    def __init__(self, connection):
        self.connection = connection
        connection.addListeners(self)

        msg = of.ofp_flow_mod(command=of.OFPFC_DELETE)
        connection.send(msg)

        msg = of.ofp_flow_mod()
        msg.priority = 0
        msg.actions.append(of.ofp_action_output(port=of.OFPP_CONTROLLER))
        connection.send(msg)

        Timer(5, toggle_block, recurring=True)

    def _handle_PacketIn(self, event):
        global blocked

        msg = of.ofp_packet_out()
        msg.data = event.ofp

        if not blocked:
            msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))

        self.connection.send(msg)

def start_switch(event):
    log.info("Controlling %s" % (dpid_to_str(event.dpid)))
    TimeoutSwitch(event.connection)

def launch():
    core.openflow.addListenerByName("ConnectionUp", start_switch)
