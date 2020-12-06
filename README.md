# selenium
Selenium Test Project

# Standalon Setup
docker run -d --rm --name selenium -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-firefox:4.0.0-beta-1-prerelease-20201202

# Recording This example shows how to start the containers manually:
    docker network create grid
    docker run -d -p 4444:4444 -p 6900:5900 --net grid --name selenium -v /dev/shm:/dev/shm selenium/standalone-chrome:4.0.0-beta-1-prerelease-20201202
    docker run -d --net grid --name video -v /tmp/videos:/videos selenium/video:ffmpeg-4.3.1-20201202
    # Run your tests
    docker stop video && docker rm video
    docker stop selenium && docker rm selenium
