from ipycanvas import Canvas, MultiCanvas

events = {'on_mouse_down': '_mouse_down_callbacks',
          'on_mouse_up':   '_mouse_up_callbacks',
          'on_mouse_move': '_mouse_move_callbacks',
          'on_mouse_out':  '_mouse_out_callbacks',
          'on_mouse_wheel':  '_mouse_wheel_callbacks',
          'on_key_down':   '_key_down_callbacks',
          }


def remove_callbacks(event_name, obj):
    '''remove all registered callbacks for the given event
       from a Canvas/MultiCanvas object
    '''
    assert event_name in events, f'unknown event {event_name}!'

    if isinstance(obj, Canvas):
        widget = obj
    elif isinstance(obj, MultiCanvas):
        widget = obj[-1]
    else:
        raise TypeError('obj must be an instance of Canvas of MultiCanvas')

    dispatcher_name = events[event_name]
    dispatcher = getattr(widget, dispatcher_name)
    method = getattr(widget, event_name)
    # use copy!
    for callback in dispatcher.callbacks[:]:
        method(callback, remove=True)


def remove_all_callbacks(obj):
    '''remove all registered callbacks from a Canvas/MultiCanvas object'''
    for event_name in events:
        remove_callbacks(event_name, obj)