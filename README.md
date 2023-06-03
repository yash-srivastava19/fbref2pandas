## FBREF2PANDAS - Export FBRef data to Pandas Dataframe

A scraper that directly gives football(not soccer) data from FBRef website directly to Pandas dataframe. Major teams and leagues supported.

[Project Repository](https://github.com/yash-srivastava19/fbref2pandas)
[PyPi Project](https://pypi.org/project/fbref2pandas/)

Contribute to the Project so that everyone can benefit from it.

*Disclaimer : This package in no way tries to take away from the work of FBRef.com I love that website and just needed a package that makes my life easier*

To install the package(it just requires `pandas` !!) : 

``` pip install fbref2pandas ```

After installation, create a `MatchLogsLink` object by providing it the following arguments(in `str` format) :

- team_id : The identifier of the team. Generally, as I have noticed, fbref uses a particular `id` for each of the team. It is a 8 character string that uniquely identifies a football team. See this table for `id` of some popular teams.

| Team ID       | Team Name        |
| ------------- | ---------------  |
| '206d90db'    | 'Barcelona'      |
| '53a2f082'    | 'Real-Madrid'    |
| 'db3b9613'    | 'Atletico-Madrid'|
| 'e31d1cd9'    | 'Real-Sociedad'  |
| '2a8183b3'    | 'Villarreal'     |

Just copy the `team_id` and pass as the first argument. 

- `year` : The `year` for which the data is required. The `year` is in the format `2022-2023`(for 2022-23 season). Pass this as second argument in the `MatchLogsLink` object.


- `comp_id` : The `comp_id` is also one of the variables that fbref maintains internally, as far as I can deduce. The `comp_id` is of the form `cXXX`, and can be found from the fbref website. See this table below for some common `comp_id`


| Comp ID       | Competition Name           |
| ------------- | -------------------------- |
| 'c8'          | 'Champions-League'         |
| 'c12'         | 'La-Liga'                  |
| 'c19'         | 'Europa-League'            |
| 'c122'        | 'UEFA-Super-Cup'           |
| 'c569'        | 'Copa-del-Rey'             |
| 'c646'        | 'Supercopa-de-Espana'      | 
| 'c882'        | 'Europa-Conference-League' |

- `log_type` : I love how many stats are available in the fbref website. These are just awesome for your next project. The `log_type` could be any of these values:


|  Log Type                |
| ------------------------ |
| 'scores_and_fixtures'    |
| 'shooting'               |
| 'goalkeeping'            |
| 'passing'                |
| 'pass_types'             |
| 'goal_and_shot_creation' |
| 'defensive_actions'      |
| 'possession'             |
| 'miscellaneous_stats'    |


After passing these 4 parameters to the `MatchLogsLink` object, most of the task is done. Just create a new `Data` object, and pass the above `MatchLogsLink` object. An example of this would be : 

```
from fbref2pandas.classes import MatchLogsLink, Data

link = MatchLogsLink('206d90db', '2022-2023', 'c12', 'shooting')
# print(link)  

data = Data(link)
```
If the link is correct, there shouldn't be a problem. Now, to get the data as a `DataFrame` object, just call the function `fbref2pandas()` of the `Data` object. The functions returns the data as a pandas `Dataframe`. If the link is incorrect, an exception is raised. Just double check if the data from the table above. Enjoy the data. 

To get the data as `DataFrame` : 

```
df = data.fbref2pandas()
```

Note : I comply with all the rules given for the data use in the [sports reference website](https://www.sports-reference.com/data_use.html), and I believe that it is in fair use. Not many requests will be taken from this package.  

Note : Help would be really appreciated to expand this package. Create a PR and add whatever you could scrape from links of FBRef. Great PRs will be merged on small notices.
