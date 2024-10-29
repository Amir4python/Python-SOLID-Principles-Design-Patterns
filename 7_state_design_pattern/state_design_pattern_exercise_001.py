"""
Implement a simple media player that can play different types of media files, including music and video

The player should have a Player class that maintains the current state of the media player. The
player should be able to transition between the following states
1) StoppedState : the player is currently stopped
2) PlayingState The player is currently playing a media file
3) PausedState: the player is currently paused.
Implement  the plater class and three state classes using state design pattern

the Player Class should have methods for plating stopping and pausing the media
and it should delegate these operations to the appropriate state object based on the
current state of the player.


"""
from abc import ABC


class PlayerState(ABC):
    def __init__(self):
        pass

    def play(self,player):
        pass

    def stop(self,player):
        pass

    def pause(self,player):
        pass

class StoppedState(PlayerState):
    def play(self,player):
        player.playerState=PlayingState()

    def stop(self,player):
        print('Cannot Stop. Player is stopped')

    def pause(self,player):
        print('Cannot Pause. Player is stopped')

class PlayingState(PlayerState):
    def play(self, player):
        print('Already playing')

    def stop(self, player):
        player.playerState=StoppedState()
        print('YES!. Player has been stopped')

    def pause(self, player):
        player.playerState = PlayingState()
        print('YES!. Player has been continue from the pause')



class PausedState(PlayerState):
    def play(self, player):
        player.playerState = PlayingState()
        print('YES!. Player has been continue from the pause')

    def stop(self, player):
        player.playerState = StoppedState()
        print('YES!. Player has been stopped')

    def pause(self, player):
        print('Already paused')


class Player:
    def __init__(self):
        self.playerState=StoppedState()

    def play(self):
        self.playerState.play(self)

    def stop(self):
        self.playerState.stop(self)

    def pause(self):
        self.playerState.pause(self)

def main():
    player=Player()
    player.play()
    player.pause()
    player.stop()

if __name__ == '__main__':
    main()