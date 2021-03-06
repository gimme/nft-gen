import yaml


_config = yaml.safe_load(open("config.yaml"))

size = int(_config.get("size"))
assets_scale = _config.get("assets-scale")
position_mode = _config.get("position-mode", "PIXELS")

output_dir = _config.get("output-dir")
assets_dir = _config.get("assets-dir")

background_color = _config.get("background-color")
shadow_position = eval(_config.get("shadow-position"))

primary_color_sign = _config.get("primary-color-sign")
accent_color_sign = _config.get("accent-color-sign")
