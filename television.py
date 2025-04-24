# television.py

class Television:
    # Class constants
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """Initializes the Television object with default settings."""
        self.__status = False  # TV is off
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """Toggles the power status of the TV."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Toggles the mute status of the TV, only if the TV is on."""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Increases the channel by 1, loops to MIN_CHANNEL if at MAX_CHANNEL."""
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """Decreases the channel by 1, loops to MAX_CHANNEL if at MIN_CHANNEL."""
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """Increases volume by 1 unless at MAX_VOLUME. Unmutes if muted."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decreases volume by 1 unless at MIN_VOLUME. Unmutes if muted."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Returns a string showing the current state of the TV."""
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"

