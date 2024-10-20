from IPython.display import display
import canvashelpers
from .maze import Maze
from .maze_fields import fields
from .viewhelpers import Mob


field_idx = {field: i for i, field in enumerate(fields)}


def colors(col, row):
    if (col, row) == (5, 5):
        return 'red'
    elif (col, row) in fields:
        return 'green'
    else:
        return 'transparent'


class View:
    def __init__(self, maze):
        self.mob = Mob(buttons=('new game', 'undo', 'redo'))
        self.mob.buttons['new game'].on_click(lambda bt: maze.new_game())
        self.mob.buttons['undo'].on_click(lambda bt: maze.undo())
        self.mob.buttons['redo'].on_click(lambda bt: maze.redo())

        self.mcanvas = self.mob.mcanvas
        self.mcanvas.on_mouse_down(self.on_mouse_down)

        self.bg, self.fg = self.mcanvas
        self.fg.global_alpha = 0.5

        kwargs = {'pos': (20, 20), 'width': 150, 'ncols': 6, 'nrows': 8}
        canvashelpers.draw_chessboard(self.bg, colors=colors, **kwargs)
        info = canvashelpers.draw_grid(self.bg, **kwargs)
        self.xy2colrow = info['xy2colrow']
        self.colrow2xy = info['colrow2xy']
        self.dx, self.dy = info['dx'], info['dy']

        self.maze = maze
        f = self.mob.out.capture()(self.update)
        self.maze.register_callback(f)

    def on_mouse_down(self, x, y):
        col, row = self.xy2colrow(x, y)
        i = field_idx.get((col, row))
        steps = (self.maze.state + 1) % 3
        state = 3*i + steps
        self.maze.move(state)

    def show_options(self, opts):
        for opt in opts:
            col, row = fields[opt // 3]
            x, y = self.colrow2xy(col, row)
            fill_style = self.fg.fill_style
            self.fg.fill_style = 'yellow'
            self.fg.fill_rect(x, y, self.dx, self.dy)
            self.fg.fill_style = fill_style

    def draw_circle(self):
        col, row = fields[self.maze.state // 3]
        x, y = self.colrow2xy(col, row)
        self.fg.fill_circle(x+self.dx/2, y+self.dy/2, 5)

    def update(self, event, data):
        self.mob.out.clear_output()
        self.fg.clear()
        self.draw_circle()
        if not self.maze.is_game_over():
            opts = self.maze.get_opts()
            self.show_options(opts)

        if event == 'new_game':
            print('new game started')
        elif self.maze.is_game_over():
            print('Congrats! You did it!')

    def _ipython_display_(self):
        display(self.mob)


if __name__ == '__main__':
    maze = Maze()
    view = View(maze)
    display(view)
