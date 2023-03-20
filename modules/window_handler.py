import win32gui, win32con

Gwindow = None


def get_by_name(target_name):
    print(f'finding: {target_name}')
    return win32gui.FindWindow(None, target_name)
    
def set_target_name(target_name):
    global Gwindow
    Gwindow = get_by_name(target_name)

def get_or_default(target_name=None):
    if target_name is None:
        global Gwindow
        window = Gwindow
    else:
        window = get_by_name(target_name)
    
    return window

def focus(target_name=None):
    window = get_or_default(target_name)
    if win32gui.IsIconic(window):
        win32gui.ShowWindow(window, 1)
    
    win32gui.SetForegroundWindow(window)
    
    print('focused')
    return window

def still_focused():
    return (win32gui.GetForegroundWindow() == Gwindow)

def maximize(target_name=None):
    
    window = focus(target_name)
    win32gui.ShowWindow(window, win32con.SW_MAXIMIZE)
    
    print('maximized')
    return window

def minimize(target_name=None):
    window = focus(target_name)
    win32gui.ShowWindow(window, win32con.SW_MINIMIZE)
    
    print('minimized')
    return window

def get_area(target_name=None):
    window = get_or_default(target_name)
    cood = win32gui.GetWindowRect(window)
    cli = win32gui.GetClientRect(window)
    
    #print(cood)
    #print(cli)
    
    margin = ( (cood[2] - cood[0]) - (cli[2] - cli[0]) ) / 2
    
    pos_topleft_x = cood[2] - cli[2] - margin
    pos_topleft_y = cood[3] - cli[3] - margin
    size_x = cli[2] - cli[0]
    size_y = cli[3] - cli[1]
    
    return (pos_topleft_x, pos_topleft_y, size_x, size_y)

def get_area_dict(target_name=None):
    cood = get_area(target_name)
    position = {'x': cood[0], 'y': cood[1]}
    size = {'width': cood[2], 'height': cood[3]}
    
    return {'position': position, 'size': size}

def get_position(target_name=None):
    dict = get_area_dict(target_name)
    return dict['position']

def get_size(target_name=None):
    dict = get_area_dict(target_name)
    return dict['size']

def set_size(target_name=None, position={'x':0,'y':0}, size={'width':1280, 'height':720}):
    window = focus(target_name)
    win32gui.MoveWindow(window, position['x'], position['y'], size['width'], size['height'], True)
    area = get_size(target_name)
    win32gui.MoveWindow(window, position['x'], position['y'], size['width'] * 2 - area['width'], size['height'] * 2 - area['height'], True)
    
    print(f'size set: {size}')
    return window