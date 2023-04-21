"""Seed file to make sample data for pets db."""

from models import User, Post, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

celebrities = [
    {"first_name": "Tom", "last_name": "Cruise", "image_url": "https://flxt.tmsimg.com/assets/378_v9_bd.jpg"},
    {"first_name": "Brad", "last_name": "Pitt", "image_url": "https://images.mubicdn.net/images/cast_member/2552/cache-207-1524922850/image-w856.jpg?size=800x"},
    {"first_name": "Angelina", "last_name": "Jolie", "image_url": "https://m.media-amazon.com/images/M/MV5BODg3MzYwMjE4N15BMl5BanBnXkFtZTcwMjU5NzAzNw@@._V1_.jpg"},
    {"first_name": "Beyonce", "last_name": "Knowles", "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/17/Beyonc%C3%A9_at_The_Lion_King_European_Premiere_2019.png"},
    {"first_name": "Jay-Z", "last_name": "Carter", "image_url": "https://image.cnbcfm.com/api/v1/image/106809430-1607619168484-gettyimages-1201923517-dsc_5270_2020012520224968.jpg?v=1679940636"},
    {"first_name": "Keanu", "last_name": "Reeves", "image_url": "https://flxt.tmsimg.com/assets/1443_v9_bc.jpg"},
    {"first_name": "Emma", "last_name": "Watson", "image_url": "https://akns-images.eonline.com/eol_images/Entire_Site/2023317/rs_1200x1200-230417122054-1200-emma-watson.cm.41723.jpg"},
    {"first_name": "Will", "last_name": "Smith", "image_url": "https://variety.com/wp-content/uploads/2023/02/GettyImages-1445892465.jpg"},
    {"first_name": "Meryl", "last_name": "Streep", "image_url": "https://prod-images.tcm.com/Master-Profile-Images/MerylStreep.185873.3.jpg"},
    {"first_name": "Leonardo", "last_name": "DiCaprio", "image_url": "https://hips.hearstapps.com/hmg-prod/images/gettyimages-1197345888.jpg"},
    {"first_name": "Adam", "last_name": "Devine", "image_url": "https://pyxis.nymag.com/v1/imgs/95e/5aa/f0e41a8edea9d2742c45707e766b7da2fa-adam-devine.jpg"},
    {"first_name": "Steve", "last_name": "Buscemi", "image_url": "https://cdn.britannica.com/16/221316-050-680EBB62/Steve-Buscemi-2012.jpg"},
    {"first_name": "Blake", "last_name": "Lively", "image_url": "https://media.allure.com/photos/63d3e7eedc36bb79e3ad5a4b/1:1/w_2564,h_2564,c_limit/blake%20lively%20brunette%20hair.jpg"},
]

# Add new objects to session, so they'll persist
for celebrity in celebrities:
    user = User(
        first_name=celebrity["first_name"],
        last_name=celebrity["last_name"],
        image_url=celebrity["image_url"]
    )
    db.session.add(user)

# Commit--otherwise, this never gets saved!
db.session.commit()
