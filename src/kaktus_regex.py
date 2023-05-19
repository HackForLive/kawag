import re


def find_date(message: str) -> list[str]:
    return re.findall("(\\d+)\\.\\s*(\\d+)\\.", message)


def find_range(message: str) -> list[str]:
    range_match = re.findall("(\\d+)\\.\\s*a\\s*(\\d+)\\.", message)

    if range_match is not None:
        return range_match
    range_match = re.findall("(\\d+):\\d+.+(\\d+):\\d+", message)

    if range_match is not None:
        return range_match
    range_match = re.findall("od.+(\\d+).+do.+(\\d+)", message)

    if range_match is not None:
        return range_match
    range_match = re.findall("mezi.+(\\d+)\\.?.+a.+(\\d+)\\.?", message)

    return range_match
