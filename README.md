# Number Classification API

This is a FastAPI-based API that classifies a given number and returns its mathematical properties along with a fun fact.

## Features
- Classifies a number as prime, perfect, Armstrong, even/odd.
- Returns the sum of the digits of the number.
- Fetches a fun fact about the number from [Numbers API](http://numbersapi.com/).

## API Endpoint
- **GET** `/api/classify-number?number=<number>`
  - Example: `/api/classify-number?number=371`
  - Response:
    ```json
    {
        "number": 371,
        "is_prime": false,
        "is_perfect": false,
        "properties": ["armstrong", "odd"],
        "digit_sum": 11,
        "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
    }
    ```

## Deployment
The API is deployed on Render and can be accessed at:
[https://hng-stage-1-backend.onrender.com](https://hng-stage-1-backend.onrender.com)

## Local Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/ericBlack1/HNG-Stage-1-backend.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the API:
   ```bash
   uvicorn main:app --reload
   ```
4. Access the API at `http://127.0.0.1:8000/api/classify-number?number=<number>`.

## Tech Stack
- **Python**
- **FastAPI**
- **Render** (for deployment)

## Testing the Deployed API
Once deployed, test the API using the Render-provided URL. For example:

```
https://hng-stage-1-backend.onrender.com/api/classify-number?number=371
```
