# Week 1: Core Backend Functionality

## My Goals
By the end of Week 1, I will have a working FastAPI backend that can generate memes using Pillow. I will understand FastAPI basics, SQLAlchemy ORM, and image manipulation.

## What I'm Building
- FastAPI application with basic routing
- SQLAlchemy models for templates and memes
- Meme generation logic with Pillow
- Core API endpoints for meme creation

## Day-by-Day Plan

### Day 1: Project Setup
- Create project structure and virtual environment
- Install FastAPI, Uvicorn, SQLAlchemy
- Create basic FastAPI app with health check endpoint
- Setup environment variables

### Day 2: Database Models
- Setup SQLAlchemy database connection
- Create MemeTemplate and GeneratedMeme models
- Test database operations
- Add sample template data

### Day 3: Meme Generation
- Install Pillow and download Impact font
- Download 5-10 meme template images
- Write meme generation function (add text to images)
- Test text positioning and styling

### Day 4: API Endpoints
- Create Pydantic schemas for validation
- Build GET /api/templates endpoint
- Build POST /api/memes/generate endpoint
- Build GET /api/memes endpoint
- Test all endpoints with FastAPI docs

### Day 5: Testing & Polish
- Add remaining meme templates
- Test generation with different templates
- Fix any bugs or text positioning issues
- Document my progress

## Expected Deliverables
- Working FastAPI server on localhost:8000
- Database with template and meme tables
- Functional meme generation via API
- 5-10 meme templates ready to use

## Key Technologies I'm Learning
- FastAPI: routing, request/response handling
- SQLAlchemy: models, sessions, queries
- Pillow: image opening, text drawing, saving
- Pydantic: data validation

## Success Criteria
I can make a POST request to my API with template_id and text, and receive a generated meme image back.