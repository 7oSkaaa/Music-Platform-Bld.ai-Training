from datetime import datetime, timezone
from artists.models import Artist
from music_platform import settings
from django.core.mail import send_mail
from celery import shared_task


@shared_task(bind=True)
def send_mail_task(self, album_name, artist_id):
    artist = Artist.objects.get(id=artist_id)
    send_mail(
        subject = 'Congratulations! 🎊',
        message= f'Congratulations {artist.stage_name} on your new album {album_name}, we will review it and get back to you soon. 🎉',
        from_email= settings.EMAIL_HOST_USER,
        recipient_list=[artist.user.email,],
        fail_silently= False,
    )
    return f'Email sent successfully to {artist.stage_name}'


# check if the artist is active on the platform
def isActive(artist):
    if artist.albums.all().count() == 0:
        return False
    album = artist.albums.all().latest('created')
    days = datetime.now(timezone.utc) - album.created
    return days.days <= 30


@shared_task(bind=True)
def send_mail_every_day_task(self):
    for artist in Artist.objects.all():    
        if not isActive(artist):
            send_mail(
                subject = "Warning ⚠️",
                message= "You haven't created an album in the past 30 days.\nSo, we want to let you know that your inactivity is causing your popularity on our platform to decrease.",
                from_email= settings.EMAIL_HOST_USER,
                recipient_list=[artist.user.email,],
                fail_silently= False,
            )
    return 'Warning emails were sent successfully 📧'