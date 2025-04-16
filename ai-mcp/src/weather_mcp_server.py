from fastapi import FastAPI, Request
import uvicorn
import requests

app = FastAPI()
API_KEY = os.getenv("WEATHER_API_KEY")

@app.post("/retrieve")
async def retrieve(request: Request):
    body = await request.json()
    query = body.get("input", "").lower()

    # Parse city name
    city = query.replace("weather in", "").strip()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url)

    if res.status_code != 200:
        return {"documents": [{"page_content": f"Could not find weather for {city}"}]}

    data = res.json()
    print(f"Weather tool called  data:{data}")
    summary = (
        f"The weather in {city.title()} is {data['weather'][0]['description']} "
        f"with a temperature of {data['main']['temp']}°C, "
        f"humidity {data['main']['humidity']}%, "
        f"and wind speed {data['wind']['speed']} m/s."
    )

    return {"documents": [{"page_content": summary}]}

if __name__ == "__main__":
    uvicorn.run(app, port=8001)
