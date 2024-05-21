## <1.5.0> - <2024-05-22>

### Sprint learnings

* Use of subqueries into a main query in SQLAlchemy.
* Using .paginate() vs .all() methods in SQLAlchemy. They don't work together.
* .all() method runs the query and returns all results as a list of objects.
* .paginate() Flask-SQLAlchemy method used to devide a big amount of data in smaller pages. Should be applied directly to the query before converting to JSON format.
* .strftime() python method used to format datetime objects into a text string according to a specified format. This is useful because JSON does not have a native datetime data type and needs to work with text strings to represent dates and times.
* .gitignore file updated to ignore unnecessary cached files and folders using the `git rm -r --cached .` command in the terminal (windows bash).


### Added

* `controllers` folder for the 3 endpoints (taxis, trajectories/id and trajectories/latest)

### Changed

* import routes in the `app.py` file (from `controllers` folder)

### Fixed

N/A

### Removed

N/A

-----------------------------------------------------------------------------------------------------------------

## <1.4.0> - <2024-05-15>

### Sprint learnings

* SQLite connection for testing purposes
* Use of SQLAlchemy to create tables and insert data in SQLite
* Run in the terminal `ENVIRONMENT=development Flask run` to run the developmemt environment
* Run in the terminal `ENVIRONMENT=testing pytest -vs` to run the developmemt environment


### Added

* ENVIRONMENT=development variable in .env file and run it in the terminal

### Changed

N/A

### Fixed

N/A

### Removed

* `vercel_connection.py` file which was using psycopg2 library

-----------------------------------------------------------------------------------------------------------------

## <1.3.0> - <2024-05-08>

### Sprint learnings

* Understanding blueprint architecture
* Modularization with blueprint
* Create a parameter as part of the URL path in `/trajectories/taxi_id`
* Create multiple queries at once with SQLAlchemy
* Use of timedelta an object that represents a duration, the difference between two instants of time.
* Correctly run coverage reports with pytest
* Understanding environment configurations
* Use of request_context() for e2e testing

### Added

* Created `taxi_route.py` and `trajectory_route.py` files into models folder
* create_app() function in `app.py` file and all running the program related code only put into this function

### Changed

* `taxi_model.py` file to `models.py` for both taxis and trajectories models

### Fixed

N/A

### Removed

* /taxis endpoint from `app.py` file to modularize and limit responsabilities

-----------------------------------------------------------------------------------------------------------------

## <1.2.0> - <2024-04-30>

### Sprint learnings

* Understanding MVC arquitecture
* Testing with pytest and fixtures
* Unit testing
* Understanding e2e testing and its difference with unit and integration testing
* The use of conftest file to make fitures global and avoid repeating lines of code.

### Added

* Created an independent test folder (outside the main folder `src`)
* Created the `conftest.py` file
* Created the `test_app.py` file for unit testing
* Created the `test_e2e.py` file for e2e testing

### Changed

N/A

### Fixed

N/A

### Removed

N/A

-----------------------------------------------------------------------------------------------------------------

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