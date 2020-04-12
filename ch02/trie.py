from typing import Optional

from attr import attrs, attrib


@attrs(slots=False)
class Node:
    _value: Optional[str] = attrib()
    _children: dict = attrib(factory=dict, init=False)

    def _add_child(self, char, value, overwrite=False):
        pass


@attrs(slots=False)
class Trie(Node):
    _value: Optional[str] = attrib(default=None)

    def __contains__(self, key):
        return self[key] is not None
