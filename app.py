from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, PlainTextResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import uvicorn
import os

from src.constants import APP_HOST, APP_PORT
from src.pipline.prediction_pipeline import (
    VehicleData,
    VehicleDataClassifier
)
from src.pipline.training_pipeline import TrainPipeline


app = FastAPI()

# Templates folder
templates = Jinja2Templates(directory="templates")


# =====================================================
# HOME ROUTE (GET "/")
# =====================================================
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "context": "Rendering"
        }
    )


# =====================================================
# TRAIN ROUTE (GET "/train")
# =====================================================
@app.get("/train")
async def train_route():
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
        return PlainTextResponse("Training successful!!!")

    except Exception as e:
        return PlainTextResponse(f"Error Occurred! {str(e)}")


# =====================================================
# PREDICTION ROUTE (POST "/")
# =====================================================
@app.post("/", response_class=HTMLResponse)
async def predict(
    request: Request,
    Gender: str = Form(...),
    Age: str = Form(...),
    Driving_License: str = Form(...),
    Region_Code: str = Form(...),
    Previously_Insured: str = Form(...),
    Annual_Premium: str = Form(...),
    Policy_Sales_Channel: str = Form(...),
    Vintage: str = Form(...),
    Vehicle_Age_lt_1_Year: str = Form(...),
    Vehicle_Age_gt_2_Years: str = Form(...),
    Vehicle_Damage_Yes: str = Form(...)
):
    try:
        vehicle_data = VehicleData(
            Gender=Gender,
            Age=Age,
            Driving_License=Driving_License,
            Region_Code=Region_Code,
            Previously_Insured=Previously_Insured,
            Annual_Premium=Annual_Premium,
            Policy_Sales_Channel=Policy_Sales_Channel,
            Vintage=Vintage,
            Vehicle_Age_lt_1_Year=Vehicle_Age_lt_1_Year,
            Vehicle_Age_gt_2_Years=Vehicle_Age_gt_2_Years,
            Vehicle_Damage_Yes=Vehicle_Damage_Yes,
        )

        # Convert to DataFrame
        vehicle_df = vehicle_data.get_vehicle_input_data_frame()

        # Load prediction pipeline
        model_predictor = VehicleDataClassifier()

        # Predict
        value = model_predictor.predict(dataframe=vehicle_df)[0]
        status = "Response-Yes" if value == 1 else "Response-No"

        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "context": status
            }
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "status": False,
                "error": str(e)
            }
        )


# =====================================================
# RUN APP
# =====================================================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=True
    )