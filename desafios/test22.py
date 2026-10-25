from rich.progress import track
from rich.progress import Progress
from rich import print
from rich import inspect
from time import sleep
from rich.bar import Bar
from rich import print_json


def progresso(number):
    with Progress() as progress:
        volume = progress.add_task('volume', True)
        progress.update(volume, advance=number)







