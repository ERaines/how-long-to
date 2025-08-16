from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from zoneinfo import ZoneInfo
from dateutil import parser


@dataclass
class CountdownResult:
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

    target_dt = parser.isoparse(target)

    if target_dt.tzinfo is None:
        target_dt = datetime(target_dt.year, target_dt.month,
                             target_dt.day, 0, 0, 0, tzinfo=ZoneInfo(tz))
    else:
        target_dt = target_dt.astimezone(ZoneInfo(tz))

    now = datetime.now(ZoneInfo(tz))
    delta = target_dt - now
    total_seconds = int(delta.total_seconds())
    past = total_seconds < 0
    remaining = abs(total_seconds)

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
