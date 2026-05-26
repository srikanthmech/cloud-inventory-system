from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# 1. THE DATA VALIDATOR (Pydantic Model)
# This acts like a bouncer at the door. It ensures the data sent to AWS is correct.
class AWSServiceRequest(BaseModel):
    service_name: str = Field(description="The name of the AWS service, e.g., EC2, S3")
    instance_count: int = Field(gt=0, description="Must be a number greater than 0")
    environment: str = Field(description="Must be 'dev', 'staging', or 'prod'")

# 2. THE GET ROUTE (From Week 1)
@app.get("/")
def home():
    return {"status": "Online", "msg": "Welcome to your Week 2 AWS API"}

# 3. THE POST ROUTE (New Week 2 Concept)
# This accepts data, validates it using our 'bouncers' rules, and processes it.
@app.post("/request-service")
def provision_service(request: AWSServiceRequest):
    # Imagine this is where Terraform will eventually plug in!
    total_estimated_cost = request.instance_count * 14.50 
    
    return {
        "message": f"Deployment request received for {request.service_name}.",
        "target_environment": request.environment,
        "status": "Validated & Pending Cloud Launch",
        "monthly_cost_estimate_usd": total_estimated_cost
    }