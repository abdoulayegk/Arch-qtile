from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import subprocess
import os
from libqtile import hook

# Programs
terminal = "kitty"
web_browser = "firefox"

# Quick Settings
default_font = "Iosevka Regular"
bar_spacing = 8
bar_padding = 20
part_padding = 20

# Presets: , , ██, ░▒▓▓▒░
bar_left = ""
bar_right = ""


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([home])


# Colors
catppuccin = {
    "flamingo": "#F3CDCD",
    "mauve": "#DDB6F2",
    "pink": "#f5c2e7",
    "maroon": "#e8a2af",
    "red": "#f28fad",
    "peach": "#f8bd96",
    "yellow": "#fae3b0",
    "green": "#abe9b3",
    "teal": "#b4e8e0",
    "blue": "#96cdfb",
    "sky": "#89dceb",
    "white": "#d9e0ee",
    "gray": "#6e6c7e",
    "black": "#1a1826",
}

mod = "mod4"
keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="toggle floating"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="toggle fullscreen"),
    # added above
    Key([mod], "e", lazy.spawn("nautilus"), desc="Launch nautilus"),
    Key([], "Print", lazy.spawn("flameshot screen -p /home/balde/Pictures")),
    Key([mod], "b", lazy.spawn("brave"), desc="Launch browser"),
    Key([mod], "d", lazy.spawn("discord"), desc="Launch discord"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 -q set Master 1dB-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -c 0 -q set Master toggle")),
    Key([], "Print", lazy.spawn("flameshot full -p Downloads/")),
    # Key([mod, "Print"], "Print", lazy.spawn("gnome-screenshot -i")),
    Key([mod], "Print", lazy.spawn("flameshot gui")),
    # Audio control
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),
    # Brithness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5%-")),
    Key([mod], "x", lazy.spawn("betterlockscreen -l blur")),
    #
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal #2"),
    Key([mod], "o", lazy.spawn(web_browser), desc="Launch the web browser."),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    # Lockscreen
    Key([mod], "l", lazy.spawn("betterlockscreen -l"), desc="Launch the lockscreen."),
    # Rofi Integration
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Launch an application."),
    # Reboot and suspend
    Key([mod, "control"], "s", lazy.spawn("systemctl suspend"), desc="Suspend"),
]

groups = [Group(i) for i in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]]
group_hotkeys = "123456789"

for g, k in zip(groups, group_hotkeys):
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                k,
                lazy.group[g.name].toscreen(),
                desc=f"Switch to group {g.name}",
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                k,
                lazy.window.togroup(g.name, switch_group=False),
                desc=f"Switch to & move focused window to group {g.name}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Bsp(
        margin=12,
        border_width=2,
        border_normal=catppuccin["black"],
        border_focus=catppuccin["mauve"],
    ),
    layout.Max(),
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font=default_font,
    fontsize=16,
    padding=2,
    forground=catppuccin["black"],
)
extension_defaults = widget_defaults.copy()


def get_widgets(primary=False):
    widgets = [
        widget.Spacer(
            length=bar_padding,
            background=catppuccin["black"],
        ),
        widget.TextBox(
            text=bar_left,
            padding=0,
            fontsize=20,
            foreground=catppuccin["mauve"],
            background=catppuccin["black"],
        ),
        widget.GroupBox(
            highlight_method="line",
            background=catppuccin["mauve"],
            highlight_color=[catppuccin["mauve"], catppuccin["mauve"]],
            inactive=catppuccin["black"],
        ),
        widget.TextBox(
            text=bar_right,
            padding=0,
            fontsize=30,
            foreground=catppuccin["mauve"],
            background=catppuccin["black"],
        ),
        widget.Spacer(length=part_padding, background=catppuccin["black"]),
        widget.Spacer(fontsize=15, foreground=catppuccin["white"]),
        widget.Spacer(
            length=part_padding,
            background=catppuccin["black"],
        ),
        widget.TextBox(
            text=bar_left,
            padding=0,
            fontsize=30,
            foreground=catppuccin["pink"],
            background=catppuccin["black"],
        ),
        widget.Volume(
            fmt="墳 {}",
            mute_command="amixer -D pulse set Master toggle",
            foreground=catppuccin["black"],
            background=catppuccin["sky"],
        ),
        widget.TextBox(
            text=bar_right,
            padding=0,
            fontsize=30,
            foreground=catppuccin["pink"],
            background=catppuccin["black"],
        ),
        widget.Spacer(
            length=bar_spacing,
            background=catppuccin["black"],
        ),
        widget.TextBox(
            text=bar_left,
            padding=0,
            fontsize=30,
            foreground=catppuccin["pink"],
            background=catppuccin["black"],
        ),
        widget.CPU(
            format=" {load_percent:04}%",
            foreground=catppuccin["black"],
            background=catppuccin["sky"],
        ),
        widget.TextBox(
            text=bar_right,
            padding=0,
            fontsize=30,
            foreground=catppuccin["pink"],
            background=catppuccin["black"],
        ),
        widget.Spacer(
            length=bar_spacing,
            background=catppuccin["black"],
        ),
        widget.TextBox(
            text=bar_left,
            padding=0,
            fontsize=30,
            foreground=catppuccin["pink"],
            background=catppuccin["black"],
        ),
        widget.Clock(
            format=" %a %I:%M %p",
            foreground=catppuccin["black"],
            background=catppuccin["sky"],
        ),
        widget.TextBox(
            text=bar_right,
            padding=0,
            fontsize=30,
            foreground=catppuccin["pink"],
            background=catppuccin["black"],
        ),
        widget.Spacer(
            length=bar_padding,
            background=catppuccin["black"],
        ),
        widget.TextBox(
            text=bar_left,
            padding=0,
            fontsize=30,
            foreground=catppuccin["pink"],
            background=catppuccin["black"],
        ),
        # Battery
        widget.Battery(
            foreground=catppuccin["black"],
            background=catppuccin["sky"],
            fontsize=15,
            battery=0,
            charge_char="  ",
            # charge_char="\uf584",
            update_interval=60,
            # discharge_char="\uf578",
            discharge_char="  ",
            font="Iosevka Nord Font",
            padding=5,
            # format="\uf584 {percent:2.0%}",
            format="   {percent:3.0%}",
            low_percentage=0.3,
        ),
        widget.Spacer(
            length=bar_padding,
            background=catppuccin["sky"],
        ),
        widget.TextBox(
            text=bar_right,
            padding=3,
            fontsize=20,
            foreground=catppuccin["pink"],
            background=catppuccin["black"],
        ),
    ]
    if primary:
        widgets.insert(6, widget.Systray())
    return widgets


screens = [
    Screen(
        top=bar.Bar(
            get_widgets(primary=True),
            22,
            background=catppuccin["black"],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "Qtile"


autostart = [
    "feh --bg-fill /home/balde/.config/qtile/wallpapers/gruvbox26.png",
    "picom --no-vsync &",
    "nm-applet &",
]

for x in autostart:
    os.system(x)
