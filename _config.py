from encodings import utf_8
import json
from pathlib import Path
import os, sys

_default = None

def getDefault():
    global _default
    return _default

def setDefault(defaultConfig):
    global _default
    _default = defaultConfig

def createDefaultFile(configFilePath=None):
    configFile = configFilePath
    if configFile is None:
        home = Path.home()
        vmiDir = home / '.vmi'
        configFile = vmiDir / 'config.json'
        if vmiDir.is_dir() is False:
            vmiDir.mkdir(parents=True, exist_ok=True)
    else:
        configFile = Path(configFilePath)
    defaultConfig = getDefault()
    configFile.write_text(json.dumps(defaultConfig, ensure_ascii=False, indent=4), encoding="utf8")
    return defaultConfig

def getConfiguration(configFilePath=None):
    configFile = configFilePath
    if configFile is None:
        home = Path.home()
        vmiDir = home / '.vmi'
        configFile = vmiDir / 'config.json'
        if vmiDir.is_dir() is False:
            vmiDir.mkdir(parents=True, exist_ok=True)
    else:
        configFile = Path(configFilePath)

    if configFile.is_file() is False:
        return createDefaultFile(configFilePath=configFilePath), vmiDir
    
    configuration = configFile.read_text(encoding='utf-8')
    try:
        configDict = json.loads(configuration)
    except Exception:
        configDict = createDefaultFile()
    finally:
        return configDict, vmiDir