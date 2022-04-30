import pathlib
p1 = pathlib.Path('x/y/z.foo.py').name

import pathlib as pl
p2 = pl.Path('x/y/z.foo.py').parent

from pathlib import Path
p3 = Path().cwd() / Path('x/y/z.foo.py')
p4 = Path('x/y/z.foo.py').absolute()
p5 = Path('/x/y/z.foo.py').resolve()

from pathlib import Path as P
p6 = P('/x/y/z.foo.py').suffixes

print(p1, p2, p3, p4, p5, p6, sep='\n')