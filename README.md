# Clovece
### Zadanie ulohy
Naprogramujte terminálové "Človeče nehnevaj sa!". 
Môžte si upraviť pravidlá. Odporúčané úpravy (zjednoduženia): po hodení 6-ky hrač nehádže ešte raz, po obkrúžení kolečka panáčikovia nejdu do "domčeka", ale sa točia daľej (teda domček ani neexistuje). Program taktiež nemusí byť úplne user friendly. 
Aktuálny stav hry má byť uložený ako jedna imutable premenná, a referencia na tento stav má byť v podstate jedinou "verejnou" mutovatelnou premennou v programe. To samozrejme neznamená, že v kóde nemajú byť mutable premenné, takéto premenné však majú existovať iba v lokálnom scope. 
Súčasťou odovzdaného repozitára má byť základná používateľská dokumentácia, stručný popis designu a aspoň základné testovacie programy. 
Ako si napríklad máte predstaviť terminálové človeče

###Popis Designu

#####Subory

######main.py
Hlavny subor obsahuje Objekt State, ktory vzdycky po volani vrati vrati novy objekt State s updatenutymi vecami. <br >
Obsahuje funkcia ako `dice` ktora orby updatejtovanie hracov. <br >
`player_turn` vrati aktualne kolo. <br >
`print_state` vypise aktualny stav Stae objektu. <br >

Podtim uz je len funkcia main, ktora roby obsluhu k uzivatelovi.

######test.py
Testovaci subor, ktory otestuje spravnu funkcnost klasy State.
