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

class MatchLogsLink:
    def __init__(self,team_id,year,comp_id, log_type):
        self.team_id = team_id
        self.year = year
        self.comp_id = comp_id
        self.log_type = log_type

        self.link = f'https://fbref.com/en/squads/{self.team_id}/{self.year}/matchlogs/{self.comp_id}/{DataType[self.log_type]}/{Teams[self.team_id]}-Match-Logs-{Comps[self.comp_id]}'

    def __repr__(self):
        return self.link


class Data:
    def __init__(self, link: MatchLogsLink):
        self.link = str(link)
    
    def fbref2pandas(self):
        try:
            data_list = pd.read_html(self.link)
        
        except Exception as e:
            print(f'The link {repr(self.link)} is not able to scrape the table from the FBRef website. Try checking for some typos.')    
        
        for table in data_list:
            df = pd.DataFrame(table)
        
        return df
