
sudo find . -name "._*" -type f -delete && docker-compose up --build

ou
sudo find . -name "._*" -type f -delete && docker-compose up -d --build


docker-compose down  