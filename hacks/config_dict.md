Updating the module dictionary so that we can use config.VAR_NAME while accessing the variable

```python
# Inside config.py
import sys

import yaml


def load_config(config_file):
    _module = sys.modules[__name__]
    with open(config_file) as gw_config:
        config_dict = yaml.safe_load(gw_config)
        _module.__dict__.update(config_dict)
```


Read more at https://stackoverflow.com/questions/5365562/why-is-the-value-of-name-changing-after-assignment-to-sys-modules-name
