'Pourya Alinezhad'
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.log import setLogLevel, info
from mininet.node import RemoteController, OVSKernelSwitch
from mininet.cli import CLI
"""
Instructions to run the topo:
    1. Go to directory where this file is.
    2. run: sudo -E python create_net3.py
The topo has 3 switches and 3 hosts.
"""


class SimpleOVSSwitch(Topo):

    def __init__(self, **opts):
        """Create custom topo."""

        # Initialize topology
        # It uses the constructor for the Topo class
        super(SimpleOVSSwitch, self).__init__(**opts)

        # Add hosts and switches
        h1 = self.addHost('host1', ip="10.0.0.1/24", mac='00:00:00:00:00:01')
        h2 = self.addHost('host2', ip="10.0.0.2/24", mac='00:00:00:00:00:02')
        h3 = self.addHost('host3', ip="10.0.0.3/24", mac='00:00:00:00:00:03')

        # Adding switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        # Add links
        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(h3, s3)

        self.addLink(s1, s2)
        self.addLink(s2, s3)


def run():
    #c = RemoteController('c', '0.0.0.0', 6633)
    net = Mininet(topo=SimpleOVSSwitch(), switch=OVSKernelSwitch, controller=None,link=TCLink)
    #net.addController(c)
    net.start()

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()