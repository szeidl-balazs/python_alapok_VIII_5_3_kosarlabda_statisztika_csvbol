import game_statistic

def print_player_stat_in_quarter(name, quarter, player_scores, score_type, score_type_count):

    print(name + ' statisztikája a(z) ' + str(quarter) + '. negyedben:')
    if player_scores != 0:
        print('Elért pontok: ' + str(player_scores))
        print(str(score_type) + ' pontos dobások száma: ' + str(score_type_count))
    else:
        print('Nem ért el pontot a negyedben.')
    

print_player_stat_in_quarter(game_statistic.player_name, game_statistic.quarter, game_statistic.player_scores, game_statistic.score_type, game_statistic.score_type_count)