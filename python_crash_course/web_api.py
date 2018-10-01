#%%
import requests
import pygal
from IPython.display import SVG, HTML
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

print('Status Code: ', r.status_code)
response_dict = r.json()
print("Total Repositories:", response_dict['total_count'])

#Explore information about repositories
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

html_pygal = """
<!DOCTYPE html>
<html>
  <head>
  <script type="text/javascript" src="http://kozea.github.com/pygal.js/javascripts/svg.jquery.js"></script>
  <script type="text/javascript" src="http://kozea.github.com/pygal.js/javascripts/pygal-tooltips.js"></script>
    <!-- ... -->
  </head>
  <body>
    <figure>
      {pygal_render}
    </figure>
  </body>
</html>
"""

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#Make Visualisation

my_style = LS('#664455', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python projects on Github'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos_svg')
HTML(html_pygal.format(pygal_render=chart.render()))