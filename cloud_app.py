from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Field, create_engine, Session, select

# ==========================================
# 1. THE ENGINE & DATABASE SETUP
# ==========================================
# Create the Database File
# This line tells Python to create a local database file named 'cloud_inventory.db'
sqlite_file_name = "cloud_inventory.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url)

app = FastAPI(title="AWS Cloud Inventory Manager")

# This code runs automatically ONLY when the web server starts up
@app.on_event("startup")
def on_startup():
    # Ensure our database table is physically built on the hard drive
    SQLModel.metadata.create_all(engine)

# ==========================================
# 2. THE BLUEPRINT / TABLE SCHEMA
# ==========================================
class CloudServer(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    server_name: str
    ram_gb: int
    environment: str  # e.g., 'dev', 'prod'

# ==========================================
# 3. THE API INTERACTION ROUTES
# ==========================================

# ROUTE A: Welcome Home
@app.get("/")
def home():
    return {"message": "Cloud Asset API is active. Go to /docs to play!"}

# ROUTE B: Create & Save a Server (POST)
@app.post("/servers")
def create_server(server_data: CloudServer):
    # Open the database door using a Session
    with Session(engine) as session:
        # Step 1: Stage the incoming data matching our blueprint
        session.add(server_data)
        # Step 2: Hit the permanent save button
        session.commit()
        # Step 3: Refresh the variable to get the auto-generated ID from the database
        session.refresh(server_data)
        
        return {"status": "Success", "saved_asset": server_data}

# ROUTE C: Read All Saved Servers (GET)
@app.get("/servers")
def get_all_servers():
    with Session(engine) as session:
        # Ask the database: "Select all rows from the CloudServer table"
        statement = select(CloudServer)
        results = session.exec(statement).all()
        return {"total_count": len(results), "inventory": results}
    
# (HTTPException is already imported at the top from fastapi)

# ROUTE D: Fetch a single server by its ID
@app.get("/servers/{server_id}")
def get_single_server(server_id: int):
    with Session(engine) as session:
        # Look up the server directly by its primary key ID
        server = session.get(CloudServer, server_id)
        
        # ERROR HANDLING: If the ID doesn't exist, don't let Python crash!
        if not server:
            raise HTTPException(status_code=404, detail=f"Server with ID {server_id} not found.")
            
        return {"status": "Found", "server": server}

# ROUTE E: Delete a server from inventory
@app.delete("/servers/{server_id}")
def delete_server(server_id: int):
    with Session(engine) as session:
        server = session.get(CloudServer, server_id)
        
        # ERROR HANDLING: Can't delete what isn't there
        if not server:
            raise HTTPException(status_code=404, detail=f"Cannot delete. ID {server_id} does not exist.")
            
        session.delete(server) # Mark for removal
        session.commit()       # Finalize the deletion on disk
        return {"status": "Deleted", "message": f"Server {server_id} successfully removed."}