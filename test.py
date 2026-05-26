# 1. We import the blueprint tool
from pydantic import BaseModel

# 2. We define what a 'Server' must look like
class ServerBlueprint(BaseModel):
    name: str
    ram_gb: int

# 3. Let's try to create a proper server matching the blueprint
try:
    my_good_server = ServerBlueprint(name="Web-Server-01", ram_gb=16)
    print("✓ Success! The server matches the blueprint.")
    print(f"Server Name: {my_good_server.name}")
    print(f"Server RAM: {my_good_server.ram_gb} GB")
except Exception as error:
    print(f"✗ Error caught: {error}")