#!/bin/bash
# Start Portfolio Project Manager and open in browser

echo "🚀 Starting Portfolio Project Manager..."

cd "$(dirname "$0")"

# Start the Flask app in the background
python3 project_manager.py &
SERVER_PID=$!

# Wait for server to start
echo "⏳ Waiting for server to start..."
sleep 3

# Open the browser
echo "🌐 Opening browser..."
if command -v xdg-open > /dev/null; then
    xdg-open http://localhost:5000
elif command -v gnome-open > /dev/null; then
    gnome-open http://localhost:5000
elif command -v firefox > /dev/null; then
    firefox http://localhost:5000 &
elif command -v google-chrome > /dev/null; then
    google-chrome http://localhost:5000 &
elif command -v chromium-browser > /dev/null; then
    chromium-browser http://localhost:5000 &
else
    echo "📝 Please open http://localhost:5000 in your browser"
fi

echo ""
echo "✅ Portfolio Project Manager is running!"
echo "📝 Access at: http://localhost:5000"
echo "🛑 Press Ctrl+C to stop the server"
echo ""

# Wait for the Flask process
wait $SERVER_PID

