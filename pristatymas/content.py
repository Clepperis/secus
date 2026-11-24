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
      "Paskelbus pavojų, operatorius pažymi rajoną arba visą miestą, patvirtina antru paspaudimu – ir visos ten esančios priedangos atsirakina per kelias sekundes. "
      "Pultas rodo kiekvienos spynos būseną, bateriją ir ryšį, todėl iš anksto matome, kuri spyna sugedusi. "
      "Dingus elektrai spyna atsirakina pati, o įprastas raktas lieka atsarginis variantas. "
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
      "Apie 10 000 € pilotui – 20 Visagino priedangų (~350 € vienoms durims).",
      "Įranga 4 600 €, montavimas 2 400 €, pultas 2 000 €, ryšys metams 700 €.",
      "Apie 3 mėnesius, elektriko, savivaldybės sutikimo ir kibernetinio saugumo patikros.",
    ],
    "notes": [
      "KALBĖTOJO TEKSTAS (~20 s):",
      "Pilotui 20-yje Visagino priedangų reikėtų apie 10 000 eurų – maždaug 350 eurų vienoms durims. "
      "Skaičiavome pagal rinkos kainas: lietuviškas Teltonika LTE valdiklis – apie 131 €, elektros spyna – nuo 30 iki 113 €, elektrikas – apie 40 € per valandą. "
      "Pinigai: įranga 4 600, montavimas 2 400, pultas 2 000, ryšys metams apie 700 eurų. "
      "Laiko reikia apie 3 mėnesių, o pagalbos – elektriko, savivaldybės sutikimo ir kibernetinio saugumo patikros, nes nuotoliniu būdu atrakinamos durys turi būti apsaugotos nuo įsilaužimo.",
      "Skaičiavimas: durims – valdiklis ~131 € + spyna ~60 € + maitinimas su akumuliatoriumi ~40 € = ~230 € įrangos; montavimas 3 val. × 40 € = 120 €. 20 durų: 4 600 € + 2 400 €. "
      "Pultas (serveris, kūrimas, saugumo patikra) ~2 000 €. Ryšys: 20 SIM × ~3 €/mėn. × 12 = ~720 €. Iš viso ~9 700 € ≈ 10 000 €.",
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
