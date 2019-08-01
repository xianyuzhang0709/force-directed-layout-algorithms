import numpy as np


class Node:
    __slots__ = ['datapoint', 'x', 'y', 'vx', 'vy']
    # 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。

    def __init__(self,
                 datapoint: np.ndarray,
                 x: float=0.0,
                 y: float=0.0,
                 vx: float=0.0,
                 vy: float=0.0) -> None:
        self.datapoint = datapoint
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def add_velocity(self, vx: float, vy: float) -> None:
        self.vx += vx
        self.vy += vy

    def apply_velocity(self) -> None:
        self.x += self.vx
        self.y += self.vy
        self.clear_velocity()

    def clear_velocity(self) -> None:
        self.vx = 0.0
        self.vy = 0.0

    def __str__(self) -> str:
        return f'Node<{self.datapoint}>({self.x} + {self.vx}, {self.y} + {self.vy})'

    def __repr__(self) -> str:
        return f'Node<{self.datapoint}>'
