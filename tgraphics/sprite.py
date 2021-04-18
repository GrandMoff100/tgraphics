from .errors import InvalidDimensionError

class Sprite:
    _temp = 0
    _all = []

    def __init__(self, pos, text, color=None):
        char_array = [
            list(line)
            for line in text.splitlines()
        ]
        self._char_map = {
            y + pos[1]:{
                x + pos[0]:char_array[y][x] for x in range(len(char_array[y]))
            } for y in range(len(char_array))
        }
        
        self.id = Sprite._temp
        Sprite._temp += 1
        Sprite._all.append(self)
        self.hidden = False

    @property
    def size(self):
        return len(self._char_map), len(list(self._char_map.values())[0])

    def move_left(self):
        self._char_map = {
            y:{
                x - 1:self._char_map[y][x] for x in self._char_map[y]
            } for y in self._char_map
        }

        self.check_is_valid()

    def move_right(self):
        self._char_map = {
            y: {
                x + 1:self._char_map[y][x] for x in self._char_map[y]
            } for y in self._char_map
        }

        self.check_is_valid()

    def move_up(self):
        self._char_map = {
            y - 1:{
                x:self._char_map[y][x] for x in self._char_map[y]
            } for y in self._char_map
        }

        self.check_is_valid()
    
    def move_down(self):
        self._char_map = {
            y + 1:{
                x:self._char_map[y][x] for x in self._char_map[y]
            } for y in self._char_map
        }

        self.check_is_valid()
    
    def check_is_valid(self):
        is_valid = True
        if not is_valid:
            raise InvalidDimensionError("You cannot move outside the border.")
    
    def hide(self):
        self.hidden = True
    
    def unhide(self):
        self.hidden = False

    def bring_forward(self):
        sprites = [s for s in Sprite._all]
        id = sprites.index(self)
        if sprites[id] != sprites[0]:
            sprites[id] = sprites[id - 1]
            sprites[id - 1] = self
            Sprite._all = [s for s in sprites]

    def bring_backward(self):
        sprites = [s for s in Sprite._all]
        id = sprites.index(self)
        if sprites[id] != sprites[-1]:
            sprites[id] = sprites[id + 1]
            sprites[id + 1] = self
            Sprite._all = [s for s in sprites]
    
    def bring_to_front(self):
        sprites = [s for s in Sprite._all]
        id = sprites.index(self)
        if sprites[id] != sprites[0]:
            sprites.pop(id)
            sprites.insert(0, self)   
            Sprite._all = [s for s in sprites]
    
    def bring_to_back(self):
        sprites = [s for s in Sprite._all]
        id = sprites.index(self)
        if sprites[id] != sprites[0]:
            sprites.pop(id)
            sprites.insert(len(sprites), self)
            Sprite._all = [s for s in sprites]

    def delete(self):
        Sprite._all.pop(Sprite._all.index(self))
        del self
