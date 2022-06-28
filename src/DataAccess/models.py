from unicodedata import name
from .db import session, base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Team(base):
    __tablename__ = "team"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    manager = Column(String)
    field = Column(String)

    def __init__(self, name, manager, field):
        self.name = name
        self.manager = manager
        self.field = field


class Match(base):
    __tablename__ = "match"
    id = Column(Integer, primary_key=True)
    day_number = Column(Integer)
    local_team_id = Column(Integer, ForeignKey('team.id'))
    visting_team_id = Column(Integer, ForeignKey('team.id'))
    field = Column(String)
    result = Column(String, default="Empty")
    # Relationships
    local_team = relationship('Team', foreign_keys=[local_team_id])
    visiting_team = relationship('Team', foreign_keys=[visting_team_id])

    def __init__(self, day_number, local_team_id: int, visiting_team_id: int, field):
        self.day_number = day_number
        self.local_team_id = local_team_id
        self.visting_team_id = visiting_team_id
        self.field = field


class PositionsTable(base):
    __tablename__ = "positions_table"
    id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey('team.id'))
    matches_played = Column(Integer, default=0)
    matches_won = Column(Integer, default=0)
    matches_lost = Column(Integer, default=0)
    tied_matches = Column(Integer, default=0)
    goals = Column(Integer, default=0)
    points = Column(Integer, default=0)
    # Relationships
    team = relationship('Team')

    def __init__(self, team: Team):
        self.team = team