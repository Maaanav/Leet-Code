class Solution:
    def rankTeams(self, votes: List[str]) -> str:

        num_pos = len(votes[0])
        team_votes = {team: [0] * num_pos for team in votes[0]}

        for vote in votes:
            for pos, team in enumerate(vote):
                team_votes[team][pos] += 1
        
        sorted_teams = sorted(
            votes[0],
            key = lambda team: ([ -count for count in team_votes[team] ], team)
        )

        return "".join(sorted_teams)        
