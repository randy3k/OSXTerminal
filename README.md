OpenHere
====

Mac only. Reveal current file at view or current folder at Finder, Terminal or iTerm. There are 
a lot of exisiting packages do the same thing, e.g. [Terminal][1], [Terminal In Packages][2] and [Open Finder][3].
The difference bewteen this package and the others is that OpenHere will peek into Terminal or iTerm to check
if there is a tab running on the intended to open directory. If such a tab is found, it would switch to that tab
instead of opening a new tab. However, uesr will need to make sure

1. using either bash or zsh
2. have the running program shown in the title of the application

![](https://user-images.githubusercontent.com/1690993/28229294-2638ba76-68b0-11e7-9264-56033b20f8d5.png)

## Usage

At the command palatte:

- Finder: Open Here
- Terminal: Open Here
- iTerm: Open Here

## Keybind

OpenHere does not ship with default keybinds. Instead, it lets you to define you own faviourite. 
Just define these keybinds in your user file.

```json
[
    { "keys": ["super+shift+t"], "command": "open_terminal_here"},
    { "keys": ["super+shift+i"], "command": "open_iterm_here"},
    { "keys": ["super+shift+f"], "command": "open_finder_here"}
]
```

[1]: https://packagecontrol.io/packages/Terminal
[2]: https://packagecontrol.io/packages/Terminal%20In%20Packages
[3]: https://packagecontrol.io/packages/Open%20Finder