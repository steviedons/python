#%%
import requests
import plotly
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

print('Status Code: ', r.status_code)
response_dict = r.json()
print("Total Repositories:", response_dict['total_count'])

#Explore information about repositories
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#Make Visualisation
 
data = [go.Bar(
            x=names,
            y=stars
        )]

plotly.offline.init_notebook_mode(connected=True)
iplot(data)