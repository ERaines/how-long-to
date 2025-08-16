from flask import Flask, request, jsonify
from flask_cors import CORS
from core import compute_countdown

app = Flask(__name__)
CORS(app)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/countdown")
def countdown():
    target = request.args.get("date")
    if not target:
        return jsonify({"error": "missing 'date' query param (YYYY-MM-DD or ISO8601)"}), 400

    tz = request.args.get("tz", "Europe/Dublin")
    title = request.args.get("title", "Event")

    try:
        result = compute_countdown(target, tz=tz, title=title)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

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
            f"{'Passaram' if result.past else 'Faltam'} "
            f"{result.days}d {result.hours}h {result.minutes}m {result.seconds}s "
            f"{'desde' if result.past else 'para'} {result.title}"
        )
    })


if __name__ == "__main__":
    app.run(port=8000, debug=True)
