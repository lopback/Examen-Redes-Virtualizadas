from ncclient import manager

router = {
    "host": "192.168.56.101", 
    "port": 830,
    "username": "cisco",
    "password": "cisco",
    "hostkey_verify": False
}

config_hostname = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname>ChaconRivera</hostname>
  </native>
</config>
"""

config_loopback = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <Loopback>
        <name>111</name>
        <ip>
          <address>
            <primary>
              <address>111.111.111.111</address>
              <mask>255.255.255.255</mask>
            </primary>
          </address>
        </ip>
      </Loopback>
    </interface>
  </native>
</config>
"""

with manager.connect(**router) as m:
    m.edit_config(target="running", config=config_hostname)
    m.edit_config(target="running", config=config_loopback)
