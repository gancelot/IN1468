from .b import foo
print(foo)

from ..dir2 import c
print(c.foo)
from ..dir2.c import foo
print(foo)

from ...relative_mods.dir1.b import foo as foo2
print(foo2)
