from distutils.core import setup
setup(
  name = 'pods',
  packages = ['pods'], # this must be the same as the name above
  package_data={'pods': ['defaults.cfg', 'data_resources.json', 'football_teams.json']},
  version = 'v0.0.2-alpha',
  description = 'Python software for Open Data Science',
  author = 'The Open Data Science Initiative',
  author_email = 'lawrennd@gmail.com',
  url = 'https://github.com/sods/ods', # use the URL to the github repo
  download_url = 'https://github.com/sods/ods/tarball/v0.0.2-alpha', 
  keywords = ['datascience', 'open', 'google sheet'], 
  classifiers = [],
)
