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

# If table isn't empty, empty it
Post.query.delete()

posts = [    
    {"title": "Ethan Hunt Returns in Mission: Impossible 8", "content": "Tom Cruise reprises his role as Ethan Hunt in the upcoming Mission: Impossible 8. The movie promises to be just as action-packed as its predecessors, with Cruise performing many of his own stunts.", "created_at": "2023-04-17 09:15:32", "user_id": 1},    
    {"title": "Maverick is Back in Top Gun: Maverick", "content": "Tom Cruise returns as Maverick in the long-awaited sequel Top Gun: Maverick. Fans of the original will be pleased to see the return of many beloved characters, and the movie promises to deliver just as much high-flying action and drama as the first.", "created_at": "2023-04-18 14:37:09", "user_id": 1},    
    {"title": "Jack Reacher: Never Go Back Hits Theaters", "content": "Tom Cruise stars in the latest installment of the Jack Reacher series, Never Go Back. The movie is full of tense action sequences and thrilling suspense, and fans of the previous movie will be pleased to see Cruise return in top form.", "created_at": "2023-04-20 08:52:17", "user_id": 1},
    {"title": "Maleficent: Mistress of Evil Brings More Magic and Action", "content": "Angelina Jolie reprises her role as the dark fairy Maleficent in Maleficent: Mistress of Evil. The movie adds more magic and action to the story of the beloved villain, and Jolie's performance continues to captivate audiences.", "created_at": "2023-04-18 13:45:21", "user_id": 3},
    {"title": "Lara Croft: Tomb Raider Takes Audiences on an Epic Adventure", "content": "Angelina Jolie stars as the iconic adventurer Lara Croft in Lara Croft: Tomb Raider. The movie takes audiences on an epic adventure full of danger, excitement, and stunning visuals. Jolie's portrayal of the fearless Croft has become a classic in the action-adventure genre.", "created_at": "2023-04-19 11:30:17", "user_id": 3},
    {"title": "Changeling Tells a Haunting Story of a Mother's Love", "content": "Angelina Jolie delivers a powerful performance in the haunting drama Changeling. Based on a true story, the movie tells the tale of a mother's search for her missing son and the corrupt system that tries to cover up the truth. Jolie's portrayal of the grief-stricken mother is heart-wrenching and unforgettable.", "created_at": "2023-04-20 08:20:45", "user_id": 3},
    {"title": "The Revenant: A Gripping Tale of Survival and Revenge", "content": "Leonardo DiCaprio delivers a tour-de-force performance in The Revenant, a gripping tale of survival and revenge set in the brutal wilderness of the 19th century American West. DiCaprio's portrayal of Hugh Glass, a fur trapper left for dead by his companions, is raw, intense, and deeply moving.", "created_at": "2023-04-17 16:25:07", "user_id": 10},
    {"title": "The Departed: A Tense Crime Thriller with an All-Star Cast", "content": "Leonardo DiCaprio stars alongside Matt Damon, Jack Nicholson, and Mark Wahlberg in the tense crime thriller The Departed. DiCaprio's portrayal of Billy Costigan, an undercover cop trying to take down a powerful criminal organization, is nuanced and complex, adding to the suspense and intrigue of the movie.", "created_at": "2023-04-18 19:55:02", "user_id": 10},
    {"title": "Inception: A Mind-Bending Action Thriller with Stunning Visuals", "content": "Leonardo DiCaprio leads an all-star cast in the mind-bending action thriller Inception. The movie takes audiences on a journey through dreamscapes and alternate realities, with DiCaprio's character Cobb leading the charge. The stunning visuals, complex plot, and standout performances make Inception a must-see for any movie lover.", "created_at": "2023-04-20 15:10:37", "user_id": 10},
    {"title": "John Wick 4 Release Date Announced", "content": "Keanu Reeves returns as John Wick in the upcoming fourth installment of the action franchise. The release date has been set for May 24, 2024, and fans are eagerly anticipating the return of the legendary hitman.", "created_at": "2023-04-19 10:30:00", "user_id": 6},
    {"title": "Neo is Back in The Matrix Resurrections", "content": "Keanu Reeves reprises his role as Neo in The Matrix Resurrections, the fourth movie in the iconic sci-fi franchise. The movie promises to be just as mind-bending as its predecessors, with Reeves once again proving his status as an action superstar.", "created_at": "2023-04-19 14:45:00", "user_id": 6},
    {"title": "Keanu Reeves Joins Star-Studded Cast of Knives Out 2", "content": "Keanu Reeves is set to join the impressive cast of Knives Out 2, the sequel to the hit 2019 murder mystery. The star-studded cast also includes Daniel Craig, Kate Hudson, and Edward Norton, and the movie is sure to be a thrilling ride for audiences.", "created_at": "2023-04-20 09:00:00", "user_id": 6}
]

# Add new objects to session, so they'll persist
for post in posts:
    p = Post(
        title=post["title"],
        content=post["content"],
        created_at=post["created_at"],
        user_id=post["user_id"]
    )
    db.session.add(p)

# Commit--otherwise, this never gets saved!
db.session.commit()