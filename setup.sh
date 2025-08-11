#!/bin/bash

# FastAPI Virtual Environment Setup Script
# This script creates a virtual environment and installs dependencies

echo "🐍 Setting up FastAPI development environment..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.11+ first."
    exit 1
fi

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "⚡ Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "🔄 Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "✅ Setup complete! 🎉"
echo ""
echo "To start developing:"
echo "1. Activate the virtual environment:"
echo "   source venv/bin/activate"
echo ""
echo "2. Start the development server:"
echo "   python run_local.py"
echo ""
echo "3. When done, deactivate the virtual environment:"
echo "   deactivate"
echo ""
echo "🌐 Your API will be available at: http://localhost:8000"
echo "📖 API docs will be at: http://localhost:8000/docs"
