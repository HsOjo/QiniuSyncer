import base64
import json
import os
import platform
import sys

from app.res.const import Const
from app.util import object_convert
from app.util.log import Log

sys_type = platform.system()

if sys_type == 'Darwin':
    CONFIG_NAME = ('com.%s.%s' % (Const.author, Const.app_name)).lower()
    CONFIG_PATH = os.path.expanduser('~/Library/Application Support/%s' % CONFIG_NAME)
else:
    CONFIG_NAME = '%s.cfg' % Const.app_name
    CONFIG_PATH = '%s/%s' % (os.path.dirname(sys.executable), CONFIG_NAME)


class ConfigBase:
    _protect_fields = [
    ]
    _config_path = CONFIG_PATH
    language = 'en'

    def load(self):
        try:
            if os.path.exists(self._config_path):
                with open(self._config_path, 'r') as io:
                    config = json.load(io)
                    for f in self._protect_fields:
                        config[f] = base64.b64decode(config[f][::-1].encode()).decode()
                    object_convert.dict_to_object(config, self, new_fields=False)
                    Log.set_replaces(
                        dict([(getattr(self, f), Const.protector) for f in self._protect_fields]))
                    Log.append('config_load', 'Info', object_convert.object_to_dict(self))
        except:
            self.save()

    def save(self):
        with open(self._config_path, 'w') as io:
            config = object_convert.object_to_dict(self)
            for f in self._protect_fields:
                config[f] = base64.b64encode(config[f].encode()).decode()[::-1]
            json.dump(config, io, indent='  ')
            Log.append('config_save', 'Info', object_convert.object_to_dict(self))

    def clear(self):
        if os.path.exists(self._config_path):
            os.unlink(self._config_path)
