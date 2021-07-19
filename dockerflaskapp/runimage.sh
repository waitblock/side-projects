docker run python-docker
docker run --publish 5000:5000 python-docker
#test image via curl
curl localhost:5000
#view currently running images
docker ps
