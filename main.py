import pandas as pd

DataType = {
    'scores_and_fixtures' : 'schedule',
    'shooting' : 'shooting',
    'goalkeeping': 'keeper',
    'passing' : 'passing',
    'pass_types' : 'passing_types',
    'goal_and_shot_creation': 'gca',
    'defensive_actions': 'defense',
    'possession': 'possession',
    'miscellaneous_stats': 'misc'
}

Teams = {
    # Laliga Top 5
    '206d90db': 'Barcelona',
    '53a2f082': 'Real-Madrid',
    'db3b9613': 'Atletico-Madrid',
    'e31d1cd9': 'Real-Sociedad',
    '2a8183b3': 'Villarreal',
}
    

Comps = {
    'all_comps': 'All-Competitions',

    # Laliga Competitions
    'c8': 'Champions-League',
    'c12': 'La-Liga',
    'c19': 'Europa-League',
    'c122': 'UEFA-Super-Cup',
    'c569': 'Copa-del-Rey',
    'c646': 'Supercopa-de-Espana',
    'c882': 'Europa-Conference-League',
}


"https://fbref.com/en/squads/53a2f082/2022-2023/all_comps/Real-Madrid-Stats-All-Competitions"    
cl = "https://fbref.com/en/squads/53a2f082/2022-2023/c8/Real-Madrid-Stats-Champions-League"
"https://fbref.com/en/squads/53a2f082/2022-2023/c569/Real-Madrid-Stats-Copa-del-Rey"
"https://fbref.com/en/squads/53a2f082/2022-2023/c646/Real-Madrid-Stats-Supercopa-de-Espana"
"https://fbref.com/en/squads/53a2f082/2022-2023/c122/Real-Madrid-Stats-UEFA-Super-Cup"


bc = "https://fbref.com/en/squads/206d90db/2022-2023/matchlogs/c12/shooting/Barcelona-Match-Logs-La-Liga"
class MatchLogsLink:
    def __init__(self, team_id,year,comp_id, log_type):
        self.team_id = team_id
        self.year = year
        self.comp_id = comp_id
        self.log_type = log_type

        self.link = f'https://fbref.com/en/squads/{self.team_id}/{self.year}/matchlogs/{self.comp_id}/{DataType[self.log_type]}/{Teams[self.team_id]}-Match-Logs-{Comps[self.comp_id]}'
        
    def __repr__(self):
        return self.link


class Data:
    def __init__(self, link):
        self.link = str(link)
    
    def fbref2pandas(self):
        data_list = pd.read_html(self.link)
        for table in data_list:
            df = pd.DataFrame(table)
        
        return df

link = MatchLogsLink('206d90db', '2022-2023', 'c12', 'shooting')
print(link)

data = Data(link)

# print(data.fbref2pandas())
