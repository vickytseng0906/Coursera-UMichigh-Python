import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

cur.executescript('''
	DROP TABLE IF EXISTS Artist;
	DROP TABLE IF EXISTS Genre;
	DROP TABLE IF EXISTS Album;
	DROP TABLE IF EXISTS Track;
	''')
cur.execute('''
	CREATE TABLE IF NOT EXISTS Artist (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		name TEXT UNIQUE
	)
	''')
cur.execute('''
	CREATE TABLE IF NOT EXISTS Genre (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		name TEXT UNIQUE
	)
	''')
cur.execute('''
	CREATE TABLE IF NOT EXISTS Album (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		artist_id INTEGER,
		title TEXT UNIQUE
	)
	''')
cur.execute('''
	CREATE TABLE IF NOT EXISTS Track (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		title TEXT UNIQUE,
		album_id INTEGER,
		genre_id INTEGER,
		len INTEGER,
		rating INTEGER,
		count INTEGER
	)
	''')

def lookup(p, key):
	found = False
	for c in p:
		if found: return c.text
		if c.tag == 'key' and c.text == key:
			found = True
	return None

stuff = ET.parse('Library.xml')
all = stuff.findall('dict/dict/dict')
print ('Dict count:', len(all))

for entry in all:
	if lookup(entry, 'Track ID') is None : continue
	artist = lookup(entry, 'Artist')
	genre = lookup(entry, 'Genre')
	album = lookup(entry, 'Album')
	title = lookup(entry, 'Name')
	length = lookup(entry, 'Total Time')
	rating = lookup(entry, 'Rating')
	count = lookup(entry, 'Play Count')
	if title is None or artist is None or album is None or genre is None: continue
	cur.execute('''INSERT OR IGNORE INTO Artist (name) VALUES ( ? )''', ( artist, ) )
	cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
	artist_id = cur.fetchone()[0]
	cur.execute('''INSERT OR IGNORE INTO Genre (name) VALUES ( ? )''', ( genre, ) )
	cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
	genre_id = cur.fetchone()[0]
	cur.execute('''INSERT OR IGNORE INTO Album (artist_id, title) VALUES (?, ?)''', (artist_id, album))
	cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
	album_id = cur.fetchone()[0]
	cur.execute('''INSERT OR IGNORE INTO Track (title, album_id, genre_id, len, rating, count) VALUES (?, ?, ?, ?, ?, ?)''', (title, album_id, genre_id, length, rating, count))
	cur.execute('SELECT id FROM Track WHERE title = ? ', (title, ))
	track_id = cur.fetchone()[0]

conn.commit()

cur.execute('''
	SELECT Track.title, Artist.name, Album.title, Genre.name FROM Track JOIN Album JOIN Artist JOIN Genre
	ON Track.genre_id = Genre.ID and Track.album_id = Album.id and Album.artist_id = Artist.id
	ORDER BY Track.title
	LIMIT 3
	''')
rows = cur.fetchall()
for row in rows:
	print ("Title:", row[0], ",Artist:", row[1] ,",Album:", row[2] ,",Genre:", row[3])
