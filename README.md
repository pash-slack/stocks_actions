# Github Actions Trial/Demo 
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fpash-slack%2Fstocks_actions.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fpash-slack%2Fstocks_actions?ref=badge_shield)



#### Description

This simple Python program pulls information about Slack's stock and has some simple tests associated with it. 

Some of the functionality demoed here includes (*see the workflows directory*): 

- Building on multiple platforms (Windows, Ubuntu, MacOs) 
- Building with different versions of Python `(2.7, 3.8)` in parallel
- Read env variables from YAML 
- Common workflows 
  - env setup (`pip` installations)
  - linting 
  - building and running 
  - test executions
- PR workflows
- Usage of other workflows e.g. labelling outdated PRs
- Create a Docker image for a new release 
- Push Docker image to Github Packages! 
- Send a notification to Slack
- Secrets (dummy data) management within Github 
- Utilization of caching

Sharing workflows within an org: 
- https://docs.github.com/en/actions/learn-github-actions/sharing-workflows-with-your-organization








## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fpash-slack%2Fstocks_actions.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fpash-slack%2Fstocks_actions?ref=badge_large)