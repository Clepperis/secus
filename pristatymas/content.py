TEAM = "GEN29 · Secus"

SLIDES = [
  {  # 1 Žmogus ir problema
    "text": [
      "Gyventojams, kurių priedanga – užrakintas daugiabučio rūsys.",
      "Skelbiamas oro pavojus, o durys užrakintos: raktas pas administratorių.",
      "2026 m. spalio 18 d. per oro pavojų Šiauliuose užrakinta liko daugiau nei pusė priedangų (LRT).",
    ],
    "notes": [
      "KALBĖTOJO TEKSTAS (~20 s):",
      "Spalio 18-ąją Šiaulių ir Panevėžio apskrityse paskelbtas oro pavojus. Žmonės bėga į priedangas, o Šiauliuose daugiau nei pusė jų užrakintos. "
      "Raktas pas administratorių, kuris gal darbe, gal atostogose. Tą dieną priedangose pasislėpė vos apie 105 žmonės. "
      "Taisyklės leidžia priedangą paruošti per 12 valandų, o pavojus trunka minutes. Taip žmonės praranda pasitikėjimą ir kitą kartą net neina.",
      "[Nuotraukoje – kadras iš gyventojo vaizdo įrašo (Facebook). Galite pasakyti: „Štai ką nufilmavo gyventojas – užrakintos durys.“]",
      "Šaltiniai: LRT, 2026-10 (lrt.lt/naujienos/lietuvoje/2/3087496); LRT apie 12 val. taisyklę (lrt.lt/naujienos/lietuvoje/2/2935348).",
    ],
  },
  {  # 2 Sprendimas ir prototipas
    "text": [
      "Išmani spyna: per pavojų vienu mygtuku atrakinamos visos rajono priedangos.",
      "Pulto prototipą: pažymi rajoną, patvirtini – ir priedangos atrakintos.",
      "DI padėjo surasti faktus ir kainas bei sukurti paspaudžiamą pulto prototipą.",
    ],
    "notes": [
      "KALBĖTOJO TEKSTAS (~25 s):",
      "Mūsų sprendimas – Secus: išmani spyna ant priedangos durų ir valdymo pultas savivaldybei. "
      "Paskelbus pavojų, operatorius pažymi rajoną arba visą miestą, patvirtina antru paspaudimu – ir visos ten esančios priedangos atsirakina per mažiau nei minutę. "
      "Pultas rodo kiekvienos spynos būseną, bateriją ir ryšį, todėl iš anksto matome, kuri spyna sugedusi. "
      "Spyna veikia nuo ličio baterijų, todėl elektros dingimas jos neišjungia; gamintojai panašioms NB-IoT spynoms nurodo 2–5 metus, o pultas iš anksto įspėja, kada keisti bateriją. Įprastas raktas lieka atsarginis variantas. "
      "[Jei galite – parodykite prototipą gyvai arba nuotrauką.] DI naudojome faktams ir kainoms surinkti bei prototipui sukurti.",
    ],
  },
  {  # 3 Verslo logika
    "text": [
      "Gyventojai – per pavojų; savivaldybės ir VRM – per valdymo pultą.",
      "Savivaldybė spyną ir montavimą perka kartą, o už pultą ir ryšį moka kasmet.",
      "Pilotas Visagine: nedaug priedangų, greitas įdiegimas. Paskui – kitos savivaldybės ir mokyklos.",
    ],
    "notes": [
      "KALBĖTOJO TEKSTAS (~20 s):",
      "Naudotojai – gyventojai, o klientas – savivaldybė, nes būtent savivaldybės atsako už priedangas ir jų prieinamumą. "
      "Modelis: savivaldybė vieną kartą perka spyną ir montavimą, o už pultą ir ryšį moka metinį mokestį – taip pajamos ne vienkartinės. "
      "Paklausa jau yra: Savivaldybių asociacijos prezidentas Audrius Klišonis viešai pasisakė už elektronines spynas priedangose. "
      "Pradėsime nuo Visagino – jis prie Baltarusijos sienos, o gegužę dronų pavojus skelbtas kaimyninėje Ignalinoje. Paskui siūlysime kitoms savivaldybėms, mokykloms ir daugiabučių administratoriams.",
      "Šaltiniai: LRT apie Klišonį (lrt.lt/naujienos/lietuvoje/2/2939320); LRT apie Ignaliną 2026-05-20 (lrt.lt/naujienos/lietuvoje/2/2934077).",
    ],
  },
  {  # 4 Mokymasis ir kitas žingsnis
    "text": [
      "Mentorius patikrino idėją: problema įrodyta, bet vienas klientas – rizika.",
      "Pradedame nuo vienos savivaldybės, o klientais laikome ir mokyklas.",
      "Išbandysime spyną ant tikrų rūsio durų, o pultą – su Visagino savivaldybe. Dar neaišku, ar pirks be įstatymo pakeitimo.",
    ],
    "notes": [
      "KALBĖTOJO TEKSTAS (~20 s):",
      "Idėją kritiškai patikrino mentorius: problemą įvertino kaip įrodytą, bet perspėjo, kad vienas klientas – valstybė – yra rizika. "
      "Todėl pakeitėme planą: pradedame ne nuo visos Lietuvos, o nuo vienos savivaldybės, ir klientais laikome ne tik VRM, bet ir savivaldybes, mokyklas, administratorius. "
      "Tyrinėdami sužinojome, kad elektronines spynas jau svarsto ir kai kurios savivaldybės, todėl mūsų skirtumas – atrakinimas regionais iš vieno pulto ir spynų būsenos stebėjimas. "
      "Kitas žingsnis – išbandyti spyną ant tikrų rūsio durų ir parodyti pultą Visagino savivaldybei. Dar neaišku, ar savivaldybės pirks be įstatymo pakeitimo.",
    ],
  },
  {  # 5 Kiek reikia
    "text": [
      "Apie 10 000 € pilotui: 12 mūsų spynų Visagine ir valdymo pultas.",
      "Spynos 3 600 €, kūrimas 3 000 €, pultas 2 000 €, montavimas ir ryšys 1 000 €.",
      "Apie 3 mėnesius, inžinieriaus mentoriaus, savivaldybės sutikimo ir kibernetinio saugumo patikros.",
    ],
    "notes": [
      "KALBĖTOJO TEKSTAS (~20 s):",
      "Pilotui reikėtų apie 10 000 eurų: 12 mūsų spynų Visagino priedangose ir valdymo pultas. "
      "Viena spyna su NB-IoT ryšio moduliu ir ličio baterijomis kainuotų apie 300 eurų; laidų tiesti nereikia, todėl montavimas pigus. "
      "Pinigai: spynos 3 600, spynos kūrimas ir bandymai 3 000, pultas 2 000, montavimas ir ryšys metams apie 1 000 eurų. "
      "Laiko reikia apie 3 mėnesių, o pagalbos – inžinieriaus mentoriaus, savivaldybės sutikimo ir kibernetinio saugumo patikros, nes nuotoliniu būdu atrakinamos durys turi būti apsaugotos nuo įsilaužimo.",
      "Skaičiavimas (apytikris, mūsų prielaidos): spyna ~300 € × 12 = 3 600 €; kūrimas (prototipai, korpusas, bandymai) ~3 000 €; pultas (serveris, kūrimas, saugumo patikra) ~2 000 €; "
      "montavimas ~40 € × 12 ≈ 500 € + ryšys 12 SIM × ~3 €/mėn. × 12 ≈ 430 € ≈ 1 000 €. Iš viso ~9 600 € ≈ 10 000 €. "
      "Palyginimui: Igloohome išmani spyna (be mobiliojo ryšio) kainuoja 160–300 €.",
    ],
  },
  {  # 6 Komanda
    "text": [
      "[Vardas], [Vardas], [Vardas] – GEN29 komanda.",
      "[Vardas] – tyrimas, [Vardas] – prototipas, [Vardas] – verslo modelis.",
      "[Vardas] susitiks su Visagino savivaldybe. Padėtų kibernetinio saugumo mentorius.",
    ],
    "notes": [
      "KALBĖTOJO TEKSTAS (~15 s):",
      "Mes – komanda GEN29: [vardai]. [Kas ką darė.] "
      "Kitą žingsnį – susitikimą su Visagino savivaldybe – imsis [vardas]. "
      "Labiausiai padėtų kontaktas savivaldybėje ir mentorius iš kibernetinio saugumo srities. Ačiū!",
    ],
  },
]
