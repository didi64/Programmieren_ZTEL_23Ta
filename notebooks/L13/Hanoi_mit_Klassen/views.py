import widgets_helpers
from ipycanvas import Canvas
from IPython.display import display


class DebugView:
    out = widgets_helpers.new_output()

    def __init__(self, game):
        game.event_handler = self.callback

    @out.capture()
    def callback(self, event, data):
        print(event, data)

    def _ipython_display_(self):
        display(self.out)


class CanvasView:
    positions = [50, 150, 250]
    disk_widths = [30, 50, 70, 90]
    disk_height = 10
    colors = ['brown', 'teal', 'blue', 'purple']

    def __init__(self, game):
        self.game = game
        self.canvas = widgets_helpers.new_canvas()
        self.game.event_handler = self.callback

    def draw_stack(self, stack, pos):
        h = self.disk_height
        for i, disk in enumerate(stack):
            self.canvas.fill_style = self.colors[disk]
            w = self.disk_widths[disk]
            self.canvas.fill_rect(pos - w/2,
                                  self.canvas.height-(i+1)*h,
                                  w,
                                  h)

    def draw_stacks(self, stacks):
        self.canvas.clear()
        for pos, stack in zip(self.positions, stacks):
            self.draw_stack(stack, pos)

    def callback(self, event, data):
        self.draw_stacks(data)

    def _ipython_display_(self):
        display(self.canvas)


class TextView:
    def __init__(self, game, debug=True):
        self.game = game
        self.out = widgets_helpers.new_output()
        self.game.event_handler = self.callback

    def print_stacks(self, event, stacks):
        self.out.clear_output()
        with self.out:
            lines = []
            for h in range(self.game.ndisks):
                line = ''.join(' '*7 if len(stack) <= h else f'{'*' * (2*stack[h]+1):^7}'
                               for stack in stacks)
                lines.append(line)
            print('\n'.join(lines[::-1]))

    def callback(self, event, data):
        self.print_stacks(event, data)

    def _ipython_display_(self):
        display(self.out)