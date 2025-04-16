# MCP with Azure Open AI

<p align="center">
  <img  src="https://github.com/khanasif1/azureopenai-mcp/blob/main/resources/mcp.gif">
</p>

## Run the solution

- Clone repository

```
    git clone https://github.com/khanasif1/azureopenai-mcp.git
```
- Create a python virtual environment
```
    python -m venv .venv
```
- Activate python virtual environment
``` Windows
    .\.venv\Scripts\Activate.ps1
```
- Install packages
```
    pip install -r requirements.txt
```
- Run  weather server
```
    python .\src\weather_mcp_server.py
```
- Run  file server
```
    python .\src\file_mcp_server.py 
```
- Run chainlit application
```
    chainlit run .\src\chainlit_app.py  
```