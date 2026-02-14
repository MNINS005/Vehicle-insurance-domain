from flask import Flask, render_template, request, Response, jsonify
from src.constants import APP_HOST, APP_PORT
from src.pipline.prediction_pipeline import VehicleData, VehicleDataClassifier
from src.pipline.training_pipeline import TrainPipeline

app = Flask(__name__)


# =====================================================
# HOME ROUTE (same as FastAPI GET "/")
# =====================================================
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", context="Rendering")


# =====================================================
# TRAIN ROUTE (same as FastAPI /train)
# =====================================================
@app.route("/train", methods=["GET"])
def train_route():
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
        return Response("Training successful!!!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")


# =====================================================
# PREDICTION ROUTE (same as FastAPI POST "/")
# =====================================================
@app.route("/", methods=["POST"])
def predict():
    try:
        form = request.form

        vehicle_data = VehicleData(
            Gender=form.get("Gender"),
            Age=form.get("Age"),
            Driving_License=form.get("Driving_License"),
            Region_Code=form.get("Region_Code"),
            Previously_Insured=form.get("Previously_Insured"),
            Annual_Premium=form.get("Annual_Premium"),
            Policy_Sales_Channel=form.get("Policy_Sales_Channel"),
            Vintage=form.get("Vintage"),
            Vehicle_Age_lt_1_Year=form.get("Vehicle_Age_lt_1_Year"),
            Vehicle_Age_gt_2_Years=form.get("Vehicle_Age_gt_2_Years"),
            Vehicle_Damage_Yes=form.get("Vehicle_Damage_Yes"),
        )

        # Convert to DataFrame
        vehicle_df = vehicle_data.get_vehicle_input_data_frame()

        # Load prediction pipeline (same as FastAPI)
        model_predictor = VehicleDataClassifier()

        # Predict
        value = model_predictor.predict(dataframe=vehicle_df)[0]
        status = "Response-Yes" if value == 1 else "Response-No"

        return render_template("index.html", context=status)

    except Exception as e:
        return jsonify({"status": False, "error": str(e)})


# =====================================================
# RUN APP
# =====================================================
if __name__ == "__main__":
    app.run(host=APP_HOST, port=APP_PORT, debug=True)
