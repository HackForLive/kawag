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
            " eso v podobě ✌🏻 dvojitýho kreditu.",
            "Stačí si dobít dnes 24. 10. mezi 17. a 19. hodinou 2-5 stovek a my ti z toho uděláme" +
            " dvakrát takovou parádu.",
            "Dobij si dnes 13. 11. mezi 16. a 19 hodinou 2 - 5 stovek a užívej si dvojitej přívod" + 
            "kreditu přímo do tvýho mobilního zařízení.",
            """
1. Tyto Podmínky závazně upravují podmínky,
za nichž společnost T-Mobile Czech Republic
a.s. (dále jen „Operátor”) nabízí svým
zákazníkům předplacené služby Kaktus (dále
jen „Účastníkům”) bonusový kredit při dobití
kreditu (dále jen „Nabídka”).
2. Podmínky jsou uveřejněny na webových
stránkách na adrese www.mujkaktus.cz
Podmínky či jejich část mohou být dále
komunikovány dalšími prostředky, např.
tiskovou inzercí, plakáty, atd. V případě
rozporu mezi zněním Podmínek uveřejněném
na internetu a zněním Podmínek
uveřejněném jiným způsobem je vždy
rozhodující znění uveřejněné na shora
uvedených webových stránkách.
3. V otázkách neupravených v Podmínkách se
přiměřeně užijí ustanovení aktuálních
Všeobecných podmínek předplacené služby
Kaktus, Podmínek zpracování osobních,
identifikačních, provozních a lokalizačních
údajů účastníků (dále společně jen „VPST”),
dále aktuální Ceník služby Kaktus a
ustanovení platného právního řádu České
republiky.
4. Pokud Účastník předplacené služby Kaktus
v níže uvedeném období jednorázově dobije
svůj kredit částkou 200 Kč nebo vyšší, získá
automaticky kredit ve výši 100% \dobité
částky navíc, maximálně však 500 Kč (dále
jen „bonusový kredit”). Nabídku je možné
využít v období od 23. 6. 2025 od 17:00 hod.
do 23. 6. 2025 19:00 hod.
5. Bonusový kredit se čerpá přednostně a je
platný po dobu 30 dnů od data jeho připsání;
nevyčerpaná část bonusového kreditu v této
době bez náhrady propadá.
6. Nabídka není určena pro Účastníky, kteří jsou
podezřelí ze zneužití SIM karty. Žádost o
vrácení standardního kreditu dobíjeného v
rámci Nabídky při ukončení Smlouvy v
případě, kdy byl ze strany Účastníka
vyčerpán především bonusový kredit získaný
za dobití v rámci Nabídky (bez vyčerpání
alespoň poloviny částky, na základě jejíhož
dobití došlo k připsání bonusového kreditu),
je ze strany Operátora považováno za
zneužití procesu dobíjení kreditu či procesu
jeho výplaty dle článku 2. VOP a Operátor je
v takovém případě oprávněn odmítnout
standardní kredit vrátit, případně jej vrátit
jen v poměrné výši.
7. Bonusový kredit není možné využívat
prostřednictvím GSM bran, Audiotexových
služeb a prémiových služeb poskytovaných v
rámci sítě elektronických komunikací
Operátora. V případě, že Účastník poruší
uvedená omezení nebo vznikne podezření z
takového jednání, bude takové chování
Účastníka považováno za zneužití Nabídky,
resp. služeb podle příslušných ustanovení
VPST s právem Operátora okamžitě
Účastníkovi bonusový kredit přidělený dle
této Nabídky odebrat.
8. Operátor si vyhrazuje právo kdykoli v době
trvání této nabídky, ale i v průběhu doby, kdy
bude nabídka Účastníkem využívána,
aktualizovat a měnit podmínky a rozsah této
nabídky. O změnách podmínek bude Operátor
Účastníka informovat v zákonem stanovené
formě.
9. Tyto Podmínky nabývají platnosti a účinnosti
dne 23. 6. 2025.
ODMĚNA ZA RYCHLÉ DOBITÍ
Obchodní podmínky akce odměna za rychlé dobití
k předplacené službě Kaktus


společnosti T-Mobile Czech Republic a.s., se sídlem Tomíčkova 2144/1, 148 00 Praha 4, IČO: 649 49 681,
zapsána do obchodního rejstříku vedeného Městským soudem v Praze, oddíl B, vložka 3787

(dále jen „Podmínky”)
            """
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
            (12, 10),
            (24, 10),
            (13, 11),
            (23, 6)
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
            (16, 19),
            (17, 19),
            (16, 19),
            (17, 19)
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
