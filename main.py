from unicodedata import name
from db.database import Database
from helper.WriteAJson import writeAJson

db = Database("db", "livros")

# Create
db.create("Clean Code", "Robert Martin", 2008, 31.0)
db.create("Harry Potter e a pedra fisofolal", "JK Rowling", 1997, 32.0)
db.create("A Guerra dos Tronos", "George R. R. Martin", 1996, 52.9)

# Read
db.read()

# Update
db.update("A Guerra dos Tronos", 45.9)

# Delete
db.delete("Clean Code")
