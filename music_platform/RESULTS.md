# Task

## outlines

- **[import models and adjust timezone](#import-models-and-adjust-timezone)**
- **[create some artists](#create-some-artists)**
- **[List down all artists](#list-down-all-artists)**
- **[create some albums](#create-some-albums)**
- **[list down all artists sorted by name](#list-down-all-artists-sorted-by-name)**
- **[list down all artists whose name starts with `A`](#list-down-all-artists-whose-name-starts-with-a)**
- **[get latest released album](#get-latest-released-album)**
- **[get all albums released before today](#get-all-albums-released-before-today)**
- **[get all albums released today or before but not after today](#get-all-albums-released-today-or-before-but-not-after-today)**
- **[count the total number of albums](#count-the-total-number-of-albums)**
- **[list down all albums ordered by cost then by name](#list-down-all-albums-ordered-by-cost-then-by-name)**
- **[in 2 different ways, for each artist, list down all of his/her albums](#in-2-different-ways-for-each-artist-list-down-all-of-his-or-her-albums)**

## import models and adjust timezone

```shell
from artists.models import Artist
from albums.models import Album
from datetime import datetime, timedelta
```

## Time and date settings

```shell
today = datetime.now()
yesterday = today - timedelta(1) 
tomorrow = today + timedelta(1) 
```

## create some artists

```shell
# Creata an artist and save it to the database

artist_1 = Artist(stage_name = 'Ahmed', social_link = 'https://www.youtube.com/c/Ahmed').save()

artist_2 = Artist(stage_name = 'Asala', social_link = 'https://www.youtube.com/c/Asala').save()

artist_3 = Artist(stage_name = 'Adnan', social_link = 'https://www.youtube.com/c/Adnan').save()

artist_4 = Artist(stage_name = 'Hamaki', social_link = 'https://www.youtube.com/c/Hamaki').save()

artist_5 = Artist(stage_name = 'Muslim', social_link = 'https://www.youtube.com/c/Muslim').save()

artist_6 = Artist(stage_name = 'Shereen', social_link = 'https://www.youtube.com/c/Shereen').save()
```

## List down all artists

```shell
# print all artists (sorted by stage_name by default)
Artist.objects.all() 

#print all artists (sorted by stage_name by default) values
Artist.objects.all().values()
```

- **Output**

```shell
# output for Artist.objects.all()
<QuerySet [<Artist: Adnan>, <Artist: Ahmed>, <Artist: Asala>, <Artist: Hamaki>, <Artist: Muslim>, <Artist: Shereen>]>

# output for Artist.objects.all().values()
<QuerySet [{'id': 3, 'stage_name': 'Adnan', 'social_link': 'https://www.youtube.com/c/Adnan'}, {'id': 1, 'stage_name': 'Ahmed', 'social_link': 'https://www.youtube.com/c/Ahmed'}, {'id': 2, 'stage_name': 'Asala', 'social_link': 'https://www.youtube.com/c/Asala'}, {'id': 4, 'stage_name': 'Hamaki', 'social_link': 'https://www.youtube.com/c/Hamaki'}, {'id': 5, 'stage_name': 'Muslim', 'social_link': 'https://www.youtube.com/c/Muslim'}, {'id': 6, 'stage_name': 'Shereen', 'social_link': 'https://www.youtube.com/c/Shereen'}]>
```

## list down all artists sorted by name

```shell
# print all artists sorted by stage_name (ascending order)
Artist.objects.all().order_by('stage_name')

# print all artists sorted by stage_name (ascending order) values
Artist.objects.all().order_by('stage_name').values()
```

- **Output**

```shell
# output for Artist.objects.all()
<QuerySet [<Artist: Adnan>, <Artist: Ahmed>, <Artist: Asala>, <Artist: Hamaki>, <Artist: Muslim>, <Artist: Shereen>]>

# output for Artist.objects.all().values()
<QuerySet [{'id': 3, 'stage_name': 'Adnan', 'social_link': 'https://www.youtube.com/c/Adnan'}, {'id': 1, 'stage_name': 'Ahmed', 'social_link': 'https://www.youtube.com/c/Ahmed'}, {'id': 2, 'stage_name': 'Asala', 'social_link': 'https://www.youtube.com/c/Asala'}, {'id': 4, 'stage_name': 'Hamaki', 'social_link': 'https://www.youtube.com/c/Hamaki'}, {'id': 5, 'stage_name': 'Muslim', 'social_link': 'https://www.youtube.com/c/Muslim'}, {'id': 6, 'stage_name': 'Shereen', 'social_link': 'https://www.youtube.com/c/Shereen'}]>
```

## list down all artists whose name starts with A

```shell
# print all artists whose name starts with `A`
Artist.objects.filter(stage_name__startswith = 'A')

# print all artists whose name starts with `A` values
Artist.objects.filter(stage_name__startswith = 'A').values()
```

- **Output**

```shell
# output for Artist.objects.filter(stage_name__startswith = 'A')
<QuerySet [<Artist: Adnan>, <Artist: Ahmed>, <Artist: Asala>]>

# output for Artist.objects.filter(stage_name__startswith = 'A').values()
<QuerySet [{'id': 3, 'stage_name': 'Adnan', 'social_link': 'https://www.youtube.com/c/Adnan'}, {'id': 1, 'stage_name': 'Ahmed', 'social_link': 'https://www.youtube.com/c/Ahmed'}, {'id': 2, 'stage_name': 'Asala', 'social_link': 'https://www.youtube.com/c/Asala'}]>
```

## create some albums

```shell
# Create an album and save it to the database

album_1 = Album(name='Cocktails', release_date=datetime(2013, 2, 26, 13, 0, 0), artist=Artist.objects.get(id=1), cost=99.99).save()

album_2 = Album(name='Gym', release_date=datetime(2015, 4, 20, 13, 0, 0), artist=Artist.objects.get(id=3), cost=99.99).save()

album_3 = Album(name='Love', release_date=datetime(2001, 4, 14, 18, 0, 0), artist=Artist.objects.get(id=5), cost=200).save()

album_4 = Album(name='Sad', release_date=datetime(2020, 10, 9, 15, 0, 0), artist=Artist.objects.get(id=1), cost=199.99).save()

album_5 = Album(release_date=datetime(2022, 10, 8, 20, 0, 0), artist=Artist.objects.get(id=2), cost=399.99).save()

album_6 = artist_1.albums.create(name='Happy', release_date=datetime(2019, 10, 8, 20, 0, 0), cost=399.99)
```

## get latest released album

```shell
# Get latest released album
Album.objects.order_by('-release_date')[0]
```

- **Output**

```shell
<Album: New Album>
```

## get all albums released before today

```shell

# Get all albums released before today
Album.objects.filter(release_date__date__lt = today.date())

# Get all albums released before today values
Album.objects.filter(release_date__date__lt = today.date()).values()
```

- **Output**

```shell
# output for Album.objects.filter(release_date__date__lt = today.date())
<QuerySet [<Album: Cocktails>, <Album: Gym>, <Album: Love>, <Album: Sad>, <Album: Happy>]>

# output for Album.objects.filter(release_date__date__lt = today.date()).values()
<QuerySet [{'id': 1, 'artist_id': 1, 'name': 'Cocktails', 'creationDate': datetime.datetime(2022, 10, 8, 16, 27, 56, 116413), 'release_date': datetime.datetime(2013, 2, 26, 13, 0), 'cost': Decimal('99.99')}, {'id': 2, 'artist_id': 3, 'name': 'Gym', 'creationDate': datetime.datetime(2022, 10, 8, 16, 27, 56, 135317), 'release_date': datetime.datetime(2015, 4, 20, 13, 0), 'cost': Decimal('99.99')}, {'id': 3, 'artist_id': 5, 'name': 'Love', 'creationDate': datetime.datetime(2022, 10, 8, 16, 27, 56, 145679), 'release_date': datetime.datetime(2001, 4, 14, 18, 0), 'cost': Decimal('200.00')}, {'id': 4, 'artist_id': 1, 'name': 'Sad', 'creationDate': datetime.datetime(2022, 10, 8, 16, 27, 56, 156082), 'release_date': datetime.datetime(2020, 10, 9, 15, 0), 'cost': Decimal('199.99')}, {'id': 6, 'artist_id': 1, 'name': 'Happy', 'creationDate': datetime.datetime(2022, 10, 8, 16, 28, 11, 862135), 'release_date': datetime.datetime(2019, 10, 8, 20, 0), 'cost': Decimal('399.99')}]>
```

## get all albums released today or before but not after today

```shell
# Get all albums released today or before but not after today
Album.objects.filter(release_date__date__lte = today.date())

# Get all albums released today or before but not after today values
Album.objects.filter(release_date__date__lte = today.date()).values()
```

- **Output**

```shell

# output for Album.objects.filter(release_date__date__lte = today.date()))
<QuerySet [<Album: Cocktails>, <Album: Gym>, <Album: Love>, <Album: Sad>, <Album: New Album>, <Album: Happy>]>

# output for Album.objects.filter(release_date__date__lte = today.date()).values()
<QuerySet [{'id': 1, 'artist_id': 1, 'name': 'Cocktails', 'creationDate': datetime.datetime(2022, 10, 12, 18, 37, 10, 84124), 'release_date': datetime.datetime(2013, 2, 26, 13, 0), 'cost': Decimal('99.99'), 'isApproved': False}, {'id': 2, 'artist_id': 3, 'name': 'Gym', 'creationDate': datetime.datetime(2022, 10, 12, 18, 37, 10, 102256), 'release_date': datetime.datetime(2015, 4, 20, 13, 0), 'cost': Decimal('99.99'), 'isApproved': False}, {'id': 3, 'artist_id': 5, 'name': 'Love', 'creationDate': datetime.datetime(2022, 10, 12, 18, 37, 10, 112166), 'release_date': datetime.datetime(2001, 4, 14, 18, 0), 'cost': Decimal('200.00'), 'isApproved': True}, {'id': 4, 'artist_id': 1, 'name': 'Sad', 'creationDate': datetime.datetime(2022, 10, 12, 18, 37, 10, 123751), 'release_date': datetime.datetime(2020, 10, 9, 15, 0), 'cost': Decimal('199.99'), 'isApproved': False}, {'id': 5, 'artist_id': 2, 'name': 'New Album', 'creationDate': datetime.datetime(2022, 10, 12, 18, 37, 10, 133642), 'release_date': datetime.datetime(2022, 10, 8, 20, 0), 'cost': Decimal('399.99'), 'isApproved': False}, {'id': 6, 'artist_id': 1, 'name': 'Happy', 'creationDate': datetime.datetime(2022, 10, 12, 18, 37, 10, 143720), 'release_date': datetime.datetime(2019, 10, 8, 20, 0), 'cost': Decimal('399.99'), 'isApproved': True}]>
```

## count the total number of albums

```Shell
# Count the total number of albums
Album.objects.count()
```

- **Output**

```shell
6
```

## list down all albums ordered by cost then by name

```shell
# Get all albums ordered by cost then by cost then by name
Album.objects.all().order_by('cost', 'name')

# Get all albums ordered by cost then by cost then by name values
Album.objects.all().order_by('cost', 'name').values()
```

- **Output**

```shell
# output for Album.objects.all().order_by('-cost', 'name')
<QuerySet [<Album: Cocktails>, <Album: Gym>, <Album: Sad>, <Album: Love>, <Album: Happy>, <Album: New Album>]>

# output for Album.objects.all().order_by('-cost', 'name').values()
<QuerySet [{'id': 1, 'artist_id': 1, 'name': 'Cocktails', 'creationDate': datetime.datetime(2022, 10, 8, 16, 27, 56, 116413), 'release_date': datetime.datetime(2013, 2, 26, 13, 0), 'cost': Decimal('99.99')}, {'id': 2, 'artist_id': 3, 'name': 'Gym', 'creationDate': datetime.datetime(2022, 10, 8, 16, 27, 56, 135317), 'release_date': datetime.datetime(2015, 4, 20, 13, 0), 'cost': Decimal('99.99')}, {'id': 4, 'artist_id': 1, 'name': 'Sad', 'creationDate': datetime.datetime(2022, 10, 8, 16, 27, 56, 156082), 'release_date': datetime.datetime(2020, 10, 9, 15, 0), 'cost': Decimal('199.99')}, {'id': 3, 'artist_id': 5, 'name': 'Love', 'creationDate': datetime.datetime(2022, 10, 8, 16, 27, 56, 145679), 'release_date': datetime.datetime(2001, 4, 14, 18, 0), 'cost': Decimal('200.00')}, {'id': 6, 'artist_id': 1, 'name': 'Happy', 'creationDate': datetime.datetime(2022, 10, 8, 16, 28, 11, 862135), 'release_date': datetime.datetime(2019, 10, 8, 20, 0), 'cost': Decimal('399.99')}, {'id': 5, 'artist_id': 2, 'name': 'New Album', 'creationDate': datetime.datetime(2022, 10, 8, 16, 27, 57, 449499), 'release_date': datetime.datetime(2022, 10, 8, 20, 0), 'cost': Decimal('399.99')}]>
```

## in 2 different ways for each artist list down all of his or her albums

```shell
# Get all albums for each artist using related object reference
for artist in Artist.objects.all():
    artist.album_set.all()

# Get all albums for each artist using objects manager
for artist in Artist.objects.all():
    Album.objects.filter(artist = artist)
```

- **Output**

```shell
# output for each artist using related object reference
<QuerySet [<Album: Gym>]>
<QuerySet [<Album: Cocktails>, <Album: Sad>, <Album: Happy>]>
<QuerySet [<Album: New Album>]>
<QuerySet []>
<QuerySet [<Album: Love>]>
<QuerySet []>

# output for each artist using objects manager
<QuerySet [<Album: Gym>]>
<QuerySet [<Album: Cocktails>, <Album: Sad>, <Album: Happy>]>
<QuerySet [<Album: New Album>]>
<QuerySet []>
<QuerySet [<Album: Love>]>
<QuerySet []>
```
