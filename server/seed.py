from server.app import app
from server.models import db
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance

with app.app_context():
    print("Seeding database...")

    Appearance.query.delete()
    Guest.query.delete()
    Episode.query.delete()

    guest1 = Guest(name="Trevor Noah", occupation="Comedian")
    guest2 = Guest(name="Zendaya", occupation="Actress")
    db.session.add_all([guest1, guest2])

    episode1 = Episode(date="2024-01-10", number=101)
    episode2 = Episode(date="2024-01-17", number=102)
    db.session.add_all([episode1, episode2])
    db.session.commit()

    app1 = Appearance(rating=5, guest_id=guest1.id, episode_id=episode1.id)
    app2 = Appearance(rating=4, guest_id=guest2.id, episode_id=episode2.id)
    db.session.add_all([app1, app2])
    db.session.commit()

    print("Done seeding!")