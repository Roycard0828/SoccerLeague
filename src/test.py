from DataAccess.team_dao import TeamDao
from DataAccess.models import Team
from DataAccess import db


def run():
    team1 = Team('RealMadrid', 'Carletto', 'Bernabeu')
    dao = TeamDao()
    dao.save(team1)


if __name__ == '__main__':
    db.base.metadata.create_all(db.connection)
    run()
