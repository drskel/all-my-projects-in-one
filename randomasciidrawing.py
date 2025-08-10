# made by skel67
cat = r"""
 /\_/\   --cat
( o.o ) 
 > ^ <
"""
sun = r"""
    \  |  /    
  `.  \ | /  .'
    `. * .'
  -- ( ☀ ) -- -SUN-
    .' * `.
  .'  / | \  `.
    /  |  \
"""
cup = r"""
   (
    )  
  __|__
 |     |] --cup of coffee
 '-----'
"""
cow = r"""
^__^ 
(oo)\_______
(__)\       )\/\ --cow
    ||----w |
    ||     ||
"""
mask = r"""
  _____
 /     \
| () () | --mask
 \  ^  /
  |||||
  |||||
"""
symbol = r"""
   .-''''-.
 .'  .-.  '.
:  .'   '.  :
: :       : :
: :       : : --symbol
:  '._.'  :  
 '.     .'
   `'''`
"""
letter_A = r"""
      /\
     /  \ --letter A
    / /\ \
   / ____ \
  /_/    \_\
"""
shark = r"""      .            
\_____)\_____
/--v____ __`<   --shark      
        )/           
        '"""
def random_ascii_drawing():
    import random
    drawings = [cat, sun, cup, cow, mask, symbol, letter_A, shark]
    return random.choice(drawings)
if __name__ == "__main__":
    print(random_ascii_drawing())
