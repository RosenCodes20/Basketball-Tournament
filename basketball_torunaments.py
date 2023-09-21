name_of_the_tournament = input()

result=""
win=0
lose=0
win_per=0
lose_per=0
while name_of_the_tournament != "End of tournaments":
    maches = int(input())
    for games in range(1,maches+1):
        points_made_by_desi_team = int(input())
        points_made_by_the_other_team = int(input())
        diff=abs(points_made_by_the_other_team-points_made_by_desi_team)
        if points_made_by_desi_team > points_made_by_the_other_team:
            win+=1
            result="win"

        elif points_made_by_the_other_team > points_made_by_desi_team:
            lose+=1
            result="lost"
        print(f"Game {games} of tournament {name_of_the_tournament}: {result} with {diff} points.")
    name_of_the_tournament = input()
win_per=win/(win+lose)*100
lose_per=lose/(win+lose)*100
print(f"{win_per:.2f}% matches win")
print(f"{lose_per:.2f}% matches lost")
