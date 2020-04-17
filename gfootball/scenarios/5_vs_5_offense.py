from . import *

def build_scenario(builder):
  builder.config().game_duration = 1000
  builder.config().end_episode_on_score = True
  builder.config().end_episode_on_out_of_play = True
  builder.config().end_episode_on_possession_change = True
  builder.config().right_team_difficulty = 0.05
  builder.config().left_team_difficulty = 0.05  
  builder.config().deterministic = False
  first_team = Team.e_Left
  second_team = Team.e_Right
  builder.SetTeam(first_team)
  builder.AddPlayer(-1.000000, 0.000000, e_PlayerRole_GK, controllable=False)
  builder.AddPlayer(0.000000,  0.020000, e_PlayerRole_RM)
  builder.AddPlayer(0.000000, -0.020000, e_PlayerRole_CF)
  builder.AddPlayer(-0.1, -0.1, e_PlayerRole_LB)
  builder.AddPlayer(-0.1,  0.1, e_PlayerRole_CB)
  builder.SetTeam(second_team)
  builder.AddPlayer(-1.000000, 0.000000, e_PlayerRole_GK, controllable=False)
  builder.AddPlayer(-0.04,  0.040000, e_PlayerRole_RM)
  builder.AddPlayer(-0.04, -0.040000, e_PlayerRole_CF)
  builder.AddPlayer(-0.1, -0.1, e_PlayerRole_LB)
  builder.AddPlayer(-0.1,  0.1, e_PlayerRole_CB)
