from project.player import Player
class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} to the guild {self.name}"
        if player != Player.NO_GUILD:
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"
    
    def kick_player(self, player_name):
        player = next((p for p in self.players if p.name == player_name), None)
        if player:
            self.players.remove(player_name)
            player.guild = self.name
            return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."
    
    def guild_info(self):
        information = [f"Guild: {self.name}"]
        for player in self.players:
            information.append(player.player_info())
        return "\n".join(information)
    