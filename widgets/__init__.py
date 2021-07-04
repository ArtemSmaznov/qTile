import widgets.general as general
import widgets.sensors as sensor
import themes.default as theme


# Default widget settings
widget_defaults = dict(
    font=theme.font_regular,
    fontsize=11,
    padding=3,
    foreground=theme.foreground,
)

extension_defaults = widget_defaults.copy()