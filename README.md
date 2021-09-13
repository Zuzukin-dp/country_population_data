# Country_population_data
## The service runs through docker-compose, saves country population data to postgres, and displays regional summary data on the screen.
## Also configured FastAPI, Uvicorn, pgAdmin 4. But no tasks implemented

### Uses only one [source](https://statisticstimes.com/demographics/countries-by-population.php) so far - statisticstimes.com

### How I started the services

### 1. Create .env with parameters based on .env.example

### 2. Run in the background and make a build
'docker-compose up -d --build'
### 3. Parse the data and insert into the database
'docker exec -it backend_ca python3 app/get_data.py'
#### or Makefile
'make get_data'
### 4. Displaying information on the screen in accordance with the task
'docker exec -it backend_ca python3 app/print_data.py'
#### or Makefile
'make print_data'

###### plans to screw FastAPI