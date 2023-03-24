import minqlx

class overload(minqlx.Plugin):
    def __init__(self):
        super().__init__()

        self.add_hook("map", self.handle_map_change)

    def handle_map_change(self, mapname: str, factory: str) -> None:
        @minqlx.delay(8)
        def map_restart():
            minqlx.console_command("map_restart")
            
        if factory not in ["ol", "olad", "olca", "olctf"]:
            return

        minqlx.set_cvar("g_gametype", "7", -1)
        map_restart()