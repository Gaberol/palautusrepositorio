class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        output = []
        for player in self.players:
            if player.nationality == nationality:
                output.append(player)

        return sorted(output, key=lambda player: player.goals + player.assists, reverse=True)