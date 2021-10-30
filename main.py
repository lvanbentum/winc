# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# initialiseren variabelen
scorer_0='Ruud Gullit'
goal_0 = 32
scorer_1='Marco van Basten'
goal_1 = 54
#genereren string met scorende spelers en tijdstippen
scorers=scorer_0+' '+str(goal_0)+', '+scorer_1+' '+str(goal_1)
print(scorers)
#initialiseren vaiuabelen voor report string
tekst_0=' scored in the '
tekst_1= 'nd minute'
tekst_2='th minute'
#genereren report
report=f"{scorer_0}{tekst_0}{goal_0}{tekst_1}\n{scorer_1}{tekst_0}{goal_1}{tekst_2}"
print(report)
# Gekozen voor Ruud Gullit als speler om overige strings op aan te maken
player="Ruud Gullit"
first_name=player[:player.find('Gullit')-1]
print(first_name)
last_name_len=len(player)-player.find('Gullit')
print(last_name_len)
name_short=player[:1]+'. '+player[player.find('Gullit'):]
print(name_short)
#tussen variabele met spatie aan het einde
chant1=(first_name+'! ')*len(first_name)
print(chant1,len(chant1))
#chant string aanmaken door laatste letter te verwijderen
chant=chant1[:len(chant1)-1]
print(chant,len(chant))
#controle of laatste letter inderdaad geen spatie is 
good_chant=(chant[:len(chant)-1]!=' ')