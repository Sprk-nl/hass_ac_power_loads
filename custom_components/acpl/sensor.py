import logging
from datetime import datetime
from datetime import timedelta

from homeassistant.const import CONF_RESOURCES
from homeassistant.components.sensor import SensorEntity, SensorDeviceClass
from homeassistant.helpers.restore_state import RestoreEntity

from .const import *
from .API import get_wastedata_from_config


_LOGGER = logging.getLogger(__name__)