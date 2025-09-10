from dataclasses import dataclass

@dataclass
class AppConfig:

    name: str
    url: str
    # icon: str

app_configs = [
    AppConfig(
        name="Einkaufsliste",
        url="/groceries"
        # icon=
    ),
    AppConfig(
        name="Shopping",
        url="/" # TODO
        # icon=
    ),
    AppConfig(
        name="ToDo",
        url="/" # TODO
        # icon=
    ),        
]