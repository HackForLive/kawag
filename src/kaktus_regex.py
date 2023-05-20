import re


def find_date(message: str) -> list[str]:
    return re.findall("(\\d+)\\.\\s*(\\d+)\\.", message)


def find_hour_range(message: str) -> list[str]:
    range_match = re.findall("(\\d+)[\\.]?\\s*a\\s*(\\d+)[\\.]?", message)
    if range_match:
        return range_match

    range_match = re.findall("od\\s*(\\d{1,2}):\\d{2}\\s*do\\s*(\\d{1,2}):\\d{2}", message)
    if range_match:
        return range_match

    range_match = re.findall("od\\s*(\\d+)\\s*do\\s*(\\d+)", message)
    if range_match:
        return range_match

    range_match = re.findall("mezi\\s+(\\d+)\\s+a\\s+(\\d+)", message)

    return range_match
