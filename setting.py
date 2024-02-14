class Setting:
    width = 800
    height = 800
    size = (width, height)
    fps = 60
    window = None

    cell_size = 20
    cols = height//cell_size
    rows = width//cell_size
    offset = 0

    Colors  = [(0, 0, 0), (255, 192, 0)]
    black = (0, 0, 0)
    white = (255, 255, 255)