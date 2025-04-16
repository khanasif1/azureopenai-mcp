# MCP with Azure Open AI
This solution demonstrates a Model context Protocol (MCP) implementation using Azure OpenAI, allowing interaction with external services through a chat interface. The system consists of multiple components that work together to process user queries and interact with different services.

<p align="center">
  <img  src="https://github.com/khanasif1/azureopenai-mcp/blob/main/resources/mcp.gif">
</p>

# AI Model Context Protocol with Azure OpenAI

A sophisticated solution that implements an AI Model Context Protocol (MCP) using Azure OpenAI, enabling intelligent communication between a chat interface and distributed services. This architecture demonstrates how to build a context-aware AI system that can route and process requests across multiple specialized services.

## System Architecture

### 1. Core AI Interface (chainlit_app.py)
**Primary Functions:**
- Provides an interactive chat interface using Chainlit
- Maintains conversation context and user session state
- Implements real-time message streaming
- Integrates with Azure OpenAI for intelligent request processing

### 2. Azure OpenAI Context Layer
**Primary Functions:**
- Powers natural language understanding using GPT models
- Maintains contextual awareness across conversations
- Performs intelligent request classification
- Routes queries to appropriate service endpoints
- Implements Azure OpenAI best practices for prompt engineering

### 3. MCP Server: Weather (weather_mcp_server.py)
**Primary Functions:**
- Handles weather-related natural language queries
- Implements weather-specific context processing
- Integrates with external weather APIs
- Provides formatted weather responses with context retention

### 4. MCP Server: File System (file_mcp_server.py)
**Primary Functions:**
- Manages file system operations through natural language
- Implements file operation context processing
- Provides secure file system access
- Returns structured file operation responses

## Technical Architecture Diagram

```
┌─────────────────┐      ┌────────────────────┐
│   User Chat     │      │  Context Manager   │
│   Interface     │◄─────┤   (Chainlit App)   │
└─────────────────┘      └──────────┬─────────┘
                                    │
                         ┌──────────▼─────────┐
                         │   Azure OpenAI     │
                         │ Context Processor  │
                         └──────────┬─────────┘
                                    │
                  ┌────────────────┬┴───────────────┐
                  │                │                │
         ┌────────▼───────┐ ┌─────▼──────┐ ┌──────▼─────┐
         │ Weather Context│ │File Context │ │Future MCP  │
         │     MCP       │ │    MCP     │ │  Services  │
         └────────┬──────┘ └─────┬──────┘ └────────────┘
                  │              │
         ┌────────▼──────┐ ┌────▼───────┐
         │  Weather API  │ │File System │
         │   Service    │ │Operations  │
         └──────────────┘ └────────────┘
```

## Key Features and Capabilities

### Context Management
- Persistent conversation context across services
- Multi-turn dialogue support
- Context-aware response generation
- Service-specific context handlers

### AI Integration
- Azure OpenAI GPT model integration
- Intelligent query understanding
- Natural language processing
- Dynamic prompt engineering

### Service Architecture
- Modular MCP service design
- Scalable microservice architecture
- Independent service deployment
- Extensible service framework

## Implementation Guide

### Prerequisites
- Azure OpenAI Service subscription
- Python 3.8 or higher
- Azure CLI installed
- Weather API credentials
- File system permissions

# Run the solution

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