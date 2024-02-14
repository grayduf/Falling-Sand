class Setting:
    width = 800
    height = 450
    size = (width, height)
    fps = 30
    window = None

    cell_size = 5
    cols = height//cell_size
    rows = width//cell_size
    offset = 0

    Colors  = [(0, 0, 0), (161, 0, 219)]
    black = (0, 0, 0)
    white = (255, 255, 255)