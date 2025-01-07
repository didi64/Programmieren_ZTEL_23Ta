from ipycanvas import Canvas
from IPython.display import display


class View:
    canvas_config = {
        'width': 300,
        'height': 100,
        'layout': {'border': '1px solid black'},
    }

    positions = [50, 150, 250]
    disk_widths = [30, 50, 70, 90]
    disk_height = 10
    stack_width = 100
    colors = ['brown', 'teal', 'blue', 'purple']

    def __init__(self):
        self.canvas = Canvas(**View.canvas_config)

    def draw_stack(self, stack, x):
        h = self.disk_height
        for i, disk in enumerate(stack):
            self.canvas.fill_style = self.colors[disk]
            w = self.disk_widths[disk]
            self.canvas.fill_rect(x - w/2,
                                  self.canvas.height-(i+1)*h,
                                  w,
                                  h)

    def draw_stacks(self, stacks):
        self.canvas.clear()
        for x, stack in zip(self.positions, stacks):
            self.draw_stack(stack, x)

    def _ipython_display_(self):
        display(self.canvas)
