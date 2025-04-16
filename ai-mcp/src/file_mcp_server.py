from fastapi import FastAPI, Request
import uvicorn
import os

app = FastAPI()
ROOT_FOLDER = "src"  # your test folder

@app.post("/retrieve")
async def retrieve(request: Request):
    body = await request.json()
    query = body.get("input", "").lower()
    print(f"query: {query}")
    if "files in" in query:
        folder = query.split("files in")[-1].strip()        
        folder_path = os.path.join(ROOT_FOLDER, folder)
        print (f"folder_path1: {os.path.join(ROOT_FOLDER, folder)}")
    else:
        folder_path = ROOT_FOLDER
        print (f"folder_path2: {ROOT_FOLDER}")

    if not os.path.exists(folder_path):
        print (f"folder_path: {folder_path} not found")
        return {"documents": [{"page_content": f"Folder '{folder_path}' not found"}]}
    
    files = os.listdir(folder_path)
    response = f"Files in folder '{folder_path}':\n" + "\n".join(files)
    print(f"Folder tool Called  data:{response}")
    return {"documents": [{"page_content": response}]}

if __name__ == "__main__":
    uvicorn.run(app, port=8002)
