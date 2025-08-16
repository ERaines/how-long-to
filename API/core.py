from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from zoneinfo import ZoneInfo
from dateutil import parser


@dataclass
class CountdownResult:
    """
    Structured result returned by compute_countdown().
    It represents the countdown breakdown for a given target date.
    """
    title: str
    target_iso: str
    now_iso: str
    tz: str
    total_seconds: int
    days: int
    hours: int
    minutes: int
    seconds: int
    past: bool


def compute_countdown(target: str, tz: str = "Europe/Dublin", title: str = "Event") -> CountdownResult:
    """
    Compute the countdown (days, hours, minutes, seconds) until a given target date.

    Args:
        target (str): Target date string. Can be "YYYY-MM-DD" or full ISO8601 (e.g., 2025-12-31T23:59:59Z).
        tz (str): Timezone identifier (IANA database, e.g., "UTC", "Europe/Dublin").
        title (str): Title/label for the countdown event.

    Returns:
        CountdownResult: Object containing the countdown breakdown and metadata.
    """
    # Parse the input string into a datetime object
    target_dt = parser.isoparse(target)

    # If no timezone is provided, assume midnight in the given timezone
    if target_dt.tzinfo is None:
        target_dt = datetime(target_dt.year, target_dt.month,
                             target_dt.day, 0, 0, 0, tzinfo=ZoneInfo(tz))
    else:
        # Convert target date to the requested timezone
        target_dt = target_dt.astimezone(ZoneInfo(tz))

    # Current time in the same timezone
    now = datetime.now(ZoneInfo(tz))

    # Time delta between target and now
    delta = target_dt - now
    total_seconds = int(delta.total_seconds())

    # If the date is in the past
    past = total_seconds < 0
    remaining = abs(total_seconds)

    # Breakdown into days, hours, minutes, seconds
    days = remaining // 86400
    hours = (remaining % 86400) // 3600
    minutes = (remaining % 3600) // 60
    seconds = remaining % 60

    return CountdownResult(
        title=title,
        target_iso=target_dt.isoformat(),
        now_iso=now.isoformat(),
        tz=tz,
        total_seconds=total_seconds,
        days=days,
        hours=hours,
        minutes=minutes,
        seconds=seconds,
        past=past,
    )
