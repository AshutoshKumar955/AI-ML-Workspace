from modules import *

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI(
    title="AI ML Workspace API",
    description="Backend API for AI-Powered ML Workspace",
    version="1.0.0"
)

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "status": "success",
        "message": "AI ML Workspace Backend Running 🚀"
    }

@app.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    # Read CSV
    df = pd.read_csv(file.file)

    return {
        "filename": file.filename,
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": df.columns.tolist(),
        "preview": df.head().to_dict(orient="records")
    }

@app.post("/eda")
async def analyze_dataset(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)

    report = {
        "basic_info": basic_info(df),
        "column_summary": col_summary(df),
        "missing_analysis": missing_values(df),
        "duplicate_analysis": duplicate_values(df),
        "invalid_value_analysis": invalid_values(df),
        "numerical_statistics": numerical_statistics(df),
        "categorical_statistics": categorical_statistics(df),
        "datetime_statistics": datetime_statistics(df),
        "outlier_analysis": check_outliers(df),
        "correlation_analysis": check_correlation(df),
        "distribution_analysis": distribution_analysis(df),
        "kurtosis_analysis": kurtosis(df),
    }

    return report
