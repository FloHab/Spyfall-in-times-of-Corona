# Passwort: 1.spionspion
# Email: spionedasspiel@gmail.com
import smtplib, ssl
import random

players = {"Player1": "player1@gmail.com", "Player2": "player2@gmail.com"}

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "sender_address@gmail.com" # here goes the mail address you want to send the mail from
password =  "password"# here goes the password of the sender address
text_template = 'Hello {0},' \
                '\n your role is "{1}" and your location is "{2}". ' \
                '\n Remember, possible locations are:{3}.'

locations = {'Airplane': ['First Class Passenger', ' Air Marshal', 'Mechanic', 'Air Hostess', 'Co-Pilot', 'Captain', 'Economy Class Passenger'],
'bank': ['Armored Car Driver', 'Manager', 'Consultant', 'Robber', 'Security Guard', 'Teller', 'Customer'],
'beach': ['Beach Waitress', 'Kite Surfer', 'Lifeguard', 'Thief', 'Beach Photographer', ' Ice Cream Truck Driver', 'Beach Goer'],
'cathedral': ['Priest', 'Beggar', 'Sinner', 'Tourist', 'Sponsor', 'Chorister', 'Parishioner'],
'cemetery': ['Priest', 'Grave Robber', 'Poet', 'Mourning Person', 'Gatekeeper', 'Dead Person', 'Zombie'],
'circus tent':  ['Acrobat', 'Animal Trainer', 'Magician', 'Fire Eater', 'Clown', 'Juggler', 'Visitor'],
'corporate party': ['Entertainer', 'Manager', 'Unwanted Guest', 'Owner', 'Secretary', 'Delivery Boy', 'Accountant'],
'crusader army':  ['Monk', 'Imprisoned Saracen', 'Servant', 'Bishop', 'Squire', 'Archer', 'Knight'],
'casino': ['Bartender', 'Head Security Guard', 'Bouncer', 'Manager', 'Hustler', 'Dealer', 'Gambler'],
'hospital': ['Nurse', 'Doctor', 'Anesthesiologist', 'Intern', 'Therapist', 'Surgeon', 'Patient'],
'hotel':['Doormann','Security Guard', 'Manager', 'Housekeeper', 'Bartender','Bellman', 'Customer'],
'military base':['Deserter', 'Colonel','Medic''Sniper','Officer','Tank Engineer', 'Soldier'],
'passage train': ['Border Patrol', 'Train Attendant', 'Restaurant Chef', 'Mechanic', 'Train Driver','Stoker','Passenger'],
'pirate ship':['Cook', 'Slave','Cannoneer', 'Tied Up Prisoner', 'Cabine Boy', 'Brave Captain','Sailor'],
'polar station':['Medic', 'Expedition Leader','Biologist', 'Radioman', 'Hydrologist','Meterologist','Geologist'],
'police staion':['Detective','Laywer','Journalist','Criminalist''Archivist','Archivist','Criminal','Patrol Officer'],
'restaurant':['Musician', 'Bouncer','Hostess', 'Head Chef', 'Food Critic', 'Waiter', 'Customer'],
'service station':['Manager', 'Tire Specialist','Biker', 'Car Owner', 'Car Wash Operator', 'Electrician', 'Auto Mechanic'],
'space station':['Engineer', 'Alien', 'Pilot', 'Commander','Scientist', 'Doctor', 'Space Tourist'],
'submarine': ['Cook', 'Commander','Sonar Techician','Electronics Technician', 'Radioman','Navigator','Sailor'],
'theater':['Coat Check Lady', 'Prompter','Cashier','Director','Actor','Crew Man', 'Audience Member'],
'world war II squad':['Resistance Fighter','Radioman','Scout','Medic','Cook', 'Imprisoned Nazi', 'Soldier'],
'nanobiophotonic':['Stefan Hell', 'Stefan Jakobs', 'Jay', 'Nickels', 'Marcel', 'Sylvia', 'Stefan Stoldt'],
'race track':['Team Owner', 'Driver','Engineer','Spectator', 'Referee','Mechanic', 'Food Vendor','Commentator'],
'art museum':['Ticket Seller','Student','Visitor','Teacher','Security Guard', 'Painter', 'Art Collector'],
'vineyard':['Gardener', 'Gourmet Guide', 'Winemaker', 'Exporter', 'Butler', 'Wine Taster', 'Sommelier'],
'baseball stadium':['Spectator','Pitcher', 'Catcher', 'Commentator','Security Guard', 'First Basemann', 'Manager'],
'library':['Old Man','Journalist','Author','Volunteer','Know-It-All', 'Student','Librarian'],
'cat show':['Judge', 'Sarah Schweighofer', 'Cat Handler', 'Veterinarian','Cat Trainer', 'Crazy Cat Lady', 'Cat'],
'retirement home':['Relative', 'Cribbage Player','Old Person','Nurse','Blind Person','Cook','Janitor'],
'jail':['Wrongly Accused Man', 'CCTV Operator', 'Guard', 'Visitor','Laywer', 'Criminal','Mainiac', 'Jailkeeper'],
'construction site':['Free-Roaming Toddler', 'Contractor', 'Crane Driver', 'Trespasser','Engineer','Architect','Construction Worker'],
'the united nations': ['Diplomat', 'Interpreter','Blowhard','Tourist','Journalist', 'Secretary of State','Speaker'],
'candy factory':['Lobbyist','Candy Maker','Pastry Chef','Visitor','Taster', 'Truffle Maker', 'Packager'],
'subway':['Tourist','Subway Operator','Ticket Inspector','Pregnant Lady','Pickpocket', 'Cleaner', 'Old Lady'],
'coal mine':['Safety Inspector', 'Miner','Overseer', 'Dump Truck Operator','Driller','Coordinator','Blasting Engineer'],
'rock concert':['Guitarist','Drummer','Roadie','Groupie','Security Guard', 'Bassist','Fan'],
'wedding':['Bride','Flower Girl','Father of the Bride','Wedding Crasher', 'Best Man', 'Maid of Honor','Relative']
}

def get_location(players, locations):
    idxs = random.sample(range(0, 6), len(players)-1)
    location = random.choice(list(locations.keys()))
    roles = [locations[location][idx] for idx in idxs]
    roles.append('Spy')
    random.shuffle(roles)
    return(roles, location)
def write_email(players, roles, location):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        for player, role in zip(players, roles):
            if role == 'Spy':
                message = 'Hello {0},' \
                          '\n you are the spy and you don\'t know the location. ' \
                          '\n Remember, possible locations are:{1}.'.format(player, locations.keys())
                server.login(sender_email, password)
                server.sendmail(sender_email, players[player], message)
            else:
                message = text_template.format(player, role, location, locations.keys())
                server.login(sender_email, password)
                server.sendmail(sender_email, players[player], message)

roles, location = get_location(players, locations)
write_email(players, roles, location)
