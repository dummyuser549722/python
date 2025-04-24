# test_television.py

import pytest
from television import Television

def test_init():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power_toggle():
    tv = Television()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_mute_behavior():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.power()
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 1"

def test_channel_up_behavior():
    tv = Television()
    tv.channel_up()  # Should do nothing
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()  # Should loop back to 0
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_channel_down_behavior():
    tv = Television()
    tv.channel_down()  # Should do nothing
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    tv.channel_down()  # Should wrap to 3
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"

def test_volume_up_behavior():
    tv = Television()
    tv.volume_up()  # Should do nothing
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.mute()
    tv.volume_up()  # Should unmute and increase volume
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"
    tv.volume_up()  # Should stay at max
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

def test_volume_down_behavior():
    tv = Television()
    tv.volume_down()  # Should do nothing
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    tv.volume_up()
    tv.volume_up()  # Volume = 2
    tv.mute()
    tv.volume_down()  # Should unmute and decrease
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.volume_down()
    tv.volume_down()  # Should stay at min
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

