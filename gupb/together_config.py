from gupb.controller import random
from gupb.scripts import arena_generator
from gupb.controller import pat_i_kot

from gupb.controller import aragorn


CONFIGURATION = {
    'arenas': [
        'ordinary_chaos',
    ],
    'controllers': [
        random.RandomController("Alice"),
        random.RandomController("Bob"),
        random.RandomController("Cecilia"),
        aragorn.AragornController("Aragorn"),
        pat_i_kot.PatIKotController("Kot i Pat")
    ],
    'start_balancing': False,
    'visualise': True,
    'show_sight': None,
    'runs_no': 1,
}
