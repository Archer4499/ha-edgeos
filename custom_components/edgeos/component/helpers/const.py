"""
Support for Constants.
"""
from datetime import timedelta

import aiohttp
import voluptuous as vol

import homeassistant.helpers.config_validation as cv

from ...core.helpers.const import *
from .enums import InterfaceTypes

ATTR_FRIENDLY_NAME = "friendly_name"

CONF_DEVICE_ID = "device_id"

WS_MAX_MSG_SIZE = 0
WS_RECONNECT_INTERVAL = timedelta(seconds=30)
WS_TIMEOUT = timedelta(minutes=1)
WS_WARNING_INTERVAL = timedelta(seconds=95)

WS_COMPRESSION_DEFLATE = 15

DEFAULT_UPDATE_API_INTERVAL = timedelta(minutes=1)
DEFAULT_UPDATE_ENTITIES_INTERVAL = timedelta(seconds=1)
DEFAULT_HEARTBEAT_INTERVAL = timedelta(seconds=50)
DEFAULT_CONSIDER_AWAY_INTERVAL = timedelta(minutes=3)

STORAGE_DATA_FILE_CONFIG = "config"
STORAGE_API_LIST = "list"
STORAGE_API_DATA_API = "api"
STORAGE_API_DATA_WS = "ws"
STORAGE_API_DATA_HA = "ha"

STORAGE_DATA_FILES = [
    STORAGE_DATA_FILE_CONFIG
]

STORAGE_API_DATA = [
    STORAGE_API_DATA_API,
    STORAGE_API_DATA_WS,
    STORAGE_API_DATA_HA
]

MESSAGES_COUNTER_SECTION = "messages"

STORAGE_DATA_MONITORED_INTERFACES = "monitored-interfaces"
STORAGE_DATA_MONITORED_DEVICES = "monitored-devices"
STORAGE_DATA_UNIT = "unit"
STORAGE_DATA_LOG_INCOMING_MESSAGES = "log-incoming-messages"
STORAGE_DATA_CONSIDER_AWAY_INTERVAL = "consider-away-interval"
STORAGE_DATA_UPDATE_ENTITIES_INTERVAL = "update-entities-interval"
STORAGE_DATA_UPDATE_API_INTERVAL = "update-api-interval"

API_DATA_LAST_UPDATE = "lastUpdate"

API_DATA_PRODUCT = "product"
API_DATA_SYSTEM = "system"
API_DATA_INTERFACES = "interfaces"
API_DATA_SESSION_ID = "session-id"
API_DATA_COOKIES = "cookies"

API_DATA_SAVE = "SAVE"

API_GET = "get"
API_SET = "set"
API_DELETE = "delete"
API_DATA = "data"

API_URL_PARAMETER_BASE_URL = "base_url"
API_URL_PARAMETER_TIMESTAMP = "timestamp"
API_URL_PARAMETER_ACTION = "action"
API_URL_PARAMETER_SUBSET = "subset"

API_URL_HEARTBEAT = "{base_url}?_={timestamp}"
API_URL_DATA = "{base_url}/api/edge/{action}.json"
API_URL_DATA_SUBSET = f"{API_URL_DATA}?data={{subset}}"

TRUE_STR = "true"
FALSE_STR = "false"

LINK_ENABLED = "up"
LINK_CONNECTED = "l1up"

INTERFACES_STATS = "stats"

BYTE = 1
KILO_BYTE = BYTE * 1024
MEGA_BYTE = KILO_BYTE * 1024

# CHANGE TO API DATA
API_DATA_DHCP_STATS = "dhcp_stats"
API_DATA_SYS_INFO = "sys_info"
API_DATA_DHCP_LEASES = "dhcp-leases"

DATA_SYSTEM_SERVICE = "service"
DATA_SYSTEM_SERVICE_DHCP_SERVER = "dhcp-server"

DHCP_SERVER_LEASES = "dhcp-server-leases"
DHCP_SERVER_STATS = "dhcp-server-stats"
DHCP_SERVER_LEASED = "leased"
DHCP_SERVER_LEASES_CLIENT_HOSTNAME = "client-hostname"
DHCP_SERVER_SHARED_NETWORK_NAME = "shared-network-name"
DHCP_SERVER_SUBNET = "subnet"
DHCP_SERVER_STATIC_MAPPING = "static-mapping"
DHCP_SERVER_IP_ADDRESS = "ip-address"
DHCP_SERVER_MAC_ADDRESS = "mac-address"

WS_INTERFACES_KEY = "interfaces"
WS_SYSTEM_STATS_KEY = "system-stats"
WS_EXPORT_KEY = "export"
WS_DISCOVER_KEY = "discover"

WS_RECEIVED_MESSAGES = "received-messages"
WS_IGNORED_MESSAGES = "ignored-messages"
WS_ERROR_MESSAGES = "error-messages"

WS_MESSAGES = [
    WS_RECEIVED_MESSAGES,
    WS_IGNORED_MESSAGES,
    WS_ERROR_MESSAGES
]

UPDATE_DATE_ENDPOINTS = [
    API_DATA_SYS_INFO,
    API_DATA_DHCP_STATS,
    API_DATA_DHCP_LEASES
]

DISCOVER_DATA_FW_VERSION = "fwversion"
DISCOVER_DATA_PRODUCT = "product"

SYSTEM_STATS_DATA_UPTIME = "uptime"
SYSTEM_STATS_DATA_CPU = "cpu"
SYSTEM_STATS_DATA_MEM = "mem"

ATTR_KILO = "KBytes"
ATTR_MEGA = "MBytes"
ATTR_BYTE = "Bytes"

UNIT_MAPPING = {
    ATTR_BYTE: BYTE,
    ATTR_KILO: KILO_BYTE,
    ATTR_MEGA: MEGA_BYTE
}

UNIT_OF_MEASUREMENT_MAPPING = {
    ATTR_BYTE: "B",
    ATTR_KILO: "KB",
    ATTR_MEGA: "MB"
}

DEVICE_LIST = "devices"
ADDRESS_LIST = "addresses"
FW_LATEST = "addresses"
ADDRESS_IPV4 = "ipv4"
ADDRESS_HW_ADDR = "hwaddr"
LAST_ACTIVITY = "Last Activity"

RESPONSE_SUCCESS_KEY = "success"
RESPONSE_ERROR_KEY = "error"
RESPONSE_OUTPUT = "output"
RESPONSE_FAILURE_CODE = "0"

HEARTBEAT_MAX_AGE = 15

WS_TOPIC_NAME = "name"
WS_TOPIC_UNSUBSCRIBE = "UNSUBSCRIBE"
WS_TOPIC_SUBSCRIBE = "SUBSCRIBE"
WS_SESSION_ID = "SESSION_ID"

SERVICE_UPDATE_CONFIGURATION = "update_configuration"

EMPTY_STRING = ""
BEGINS_WITH_SIX_DIGITS = "^([0-9]{1,6})"

STRING_DASH = "-"
STRING_UNDERSCORE = "_"
STRING_COMMA = ","
STRING_COLON = ":"

SYSTEM_DATA_HOSTNAME = "host-name"
SYSTEM_DATA_DOMAIN_NAME = "domain-name"
SYSTEM_DATA_NTP = "ntp"
SYSTEM_DATA_NTP_SERVER = "server"
SYSTEM_DATA_OFFLOAD = "offload"
SYSTEM_DATA_OFFLOAD_HW_NAT = "hwnat"
SYSTEM_DATA_OFFLOAD_IPSEC = "ipsec"
SYSTEM_DATA_TRAFFIC_ANALYSIS = "traffic-analysis"
SYSTEM_DATA_TRAFFIC_ANALYSIS_DPI = "dpi"
SYSTEM_DATA_TRAFFIC_ANALYSIS_EXPORT = "export"
SYSTEM_DATA_TIME_ZONE = "time-zone"
SYSTEM_DATA_LOGIN = "login"
SYSTEM_DATA_LOGIN_USER = "user"
SYSTEM_DATA_LOGIN_USER_LEVEL = "level"

USER_LEVEL_ADMIN = "admin"

SYSTEM_INFO_DATA_FW_LATEST = "fw-latest"
SYSTEM_INFO_DATA_FW_LATEST_STATE = "state"
SYSTEM_INFO_DATA_FW_LATEST_VERSION = "version"
SYSTEM_INFO_DATA_FW_LATEST_URL = "url"

SYSTEM_INFO_DATA_FW_CHANGELOG_URL = "https://www.ui.com/download/edgemax"

FW_LATEST_STATE_CAN_UPGRADE = "can-upgrade"

SYSTEM_INFO_DATA_SW_VER = "sw_ver"

SYSTEM_DATA_ENABLE = "enable"
SYSTEM_DATA_DISABLE = "disable"

INTERFACE_DATA_NAME = "name"
INTERFACE_DATA_DESCRIPTION = "description"
INTERFACE_DATA_TYPE = "type"
INTERFACE_DATA_DUPLEX = "duplex"
INTERFACE_DATA_SPEED = "speed"
INTERFACE_DATA_BRIDGE_GROUP = "bridge-group"
INTERFACE_DATA_ADDRESS = "address"
INTERFACE_DATA_AGING = "aging"
INTERFACE_DATA_BRIDGED_CONNTRACK = "bridged-conntrack"
INTERFACE_DATA_HELLO_TIME = "hello-time"
INTERFACE_DATA_MAX_AGE = "max-age"
INTERFACE_DATA_PRIORITY = "priority"
INTERFACE_DATA_PROMISCUOUS = "promiscuous"
INTERFACE_DATA_STP = "stp"
INTERFACE_DATA_RECEIVED = "received"
INTERFACE_DATA_SENT = "sent"
INTERFACE_DATA_MULTICAST = "multicast"
INTERFACE_DATA_STATS = "stats"
INTERFACE_DATA_UP = "up"
INTERFACE_DATA_LINK_UP = "l1up"
INTERFACE_DATA_MAC = "mac"
INTERFACE_DATA_HANDLER = "handler"

DEVICE_DATA_NAME = "hostname"
DEVICE_DATA_DOMAIN = "domain"
DEVICE_DATA_IP = "ip"
DEVICE_DATA_MAC = "mac"
DEVICE_DATA_RECEIVED = "received"
DEVICE_DATA_SENT = "sent"

TRAFFIC_DATA_DIRECTION = "direction"
TRAFFIC_DATA_RATE = "rate"
TRAFFIC_DATA_TOTAL = "total"
TRAFFIC_DATA_ERRORS = "errors"
TRAFFIC_DATA_PACKETS = "packets"
TRAFFIC_DATA_DROPPED = "dropped"
TRAFFIC_DATA_LAST_ACTIVITY = "last_activity"
TRAFFIC_DATA_LAST_ACTIVITY_IN_SECONDS = "last_activity_in_seconds"

TRAFFIC_STATS_BPS_KEY = "bps"
TRAFFIC_STATS_BYTES = "bytes"

TRAFFIC_DATA_DIRECTION_SENT = "tx"
TRAFFIC_DATA_DIRECTION_RECEIVED = "rx"

TRAFFIC_DATA_DIRECTIONS = [
    TRAFFIC_DATA_DIRECTION_SENT,
    TRAFFIC_DATA_DIRECTION_RECEIVED
]

TRAFFIC_DATA_INTERFACE_ITEMS = {
    TRAFFIC_STATS_BPS_KEY: TRAFFIC_DATA_RATE,
    TRAFFIC_STATS_BYTES: TRAFFIC_DATA_TOTAL,
    TRAFFIC_DATA_ERRORS: TRAFFIC_DATA_ERRORS,
    TRAFFIC_DATA_PACKETS: TRAFFIC_DATA_PACKETS,
    TRAFFIC_DATA_DROPPED: TRAFFIC_DATA_DROPPED
}

TRAFFIC_DATA_DEVICE_ITEMS = {
    TRAFFIC_DATA_RATE: TRAFFIC_DATA_RATE,
    TRAFFIC_STATS_BYTES: TRAFFIC_DATA_TOTAL
}

INTERFACES_MAIN_MAP = [
    INTERFACE_DATA_UP,
    INTERFACE_DATA_LINK_UP,
    INTERFACE_DATA_SPEED,
    INTERFACE_DATA_DUPLEX,
    INTERFACE_DATA_MAC,
]

DISCOVER_DEVICE_ITEMS = [
    DEVICE_DATA_NAME,
    DISCOVER_DATA_PRODUCT,
    SYSTEM_STATS_DATA_UPTIME,
    DISCOVER_DATA_FW_VERSION,
    "system_status"
]

SERVICE_SCHEMA_UPDATE_CONFIGURATION = vol.Schema(
    {
        vol.Required(CONF_DEVICE_ID): cv.string,
        vol.Optional(STORAGE_DATA_CONSIDER_AWAY_INTERVAL.replace(STRING_DASH, STRING_UNDERSCORE)): vol.Range(10, 1800),
        vol.Optional(STORAGE_DATA_UPDATE_ENTITIES_INTERVAL.replace(STRING_DASH, STRING_UNDERSCORE)): vol.Range(1, 60),
        vol.Optional(STORAGE_DATA_UPDATE_API_INTERVAL.replace(STRING_DASH, STRING_UNDERSCORE)): vol.Range(30, 180),
        vol.Optional(STORAGE_DATA_LOG_INCOMING_MESSAGES.replace(STRING_DASH, STRING_UNDERSCORE)): cv.boolean,
        vol.Optional(STORAGE_DATA_UNIT.replace(STRING_DASH, STRING_UNDERSCORE)): vol.In(UNIT_MAPPING.keys()),
    }
)

WS_CLOSING_MESSAGE = [
    aiohttp.WSMsgType.CLOSE,
    aiohttp.WSMsgType.CLOSED,
    aiohttp.WSMsgType.CLOSING,
]

SPECIAL_INTERFACES = {
    InterfaceTypes.PPPOE_PREFIX: "Internet Dail-Up",
    InterfaceTypes.SWITCH_PREFIX: "Switch",
    InterfaceTypes.VIRTUAL_TUNNEL_PREFIX: "Virtual Tunnel",
    InterfaceTypes.OPEN_VPN_PREFIX: "OpenVPN",
    InterfaceTypes.BONDING_PREFIX: "VLAN"
}

IGNORED_INTERFACES = [
    InterfaceTypes.LOOPBACK
]

RECEIVED_RATE_PREFIX = "Received Rate"
RECEIVED_TRAFFIC_PREFIX = "Received Traffic"
RECEIVED_DROPPED_PREFIX = "Received Dropped"
RECEIVED_ERRORS_PREFIX = "Received Errors"
RECEIVED_PACKETS_PREFIX = "Received Packets"

SENT_RATE_PREFIX = "Sent Rate"
SENT_TRAFFIC_PREFIX = "Sent Traffic"
SENT_DROPPED_PREFIX = "Sent Dropped"
SENT_ERRORS_PREFIX = "Sent Errors"
SENT_PACKETS_PREFIX = "Sent Packets"

RECEIVED_RATE_ICON = "mdi:download-network-outline"
RECEIVED_TRAFFIC_ICON = "mdi:download-network-outline"
RECEIVED_DROPPED_ICON = "mdi:package-variant-minus"
RECEIVED_ERRORS_ICON = "mdi:timeline-alert"
RECEIVED_PACKETS_ICON = "mdi:package-up"

SENT_RATE_ICON = "mdi:upload-network-outline"
SENT_TRAFFIC_ICON = "mdi:upload-network-outline"
SENT_DROPPED_ICON = "mdi:package-variant-minus"
SENT_ERRORS_ICON = "mdi:timeline-alert"
SENT_PACKETS_ICON = "mdi:package-up"

STATS_ICONS = {
    RECEIVED_RATE_PREFIX: RECEIVED_RATE_ICON,
    RECEIVED_TRAFFIC_PREFIX: RECEIVED_TRAFFIC_ICON,
    RECEIVED_DROPPED_PREFIX: RECEIVED_DROPPED_ICON,
    RECEIVED_ERRORS_PREFIX: RECEIVED_ERRORS_ICON,
    RECEIVED_PACKETS_PREFIX: RECEIVED_PACKETS_ICON,
    SENT_RATE_PREFIX: SENT_RATE_ICON,
    SENT_TRAFFIC_PREFIX: SENT_TRAFFIC_ICON,
    SENT_DROPPED_PREFIX: SENT_DROPPED_ICON,
    SENT_ERRORS_PREFIX: SENT_ERRORS_ICON,
    SENT_PACKETS_PREFIX: SENT_PACKETS_ICON,
}

STATS_RATE = [
    RECEIVED_RATE_PREFIX,
    SENT_RATE_PREFIX
]

STATS_TRAFFIC = [
    RECEIVED_TRAFFIC_PREFIX,
    SENT_TRAFFIC_PREFIX
]

STATS_UNITS = {
    RECEIVED_DROPPED_PREFIX: TRAFFIC_DATA_DROPPED,
    RECEIVED_ERRORS_PREFIX: TRAFFIC_DATA_ERRORS,
    RECEIVED_PACKETS_PREFIX: TRAFFIC_DATA_PACKETS,
    SENT_DROPPED_PREFIX: TRAFFIC_DATA_DROPPED,
    SENT_ERRORS_PREFIX: TRAFFIC_DATA_ERRORS,
    SENT_PACKETS_PREFIX: TRAFFIC_DATA_PACKETS,
}
