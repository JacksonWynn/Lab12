class Television:
    '''
    Class to represent the Television objects.
    '''
    MIN_CHANNEL: int = 0     # Minimum TV channel
    MAX_CHANNEL: int = 3     # Maximum TV channel

    MIN_VOLUME: int = 0      # Minimum TV volume
    MAX_VOLUME: int = 2      # Maximum TV volume

    def __init__(self) -> None:
        '''
        Initializer method creates new Television object and initializes channel to 0, volume to 0, and isOn to False.
        '''
        self.__channel: int = 0
        self.__volume: int = 0
        self.__isOn: bool = False

    def power(self) -> None:
        '''
        Switches isOn value of called Television object to False if it is currently True, otherwise, switches it to True.
        '''
        if not self.__isOn:
            self.__isOn = True
        else:
            self.__isOn = False

    def channel_up(self) -> None:
        '''
        Checks if called Television object is on. If not, does nothing; otherwise, increments channel by 1 if it is less than 3 and sets it to 0 otherwise.
        '''
        if self.__isOn:
            if self.__channel < 3:
                self.__channel += 1
            else:
                self.__channel = 0

    def channel_down(self) -> None:
        '''
        Checks if called Television object is on. If not, does nothing; otherwise, decrements channel by 1 if it is greater than 0 and sets it to 3 otherwise.
        '''
        if self.__isOn:
            if self.__channel > 0:
                self.__channel -= 1
            else:
                self.__channel = 3
        pass

    def volume_up(self) -> None:
        '''
        Checks if called Television object is on. If not, does nothing; otherwise, increments volume by 1 if it is less than 2.
        '''
        if self.__isOn:
            if self.__volume < 2:
                self.__volume += 1

    def volume_down(self) -> None:
        '''
        Checks if called Television object is on. If not, does nothing; otherwise, decrements volume by 1 if it is greater than 0.
        '''
        if self.__isOn:
            if self.__volume > 0:
                self.__volume -= 1

    def __str__(self) -> str:
        '''
        If a Television object is referenced as a string, that string is a description of the values of the object.
        '''
        return(f"TV status: Is on = {self.__isOn}, Channel = {self.__channel}, Volume = {self.__volume}")
        pass
