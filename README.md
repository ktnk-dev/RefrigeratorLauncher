<img src="https://cdn.discordapp.com/attachments/766382334067867668/1081007718904643604/frige.png" height=250 width=200>

# RefrigeratorLauncher
- This launcher can run Cultivation or _that anime game_, moving or removing `version.dll` file automatically 
- You must put paths to Cultivation or _that anime game_, to game files and version.dll

# Editing `config.cfg`
**Config file must be in the same folder with app** (`.exe` or `.pyw`)
- `original_launcher` — Path to original launcher (not game launcher)
- `cultivation_launcher` — Path to Cultivation launcher
- `game_path` — Path to game folder
- `version_dll_path` — Path to version.dll (by default should be in the same folder with app)

# `config.cfg` example 
```ini
original_launcher=C:\Genshin Impact\launcher.exe
cultivation_launcher=C:\Program Files\Cultivation\Cultivation.exe
game_path=C:\Genshin Impact\Genshin Impact game
version_dll_path=version.dll
```
