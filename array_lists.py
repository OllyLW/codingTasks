# Define the class of Album
class Album:
    # Initiate the class with the variables
    # Album_name, numer_of_songs, album_artist
    def __init__ (self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    # Define the string method for the class
    # Makes string 
    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"


# Create a list of albums
# Each album is assigned to the Class
albums1 = [
    Album("Yummy", 16, "James"),
    Album("Cowboy Carter", 27, "Beyonce"),
    Album("One Deep River", 12, "Mark Knopfler"),
    Album("Guts", 12, "Olivia Rodrigo"),
    Album("Gold", 19, "ABBA")
]

# Iterate through albums1 list
# Print each album as per str function in Class
print("Original album list:")
for album in albums1:
    print(album)

# Sort the albums1 list using number_of_songs as key
albums1.sort(key=lambda x: x.number_of_songs)

# Prints the new sorted list
print("\nSorted album list:")
for album in albums1:
    print(album)

# Swap element 1 and 2 around in the album list:
albums1[1], albums1[2] = albums1[2], albums1[1]

# Prints new sorted list
print("\nAlbum list after swapping element 1 and 2:")
for album in albums1:
    print(album)

# Define albums2 list:
albums2 = [
    Album("The Tortured Poets Department", 17, "Taylor Swift"),
    Album("Yeezus", 10, "Kanye West"),
    Album("Eternal Sunshine", 13, "Ariana Grande"),
    Album("Circles", 12, "Mac Miller"),
    Album("30", 12, "Adele")
]

# Print Albums2 list:   
print("\nAlbum 2 list:")
for album in albums2:
    print(album)

# Copy albums1 into albums2:
albums2.extend(albums1)

print("\n Albums1 + Albums2:")
for album in albums2:
    print (album)


# Add specific albums to album 2 list:
albums2.append(Album("Dark Side of the Moon", 9, "Pink Floyd"))
albums2.append(Album("Oops!... I Did It Again", 16, "Britney Spears"))

print("\n New list with specific albums addes:")
for album in albums2:
    print (album)


# Sort the albums 2 list alphabetically by album name:
albums2.sort(key=lambda y: y.album_name)

print("\n New total album list sorted alphabetically:")
for album in albums2:
    print (album)

# Searching for a specific album:

# Initiate a variable to store the index in
index_of_album = None

# Iterate through albums2 to search for Dark Side of the Moon
for index, album in enumerate(albums2):
    if album.album_name == "Dark Side of the Moon":
        index_of_album = index
        break

# Check if the album has been found and if it has print the index
if index_of_album is not None:
    print(f"\nThe index of Dark Side of the Moon is: {index_of_album}")
else:
    print("Dark Side of the Moon is not found in Albums list")