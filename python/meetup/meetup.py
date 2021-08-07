from datetime import date, timedelta
import calendar


class MeetupDayException(Exception):
    pass


_weekday_by_str = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6,
}


def _number_of_days(year: int, month: int) -> int:
    return calendar.monthrange(year, month)[1]


def _first_date_of(year: int, month: int):
    return date(year, month, 1)


def _last_date_of(year: int, month: int):
    return _first_date_of(year, month) + timedelta(
        days=_number_of_days(year, month) - 1
    )


def _iterate_between_dates(first: date, last: date):
    date = first
    # forward iteration
    if first < last:
        while date <= last:
            yield date
            date += timedelta(days=1)
    # reverse iteration
    else:
        while date >= last:
            yield date
            date -= timedelta(days=1)


def _find_weekday_occurrence(
    first: date, last: date, weekday: int, weekday_occur: int = 1
):
    cnt = 0
    for d in _iterate_between_dates(first, last):
        if d.weekday() == weekday:
            cnt += 1
        if cnt == weekday_occur:
            return d
    raise MeetupDayException(f"Incorrect meetup date!")


def meetup(year: int, month: int, week: str, weekday_str: str) -> date:
    weekday = _weekday_by_str[weekday_str]

    if week in ("1st", "2nd", "3rd", "4th", "5th"):
        return _find_weekday_occurrence(
            _first_date_of(year, month),
            _last_date_of(year, month),
            weekday,
            int(week[0]),
        )
    elif week == "last":
        return _find_weekday_occurrence(
            _last_date_of(year, month), _first_date_of(year, month), weekday
        )
    elif week == "teenth":
        return _find_weekday_occurrence(
            date(year, month, 13), date(year, month, 19), weekday
        )

    raise MeetupDayException(f"Incorrect meetup date!")
