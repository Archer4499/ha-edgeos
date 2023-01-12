"""
Support for update.
"""
from __future__ import annotations

import logging

from homeassistant.components.update import UpdateEntity
from homeassistant.core import HomeAssistant

from ..helpers.const import *
from ..models.base_entity import BaseEntity
from ..models.entity_data import EntityData

_LOGGER = logging.getLogger(__name__)


class CoreUpdate(BaseEntity, UpdateEntity):
    """Representation of an update entity."""

    @property
    def installed_version(self) -> str | None:
        """Version installed and in use."""
        return self.entity.details.get(ATTR_UPDATE_INSTALLED_VERSION)

    @property
    def latest_version(self) -> str | None:
        """Latest version available for install."""
        return self.entity.details.get(ATTR_UPDATE_LATEST_VERSION)

    @property
    def release_url(self) -> str | None:
        """URL to the full release notes of the latest version available."""
        return self.entity.details.get(ATTR_UPDATE_RELEASE_URL)

    @property
    def title(self) -> str | None:
        """Title of the software.
        This helps to differentiate between the device or entity name
        versus the title of the software installed.
        """
        return self.entity.details.get(ATTR_UPDATE_TITLE)

    @staticmethod
    def get_component(hass: HomeAssistant, entity: EntityData):
        update = CoreUpdate()
        update.initialize(hass, entity, DOMAIN_UPDATE)

        return update

    @staticmethod
    def get_domain():
        return DOMAIN_UPDATE
