import re

messages: list[str] = [
    "Zasaď dneska 20. 4. 200 - 500 kaček mezi 18 a 21 hodinou a nech svůj kredit" +
        " \uD83C\uDF31 rozkvést do dvojnásobný velikosti.",
    "Stačí dnes 11. 4. dobít mezi 17 a 20 hodinou 200 - 500 kaček a" +
        " tvá porce volání, sms a dat poroste jak 🍄 po dešti.",
    "Když pořídíš kredit za 2 až 5 stovek dneska 21. 6. mezi " +
        "17. a 19. hodinou, vyznamenáme tě 2x takovym kreditem. \uD83C\uDF35",
    "Ukážeme ti pořádný kouzla ⚡️ Stačí, když si dneska 11. 1. od 16 do 19 hodin dobiješ " +
        "za 2 až 5 stovek a objeví se ti dvakrát takovej kredit. Kredity na " +
        "tebe! \uD83C\uDF35 Sdílet na Facebooku",
    "Dobij si dneska 9. 6. od 17:00 do 20:00 "+
        "mezi 2 - 5 kilama a smlsni si na dvojnásobnym kreditu. \uD83E\uDD60",
    "Postačí, když si dneska 26. 10. dobiješ mezi 18. a 20. hodinou za 2 až 5 kil, tak" +
        " datování, zprávám i volání můžeš dát pěkně do těla. \uD83C\uDF35 Sdílet " +
        "na Facebooku"
]

dates_expected = [
    (20, 4),
    (11, 4),
    (21, 6),
    (11, 1),
    (9, 6),
    (26, 10)
]

hours_expected = [
    (18, 21),
    (17, 20),
    (17, 19),
    (16, 19),
    (17, 20),
    (18, 20)
]

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


[print(msg.encode('utf-16', 'surrogatepass').decode('utf-16')) for msg in messages]
[print(find_date(msg)) for msg in messages]
[print(find_range(msg)) for msg in messages]
