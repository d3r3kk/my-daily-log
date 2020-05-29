import dataclasses
import logging
import pathlib


@dataclasses.dataclass
class MyDailyLogConfig:
    base_folder: pathlib.Path
    template: str
    day_offset: int
    verbosity: str
