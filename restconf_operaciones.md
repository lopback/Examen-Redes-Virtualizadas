# Ítem 5 – Operaciones RESTCONF desde Postman

## 1. DELETE Loopback111
- Método: DELETE
- URL: /restconf/data/ietf-interfaces:interfaces/interface=Loopback111

## 2. PUT Loopback33 (apagada)
- Método: PUT
- URL: /restconf/data/ietf-interfaces:interfaces/interface=Loopback33
- Body:
{
  "ietf-interfaces:interface": {
    "name": "Loopback33",
    "type": "iana-if-type:softwareLoopback",
    "enabled": false,
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "33.33.33.33",
          "netmask": "255.255.255.255"
        }
      ]
    }
  }
}

## 3. GET Interfaces
- Método: GET
- URL: /restconf/data/ietf-interfaces:interfaces
