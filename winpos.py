import win32gui

def move(self, pos, hwnd=None):
        """
        :param pos: A tuple describing the (X,Y,Width,Height) of the window OR
            A tuple describing the (X,Y) coordinates of the top right windows position
        :param hwnd: Move supplied window. If not supplied, then the default window is moved
        :return: The window handle
        """

        if hwnd is None:
            hwnd = self.get_hwnd()

        if len(pos) == 4:
            win32gui.MoveWindow(hwnd, pos[0], pos[1], pos[2], pos[3], 1)
        if len(pos) == 2:
            win_size = self.get_bbox_size()
            win32gui.MoveWindow(hwnd,pos[0],pos[1],win_size[0],win_size[1], 1)

move()
