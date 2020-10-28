from project.player import Player


class Guild:
    def __init__(self, name: str, list_of_players=None):
        if list_of_players is None:
            list_of_players = []
        self.name = name
        self.list_of_players = list_of_players

    def assign_player(self, player: Player):
        if player in self.list_of_players:
            return f'Player {player.name} is already in the guild.'
        if not player.guild == 'Unaffiliated':
            return f'Player {player.name} is in another guild.'
        self.list_of_players.append(player)
        player.guild = self.name
        return f'Welcome player {player.name} to the guild {player.guild}'

    def kick_player(self, player_name: str):
        if player_name in [p.name for p in self.list_of_players]:
            player = [p for p in self.list_of_players if p.name == player_name][0]
            self.list_of_players.remove(player)
            return f'Player {player_name} has been removed from the guild.'
        return f'Player {player_name} is not in the guild.'

    def guild_info(self):
        result = f'Guild: {self.name}\n'
        for p in self.list_of_players:
            result += p.player_info() + '\n'
        return result
