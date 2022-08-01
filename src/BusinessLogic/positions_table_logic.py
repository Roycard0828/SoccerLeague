from ..DataAccess.models import Match
from .positions_table_controller import PositionsTableController
from .match_controller import MatchController


def update_data_table_team(match: Match):
    """ Generate information based on the result of a match"""
    local_team = match.local_team
    visiting_team = match.visiting_team
    result = str(match.result)
    # Validate if a result was assigned to the match
    if result != "Empty":
        goals = result.split(sep='-')
        local_team_goals = goals[0]
        visiting_team_goals = goals[1]
    else:
        local_team_goals = 0
        visiting_team_goals = 0

    # Make dictionaries to organize the information
    data_local_team = {'team_id': local_team.id,
                       'match_won': 0,
                       'match_lost': 0,
                       'tie_match': 0,
                       'goals': int(local_team_goals),
                       'points': 0}
    data_visiting_team = {'team_id': visiting_team.id,
                          'match_won': 0,
                          'match_lost': 0,
                          'tie_match': 0,
                          'goals': int(visiting_team_goals),
                          'points': 0}

    if local_team_goals > visiting_team_goals:
        data_local_team['match_won'] = 1
        data_local_team['points'] = 3

        data_visiting_team['match_lost'] = 1
    elif local_team_goals < visiting_team_goals:
        data_visiting_team['match_won'] = 1
        data_visiting_team['points'] = 3

        data_local_team['match_lost'] = 1
    else:
        data_local_team['points'] = 1
        data_local_team['tie_match'] = 1

        data_visiting_team['points'] = 1
        data_visiting_team['tie_match'] = 1

    PositionsTableController.update_team_points(data_local_team, data_visiting_team)


def end_soccer_day(soccer_day: int):
    """Update all the teams from a specific soccer day number"""
    matches = MatchController.get_all_matches_by_day_number(soccer_day)
    for match in matches:
        update_data_table_team(match)


def start_season():
    PositionsTableController.register_all_teams()
