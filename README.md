# ASDT week 5

# Koodin ajaminen

- Create a new virtual environment
```sh
# macOS/Linux
python3 -m venv .venv

# Windows
python -m venv .venv
```
- Activate the virtual environment
```sh
# macOS/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

- Install the required packages
```sh
pip install -r requirements.txt
```

## Part 1

-luo tkinterillä ratkaisu, joka havainnollistaa vasempaan reunaan aution saaren ja toiseen reunaan asutun mantereen
 
-luo toiminto, jolla Ernesti pystyy lähettämään apinan uimaan kohti manteretta saaren pohjoispäästä sadan pienen askelen verran (yksi ”askel” kuvaa aina jokaista uitua kilometriä) ja havainnollista tämän uinti käyttöliittymässä parhaaksi katsomallasi tavalla
 
-luo vastaavasti toiminto, jolla Kernesti pystyy myös lähettämään apinan uimaan kohti manteretta samalla tavalla kuin Ernestinkin, mutta saaren eteläpäästä

## Part 2

-luo toiminto, joka määrittelee apinan, jolle on opetettu yksi sana Ernestin ja Kernestin luomasta hätäviestistä
 
-luo toiminto säikeistystä (threading) käyttäen, jolla Ernesti voi lähettää yksittäisen apinan mukanaan yksi sana kohti manteretta. Ilmaise sopivalla äänimerkillä uimaääniä jokaisen "kilometrin" kohdalla. Ja, mikäli apina pääsee perille, ilmaise tämä sopivalla äänimerkillä.
 
-luo vastaava toiminto Kernestille apinan lähettämistä varten

## Part 3

-luo apinan uintimatkaan toiminto, jossa joka ilmentää sitä, että jokaisella kuljetulla kilometrillä apinalla on noin prosentin todennäköisyys tulla syödyksi. Säädä tätä "syödyksi tulemisen riskiprosenttia" siten, että noin puolet lähetetyistä apinoista pääsee perille. Mikäli hai syö apinan, luo uintimatkaan tätä ilmentävä ääniefekti
 
-määritä Ernesti lähettämään 10 apinaa saarelta mantereelle, samoin määritä Kernesti tekemään sama. Tarkkaile ja varmista visuaalisesti, pääseekö lähetetyistä apinoista noin puolet perille.

## Part 4

-luo mantereelle sen pohjoispäähän säikeistystä hyödyntäen satamavahdit, jotka tarkkailevat rantaan saapuvia apinoita. Nimeä satamavahdit Pohteriksi ja Eteteriksi. Pohteri tarkkailee mantereella pohjoispäässä Ernestin lähettämiä apinoita ja Eteteri vastaavasti mantereen eteläpäässä. Heti kun toinen havaitsee, että saapuneessa viestissä on yli 10 erilaista sanaa, hän osaa tulkita hätäviestin ja lähettää evakuointilaivan saarelle (joko sen eteläpäähän tai pohjoispäähän) 

-havainnollista evakuointilaivan saapuminen autiolle saarelle ja ilmaise joko Ernestin tai Kernestin riemu siitä, että juuri hän sai hätäviestin menemään ensimmäisenä perille!

## Part 5

-tee laskelma ja vertailu kummassa päässä manteretta oli isommat juhlat, kun yhdestä apinasta riittää perunoiden kera tarjottuna syötävää neljälle?

-ja laske kuinka paljon mustapippuria molemmissa juhlissa kuluu yhteensä

### Resepti

- 1 apina
- 2 kg perunoita
- 3 dl kuohukermaa
- 2 tl mustapippuria
- 1 tl suolaa
