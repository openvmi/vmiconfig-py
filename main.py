if __name__ == "__main__":
    import _config
    _config.setDefault({"name": "vmilabs", "version": "2.0"})
    print(_config.getDefault())
    configuration,vmidir = _config.getConfiguration("./config.json")
    print(configuration)
    print(vmidir)