#import sys
import colorama
import textwrap

from .errors import (
    ScreenExistsError, 
    InvalidCharError,
    InvalidDimensionError
)
from .chars import Chars
from .std import Stdout
from .readchar import readkey
from .sprite import Sprite

class Screen:
    _created = False
    
    def __init__(self, 
            size, 
            text_center=False,
            title=None, 
            description=None
            ) -> None:
        if Screen._created:
            raise ScreenExistsError(
                "A Screen has already been initialized, "
                "only one can be initialized at a time."
            )
        
        if title is None:
            title = 'Blessings Window'
        self.text_center = text_center
        self._title = title

        self.size = size
        
        if description is None:
            description = ''
        self.description = description

        colorama.init()
        self._stdout = Stdout()

        #self.refresh()
        Screen._created = True

    @property
    def title(self):
        return self._title if not self.text_center else self._title.center(self.size[0])
    
    def _clear(self) -> None:
        self._stdout.clear()
    
    def _write(self, content) -> None:
        self._stdout.write(content)

    def _read(self) -> str:
        return self._stdout.read()
    
    @property
    def body(self):
        pixels = {
            y:{
                x:None for x in range(self.size[0])
            } for y in range(self.size[1])
        }
        
        for sprite in self.sprites:
            for y in sprite._char_map:
                for x in sprite._char_map[y]:
                    if pixels[y][x] is None:
                        pixels[y][x] = sprite._char_map[y][x]
        
        return '\n'.join([
            ''.join([
                str(pixel) if pixel is not None else ' ' for pixel in line.values()
            ]) for line in pixels.values()
        ])

    @property
    def screen_text(self):
        top = Chars.U_L_CORNER + Chars.H_LINE * self.size[0] + Chars.U_R_CORNER
        middle = [Chars.V_LINE + line + Chars.V_LINE for line in self.body.splitlines()]
        bottom = Chars.D_L_CORNER + Chars.H_LINE * self.size[0] + Chars.D_R_CORNER
        return '\n'.join([
            *([self.title, self.description] if self.description != '' else [self.title]), 
            *[top, *middle, bottom]
        ]) + '\n'

    def refresh(self):
        self._clear()
        self._write(self.screen_text)
    
    @property
    def sprites(self):
        return [sprite for sprite in Sprite._all if not sprite.hidden]
    
    def get_sprite(self, id):
        try:
            return {s.id:s for s in Sprite._all}[id]
        except KeyError:
            return None

