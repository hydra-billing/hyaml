import re
from ipaddress import ip_address, ip_network, IPv4Address, IPv4Network
from hyaml.methods.prelude.string import is_like, regexp_replace


def is_mac(string):
    return is_like(regexp_replace(string.lower(), "[^a-f\\d]"), "^[a-f\\d]{12}$")


def is_ip4(string):
    try:
        return isinstance(ip_address(string), IPv4Address)
    except ValueError:
        return False


_private_networks = [
    IPv4Network("10.0.0.0/8"),
    IPv4Network("172.16.0.0/12"),
    IPv4Network("192.168.0.0/16"),
]


def is_private_ip4(string):
    try:
        address = ip_address(string)

        if not isinstance(address, IPv4Address):
            return False

        for network in _private_networks:
            if address in network:
                return True

        return False
    except ValueError:
        return False


def is_ip4_mask(string):
    try:
        network = ip_network("0.0.0.0/%s" % string)

        return (
            isinstance(network.netmask, IPv4Address) and str(network.netmask) == string
        )
    except ValueError:
        return False


def ip4_and(string, mask):
    return str(ip_address(int(ip_address(string)) & int(ip_address(mask))))


def ip4_or(string, mask):
    return str(ip_address(int(ip_address(string)) | int(ip_address(mask))))


def ip4_scan(string):
    match = re.search(
        "(?:(?:25[0-5]|2[0-4]\\d|[01]?\\d\\d?)\\.){3}"
        "(?:25[0-5]|2[0-4]\\d|[01]?\\d\\d?)",
        string,
    )

    if match is None:
        return ""
    else:
        return match.group(0)


def format_mac(string, separator="-", groups=6):
    raw = re.sub("[^A-F0-9]", "", string.upper())
    group_size = 12 // groups

    return separator.join(
        [raw[(i * group_size) : (i + 1) * group_size] for i in range(groups)]
    )


def normalize_mac(string):
    return format_mac(string)


def to_subnet_mask(number):
    network = ip_network("0.0.0.0/%s" % number)

    return str(network.netmask)


def to_subnet_suffix(string):
    network = ip_network("0.0.0.0/%s" % string)

    return "{0:b}".format(int(network.netmask)).count("1")

