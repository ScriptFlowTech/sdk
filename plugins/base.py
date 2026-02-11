class Plugin:
    name = "base"

    def run(self, *args, **kwargs):
        raise NotImplementedError
