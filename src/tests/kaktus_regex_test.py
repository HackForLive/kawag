"""
A simple regex test example for kaktus watch dog notifications

note: export PYTHONPATH, 
e.g. [print(msg.encode('utf-16', 'surrogatepass').decode('utf-16')) for msg in messages]
"""
import unittest
from src.kaktus_regex import find_date, find_hour_range


class TestKaktusRegex(unittest.TestCase):
    """Include test cases on a given kaktus messages"""

    def setUp(self):
        self.messages: list[str] = [
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
                "na Facebooku",
            "Stačí dnes 11. 7. naladit 200 - 500 kaček mezi 16 a 19 hodinou a Kaktus ti nabrnkne" + 
            " 2x takovej nářez.🔥",
            "Dobij si dnes 19. 9. mezi 17 a 20 hodinou 200 - 500 korun a získej dvojitou nálož " + 
            "kreditu 💸, než tahle past sklapne.",
            "Dobij dnes 13. 9. mezi 17 a 19 hodinou 200 až 500 Kč a my ti nasolíme 🧂 tuplovanou" +
            " sumu, ani nemrkneš. 🦾🌵",
            "Podráždi ho 2 až 5 stovkama dneska 21. 8. mezi 16 a 18 hodinou a my už ti píchnem," +
            " aby byl 2x takovej. 🐝",
            "Stačí si dneska 12. 10. dobít 2 až 5 stovek mezi 16. a 19. hodinou a vytasit pořádný" +
            " eso v podobě ✌🏻 dvojitýho kreditu."
        ]
        self.dates_expected = [
            (20, 4),
            (11, 4),
            (21, 6),
            (11, 1),
            (9, 6),
            (26, 10),
            (11, 7),
            (19, 9),
            (13, 9),
            (21, 8),
            (12, 10)
        ]
        self.hours_expected = [
            (18, 21),
            (17, 20),
            (17, 19),
            (16, 19),
            (17, 20),
            (18, 20),
            (16, 19),
            (17, 20),
            (17, 19),
            (16, 18),
            (16, 19)
        ]
        # [print(msg.encode('utf-16', 'surrogatepass').decode('utf-16')) for msg in self.messages]

    def test_case_for_dates(self):
        for idx, message in enumerate(self.messages):
            match_date = find_date(message=message)[0]

            self.assertIsNotNone(match_date)
            print(match_date)
            self.assertAlmostEqual(int(match_date[0]), self.dates_expected[idx][0])
            self.assertAlmostEqual(int(match_date[1]), self.dates_expected[idx][1])

    def test_case_for_hours(self):
        for idx, message in enumerate(self.messages):
            match_date = find_hour_range(message=message)
            self.assertNotEqual(match_date, [])
            match_date = match_date[0]

            self.assertIsNotNone(match_date)
            print(match_date)
            self.assertAlmostEqual(int(match_date[0]), self.hours_expected[idx][0])
            self.assertAlmostEqual(int(match_date[1]), self.hours_expected[idx][1])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestKaktusRegex)
    unittest.TextTestRunner(verbosity=2).run(suite)
