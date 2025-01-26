import widgets_helpers
import canvas_helpers
from IPython.display import display


class CanvasView:

    err_out = widgets_helpers.new_output()
    positions = [50, 150, 250]
    disk_widths = [30, 50, 70, 90]
    disk_height = 10
    colors = ['brown', 'teal', 'blue', 'purple']

    def __init__(self, game):
        self.game = game
        self.canvas = widgets_helpers.new_canvas()
        self.src = None

        self.game.event_handler = self.callback
        canvas_helpers.remove_all_callbacks(self.canvas)
        self.canvas.on_key_down(self.on_key_down)

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

    @err_out.capture()
    def on_key_down(self, key, *flags):
        # print(key)
        if key in '123' and self.src is None:
            self.src = int(key) - 1
            return
        elif key in '123':
            dst = int(key) - 1
            self.game.move_disk(self.src, dst)
        elif key == 'n':
            self.game.new_game()
        self.src = None

    def _ipython_display_(self):
        display(self.canvas, self.err_out)