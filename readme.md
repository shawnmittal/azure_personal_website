# Azure App Services With Docker and Python Flask

## Intro
Building a personal website, but doing so with Azure App Services to demonstrate a containerized deployment for a simple flask web application. 

As a disclaimer, this is definitely not the best way to deploy multiple applications into production. Ideally, each application should have it's own lightweight container image and be deployed via some sort of container orchestration tool. The reason I didn't do this is because I didn't feel like managing a set of microservices for an application that is not going to need to operate at scale. 

The actual Docker image ends up being pretty chunky, but it works for my use case so I'm ok with it. Also of note, don't use python on an alpine image. See third bullet in references section.

## Local Build
To build the docker image run `./scripts/docker-build-local.sh`. This builds an image based on Dockerfile in top level project directory. To run the docker image run `./scripts/docker-run-local.sh`, which port forwards from container to localhost:5000.

## Example Projects Included
- Bokeh dashboard: I built a quick Bokeh dashboard using the titanic dataset to test access and functionality for Bokeh dashboards on US Government networks. Sixty percent of the time it works every time.
- VADER Sentiment Analysis: A quick nlp application that analyzes news articles based on the url you pass to it. Wanted to include something data sciency on my website, but couldn't share any of my day-job work and didn't feel like spending too much time/resources on a demo app.

## References
* [Microsoft Sample Flask Code](https://github.com/microsoft/python-sample-vscode-flask-tutorial)
* [Microsoft Docker Container Deployment Tutorial](https://docs.microsoft.com/en-us/azure/python/tutorial-deploy-containers-01)
* [Using Alpine Can Make Python Docker Builds 50x Slower](https://pythonspeed.com/articles/alpine-docker-python/)