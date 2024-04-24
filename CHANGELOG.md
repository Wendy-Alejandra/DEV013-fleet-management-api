## <1.1.0> - <2024-04-24>

### Sprint learnings

* Creation of swagger documentation (not fully)
* Modularizing the project (still learning).
* Creation of endpoints and its pagination.
* paginate() is a non iterable object so I learnt the use of .item which iterates it as a list.
* Use of postman to check how to paginate the endpoint and apply it to the code using SQLAlchemy.

### Added

* Created folder models to store taxi model at first place.
* Created the config.py file to set up SQLAlchemy module and interact with postgre db and separate responsibilities in the app.py file.
* Created templates folder and added an index.html file (for practicing).
* Created the endpoint /taxis in the app.py file with its pagination using SQLAlchemy.

### Changed

* Changed the conexion.py file to vercel_connect.py (this file is not in use)

### Fixed

N/A

### Removed

* Removed templates folder I added for practicing routes creations

-----------------------------------------------------------------------------------------------------------------

## <1.0.0> - <2024-04-17>

### Sprint learnings

* Vercel postgresSQL
* Database connection (from vercel postgre to PGAdmin and to VSCode) using psycopg2 module to access postgreSQL
* Environment variables and accessing to those variables using os module with os.getenv(""), os.environ.get("") and os.environ[""]
* SQL commands in PostgreSQL (tables creation, visualization, data insertion from vercel and PGAdmin)
* Running flask app with a simple routing using http://127.0.0.1:5000 (for practicing)


### Added

* Created database in vercel
* Created the SRC folder
* Created a conexion.py file
* Stablished connection to vercel database in the conexion.py file
* Created taxis and trajectories tables
* Inserted the data provided by Laboratoria into each table
* Created the app.py file to run flask (for practicing)
* Created templates folder and added an index.html file (for practicing)

### Changed

N/A

### Fixed

N/A

### Removed

N/A