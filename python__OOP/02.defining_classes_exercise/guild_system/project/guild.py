from guild_system.project.player import Player


class Guild:
    players = []

    def __init__(self, name: str):
        self.name = name

    def assign_player(self, player: Player):
        # search_player = [p for p in self.players if p.name == player][0]
        self.players.append(player)
        if self.name == Player.guild:
            return f'Player {player.name} is already in the guild.'

        Player.guild = self.name
        return f'Player {player.name} is in another guild.'





    def kick_player(self, player_name) -> str:
        pass

    def guild_info(self):
        pass


"""
Добавете играча в гилдия. Връщане на 
"Приветствен играч {player_name} в гилдия {guild_name}". 
Не забравяйте да промените гилдията на играча в класа на играчите. 

Ако играчът вече е в гилдия, върнете се в "Играч {player_name} вече 
е в гилдия." Ако играчът е в друга гилдия, върнете се в "Media Player 
{player_name} е в друга гилдия."
"""
player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
