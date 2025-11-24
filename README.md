# Bitasmbl-File-Converter-9386af-

## Description
Build a web application that allows users to upload files and convert them between formats, such as PDF to text or images to PNG. The system focuses on simplicity, intuitive UI, and fast conversions without requiring complex setup.

## Tech Stack
- FastAPI
- React
- Tailwind CSS

## Requirements
- Allow users to upload PDF and image files
- Convert PDF documents to text and images to PNG format
- Provide download links for converted files
- Show status updates during conversion (loading/progress)
- Handle unsupported file types and errors gracefully

## Installation
bash
git clone https://github.com/MrBitasmblTester/Bitasmbl-File-Converter-9386af-.git
cd Bitasmbl-File-Converter-9386af-
 

## Backend
bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload


## Frontend
bash
cd frontend
npm install
npm start


## Usage
1. Open the frontend in a browser.
2. Upload a PDF or image file.
3. Wait for conversion and download the result.

## Implementation Steps
1. Set up FastAPI server for file upload and response handling.
2. Implement PDF-to-text conversion logic.
3. Implement image-to-PNG conversion logic.
4. Store converted files temporarily and expose download URLs.
5. Build React UI for upload, status display, and download links.
6. Style components using Tailwind CSS.
7. Add error handling for unsupported types and failures.

## API Endpoints
- POST /convert
- GET /download/{file_id}