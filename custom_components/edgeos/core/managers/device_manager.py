import logging

from homeassistant.helpers.device_registry import async_get

from ...configuration.helpers.const import DEFAULT_NAME

_LOGGER = logging.getLogger(__name__)


class DeviceManager:
    def __init__(self, hass, ha):
        self._hass = hass
        self._ha = ha

        self._devices = {}

    @property
    def title(self):
        title = self._ha.config_data.entry.title

        return title

    @property
    def devices(self):
        return self._devices

    async def async_remove_entry(self, entry_id):
        dr = async_get(self._hass)
        dr.async_clear_config_entry(entry_id)

    async def delete_device(self, name: str):
        _LOGGER.info(f"Deleting device {name}")

        device = self._devices.get(name)

        if device is not None:
            device_identifiers = device.get("identifiers", {})
            device_connections = device.get("connections", {})

            dr = async_get(self._hass)

            device_dr = dr.async_get_device(device_identifiers, device_connections)

            if device_dr is not None:
                if device.get("via_device") == (DEFAULT_NAME, self._ha.system_name):
                    dr.async_update_device(device_dr.id, via_device_id=None)

                config_id = self._ha.entry_id
                dr.async_update_device(device_dr.id, remove_config_entry_id=config_id)

    async def async_remove(self):
        for device_name in self._devices:
            await self.delete_device(device_name)

    def get(self, name):
        return self._devices.get(name, {})

    def set(self, name, device_info):
        self._devices[name] = device_info
