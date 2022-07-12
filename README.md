# Erstjahresprojekt

Erstjahresprojekt: Reinforcement Learning in virtuellen Umgebungen

ANLEITUNG:

WICHTIG:
Vor dem ersten Anlauf muss neben den Libraries auch das custom Gym-environment installiert werden. Dazu im Terminal in den Unterordner "mairio/Code/gym-mairio" navigieren und per "pip install -e ." installieren.

Gym muss auf Version 0.24.0 sein!

Aktuell nur unter Windows!

1. Im Ordner "bizhawk-2-8" das Programm "Emuhawk.exe" starten (gegebenenfalls noch die prerequisites installieren: https://github.com/TASEmulators/BizHawk-                   Prereqs/releases) 

2. Unter der Reiter "File" mit der Option "open Rom" die Rom Laden. Sie befindet sich im Unterordner "Mairio/Gamefiles"

3. Unter dem Reiter "Tools" die Lua-Konsole öffnen

4. Skript öffnen im Ordner "Code/Data/helper_functions_lua.lua"

5. Wenn Lua jetzt keine Rückmeldung gibt ist alles richtig. Jetzt Python Datei "Code/main.py" ausführen

Optional:
In config.py die Parameter anpassen, oder im Lua Skript "Code/Data/helper_functions_lua.lua" in Zeile 478 die Variable "current_level" ändern, um ein anderes Startlevel zu wählen

Wichtig: Wird das Lua-Skript eigenständig ausgeführt oder das Python-skript fertig durchgelaufen kann der Emulator abstürzen. Am besten einfach main.py neu ausführen, ohne den Emulator anzufassen
