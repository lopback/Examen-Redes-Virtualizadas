from netmiko import ConnectHandler


router = {
    "device_type": "cisco_ios",
    "host": "192.168.56.101",
    "username": "cisco",
    "password": "cisco"
}

# Conexión al router
conexion = ConnectHandler(**router)


comandos_config = [
    "router ospf 10",
    "router-id 1.1.1.1",
    "network 192.168.56.0 0.0.0.255 area 0",
    "passive-interface default",
    "no passive-interface Loopback0",
    "exit",
    "ipv6 unicast-routing",
    "interface Loopback44",
    "ipv6 enable",
    "ipv6 ospf 10 area 0",
    "interface GigabitEthernet1",
    "ipv6 enable",
    "ipv6 ospf 10 area 0",
    "router ospfv3 10",
    "router-id 2.2.2.2"
]

print("Configurando OSPF...")
salida_config = conexion.send_config_set(comandos_config)
print(salida_config)


print("=== Interfaces ===")
print(conexion.send_command("show ip interface brief"))

print("=== Running Config (OSPF) ===")
print(conexion.send_command("show running-config | section ospf"))

print("=== Versión del router ===")
print(conexion.send_command("show version"))

conexion.disconnect()
