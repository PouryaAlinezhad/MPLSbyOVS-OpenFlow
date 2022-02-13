# MPLSbyOVS-OpenFlow
Implementing a MPLS network with OVS and OpenFlow <br />
Multiprotocol Label Switching (MPLS) is a mechanism in high-performance telecommunications networks<br />
that directs data from one network node to the next based on short path labels rather than long<br />
network addresses, avoiding complex lookups in a routing table. The labels identify virtual links<br />
(paths) between distant nodes rather than endpoints. MPLS can encapsulate packets of various network<br />
protocols.MPLS works by prefixing packets with an MPLS header, containing one or more<br />
labels. This is called a label stack.<br />
<br />
in the topology image the numbers in blue correspond to the label that the packets carry with them in each link.<br />
As you can see, when packets travel from h1 to h3:<br />
◦ The switch s1 pushes the label 12 and forwards the packet to switch s2.<br />
◦ The switch s2 swaps the label 12 for the label 23 and forwards the packet to switch s3<br />
◦ The switch s3 pops the label 23 and forwards the packet to host h3.<br />
This environment is set up using only mininet and Open vSwitch. Please note that the label stack<br />
of the packets is just one label deep, this is because currently Open vSwitch only supports one label.<br />
The whole experiment will be performed in userspace, as the OVS kernel module does not support<br />
MPLS yet. For this reason you we use the option ”datapath=user”.<br />
