def draw_chessboard(canvas, bg='grey', fg='blue'):
    n = 8  
    canvas.fill_style = bg
    canvas.fill_rect(0, 0, canvas.width, canvas.height)

    # Zeichne (ungerade) Felder mit color2
    canvas.fill_style = fg

    # width und height eines Feldes
    dw = canvas.width / n
    dh = canvas.height / n

    for x in range(n):
        for y in range(n):
            # zeichen Feld falls x + y ungerade
            if (x + y) % 2 == 1:
                canvas.fill_rect(x*dw, y*dh, dw, dh)


def draw_circle(canvas, x, y, color='black'):
    n = 8
    canvas.fill_style = color
    dw = canvas.width / n
    dh = canvas.height / n

    col = x // dw
    row = y // dh

    center = ((col+0.5)*dw, (row+0.5)*dh)
    canvas.fill_circle(*center, min(dw, dh)/3)