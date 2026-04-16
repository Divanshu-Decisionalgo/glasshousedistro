#!/usr/bin/env bash
set -euo pipefail

PORT=${PORT:-3000}
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Pick an available server
if command -v python3 &>/dev/null; then
    echo "Starting Glass House Distro at http://localhost:$PORT"
    echo "Press Ctrl+C to stop."
    cd "$DIR"
    python3 -m http.server "$PORT"
elif command -v npx &>/dev/null; then
    echo "Starting Glass House Distro at http://localhost:$PORT"
    echo "Press Ctrl+C to stop."
    npx serve "$DIR" -l "$PORT"
elif command -v php &>/dev/null; then
    echo "Starting Glass House Distro at http://localhost:$PORT"
    echo "Press Ctrl+C to stop."
    php -S "localhost:$PORT" -t "$DIR"
else
    echo "Error: no suitable server found. Install Python 3, Node.js, or PHP." >&2
    exit 1
fi
