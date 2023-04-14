"""Algorithm to generate the calendar of matches according
    to the registered teams"""

from .team_controller import TeamController
from .match_controller import MatchController
from ..DataAccess.models import Match, Team


def create_calendar():
    team_list = TeamController.get_all_teams()

    list_one = []
    list_two = []
    total_number_teams = len(team_list)
    soccer_days = 0

    # The soccer_days number is (n-1) to a even number of matches
    if total_number_teams % 2 == 0:
        half = int(total_number_teams/2)
        list_one = team_list[0:half]
        list_two = team_list[half:total_number_teams]
        list_two = list(list_two + [0])
        soccer_days = total_number_teams - 1
        soccer_day_counter = 0

        for i in range(0, soccer_days):
            # Make a series of matches of a one soccer day
            for j in range(0, half):
                local_team: Team
                visiting_team: Team
                if soccer_day_counter % 2 == 0:
                    local_team = list_one[j]
                    visiting_team = list_two[j]
                else:
                    local_team = list_two[j]
                    visiting_team = list_one[j]

                MatchController.add_match(soccer_day_counter, local_team, visiting_team, local_team.field)

            # Rotate teams
            list_two[-1] = list_one[-1]
            for a in range(half - 2, 0, -1):
                list_one[a+1] = list_one[a]

            list_one[0] = list_two[0]

            for b in range(half):
                list_two[b] = list_two[b+1]

            soccer_day_counter += 1
    else:
        half = int((total_number_teams-1)/2)
        list_one = team_list[0:half+1]
        list_two = team_list[half+1:total_number_teams]
        break_team = None
        soccer_days = total_number_teams
        soccer_day_counter = 1

        for i in range(soccer_days):
            break_team = list_one[-1]
            for j in range(0, half):
                local_team: Team
                visiting_team: Team

                if soccer_day_counter % 2 == 0:
                    local_team = list_one[j]
                    visiting_team = list_two[j]
                else:
                    local_team = list_two[j]
                    visiting_team = list_one[j]

                MatchController.add_match(soccer_day_counter, local_team, visiting_team, local_team.field)

            # Rotate teams
            for a in range(len(list_one)-2, -1, -1):
                list_one[a+1] = list_one[a]

            list_one[0] = list_two[0]

            for b in range(0, len(list_two) - 1):
                list_two[b] = list_two[b+1]

            list_two[-1] = break_team # Get out the team of its break

            soccer_day_counter += 1
