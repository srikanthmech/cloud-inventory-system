
from sqlmodel import SQLModel, Field, create_engine, Session

# 1. Define our table structure
class CloudServerTable(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    server_name: str
    ram_gb: int

# 2. Create the Database File
# This line tells Python to create a local database file named 'cloud_inventory.db'
sqlite_file_name = "cloud_inventory.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url)

print("Creating database and tables...")
SQLModel.metadata.create_all(engine) # This physically builds the file
print("✓ Database file created successfully!")

# 3. Let's save a piece of data into it!
# A 'Session' is like opening a door to the database, walking in, and closing it when done.
with Session(engine) as session:
    # Create a new row using our Python blueprint
    new_server = CloudServerTable(server_name="Production-App-01", ram_gb=64)
    
    session.add(new_server) # Stage the row in the database
    session.commit()        # Hit the 'Save' button permanently
    print(f"✓ Successfully saved '{new_server.server_name}' to the database file!")
    print("Current Cloud Servers in Inventory:")
    servers = session.query(CloudServerTable).all() # Fetch all rows from the table
    for server in servers:
        print(f" - {server.server_name} ({server.ram_gb} GB RAM)")