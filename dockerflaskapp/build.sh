docker build --tag python-docker
docker images
#add a tag to our image
docker tag python-docker:latest python-docker:v1.0.0
docker images
