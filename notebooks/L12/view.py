from ipycanvas import Canvas


def draw_stack(stack, pos):
    h = disk_height
    for i, disk in enumerate(stack):
        canvas.fill_style = colors[disk]
        w = disk_widths[disk]
        canvas.fill_rect(pos - w/2, canvas.height-(i+1)*h, w, h)


def draw_stacks(stacks):
    canvas.clear()
    for pos, stack in zip(stack_positions, stacks):
        draw_stack(stack, pos)


canvas_config = {
    'width': 300,
    'height': 100,
    'layout': {'border': '1px solid black'},
}

stack_positions = [50, 150, 250]
disk_widths = [30, 50, 70, 90]
disk_height = 10
colors = ['brown', 'teal', 'blue', 'purple']

canvas = Canvas(**canvas_config)