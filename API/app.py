from flask import Flask, request, jsonify
from flask_cors import CORS
from core import compute_countdown

# Create Flask application instance
app = Flask(__name__)

# Enable CORS to allow requests from a separate frontend (browser-based clients)
CORS(app)


@app.get("/health")
def health():
    """
    Health-check endpoint.
    Useful for monitoring and confirming that the API is running.
    """
    return {"status": "ok"}


@app.get("/countdown")
def countdown():
    """
    Countdown endpoint.
    Accepts query parameters:
        - date (required): target date (YYYY-MM-DD or ISO8601 string)
        - tz (optional): timezone, default "Europe/Dublin"
        - title (optional): event title, default "Event"

    Example:
        GET /countdown?date=2025-12-25&title=Christmas&tz=UTC
    """
    target = request.args.get("date")
    if not target:
        return jsonify({"error": "missing 'date' query param (YYYY-MM-DD or ISO8601)"}), 400

    tz = request.args.get("tz", "Europe/Dublin")
    title = request.args.get("title", "Event")

    try:
        result = compute_countdown(target, tz=tz, title=title)
    except Exception as e:
        # Return error details if date parsing or timezone fails
        return jsonify({"error": str(e)}), 400

    # Return countdown result as JSON
    return jsonify({
        "title": result.title,
        "target": result.target_iso,
        "now": result.now_iso,
        "timezone": result.tz,
        "total_seconds": result.total_seconds,
        "past": result.past,
        "breakdown": {
            "days": result.days,
            "hours": result.hours,
            "minutes": result.minutes,
            "seconds": result.seconds
        },
        "message": (
            f"{'Elapsed' if result.past else 'Remaining'} "
            f"{result.days}d {result.hours}h {result.minutes}m {result.seconds}s "
            f"{'since' if result.past else 'until'} {result.title}"
        )
    })


@app.get("/")
def root():
    """
    Friendly root route so hitting "/" is helpful instead of 404.
    """
    return {
        "name": "how-long-to API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "countdown": "/countdown?date=YYYY-MM-DD&tz=Europe/Dublin&title=Event"
        }
    }, 200


if __name__ == "__main__":
    # Run development server (do not use in production!)
    app.run(port=8000, debug=True)
