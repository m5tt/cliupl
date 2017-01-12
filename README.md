# Description
cliupl is a simple plugin style command line image uploader. cliupl will upload to any site given there is a plugin for it.

Plugins can also implement there own command line interface. cliupl will simply parse all known options and then pass any unknowns to the chosen plugin.

# Examples
Upload to tiikoni


`cliupl --img-file ~/image.png --site tiikoni`

Upload to imgur


`cliupl --img-file ~/image.png --site imgur`
