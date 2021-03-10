from libqtile import bar

import theme.default as theme
import widgets as my_widget
from utils import power_line


def init_panel_widgets(s='main'):
    if s == 'main':
        return [
            my_widget.separator(),
            my_widget.prompt_widget(),
            my_widget.time(),
            my_widget.layout_icon(),
            my_widget.group_box(),
            my_widget.separator(40),
            my_widget.window_name(),

            *power_line(1, my_widget.network),
            *power_line(2, my_widget.memory),
            *power_line(3, my_widget.thermals),
            *power_line(4, my_widget.volume),
            *power_line(5, my_widget.date),
            my_widget.sys_tray(),
        ]
    else:
        return [
            my_widget.separator(),
            my_widget.time(),
            my_widget.layout_icon(),
            my_widget.group_box(),
            my_widget.separator(40),
            my_widget.window_name(),

            *power_line(1, my_widget.network),
            *power_line(2, my_widget.memory),
            *power_line(3, my_widget.thermals),
            *power_line(4, my_widget.date),
        ]


def init_bar(s='main'):
    return bar.Bar(init_panel_widgets(s), theme.bar_size, background=theme.background, opacity=1)
