# EquiSphere

https://www.prisma.io/
https://prisma-client-py.readthedocs.io/en/stable/

# Run local database
```
docker-compose up -d --build # Run postegres server
```

# Setup environment
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

# Add .env file
```
DATABASE_USERNAME = postgres
DATABASE_PASSWORD = password
DATABASE_PORT = 5433
DATABASE_NAME = equifast
DATABASE_URL= "postgres://${DATABASE_USERNAME}:${DATABASE_PASSWORD}@localhost:${DATABASE_PORT}/${DATABASE_NAME}"

API_PREFIX = "/api"
```

# Add the data models to your database and generate the client
```
prisma db push    # Re-generate for each model udpate
                  # Will generate the complete database at first run
```


# Generate data
```
cd app
python3 -m fake_data.main
```


# Run fastapi server
```

python3 main.py
```

# Generate and apply migrations
```
prisma migrate dev --name <migration_name>
```