from dataclasses import dataclass, field
from queue import Queue
from typing import List

shape = '''
    +------|
    |       
    |        
    |       
    |        
    |
 ===!==============
'''
man_index = [[25, 'O'], [37, '/'], [38, '|'], [39, '\\'], [52, '^'], [64, '/'], [66, '\\']]

def get_man_shape() -> Queue:
    q = Queue()
    [q.put(pair) for pair in man_index]
    return q

def get_shape_as_list() -> List[str]:
    return list(shape)

@dataclass
class Dashboard:
    _draw: List[str] = field(default_factory=get_shape_as_list, init=False)
    _man_shape: Queue = field(default_factory=get_man_shape, init=False)

    def get_rest_tries(self) -> int:
        return self._man_shape.qsize()
    
    def update_shape(self):
        index, char = self._man_shape.get()
        self._draw[index] = char
    
    def get_draw(self) -> str:
        # print(self._draw)
        return ''.join(self._draw)






