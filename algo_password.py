import string, random
from xml.dom.minidom import CharacterData

class password:
    def __init__(self,use_app,password_size):
        self.use_app = use_app
        self.password_size = password_size
        self.my_password = self.password_gen(password_size)

    def password_gen (self,size):
        password_res = ""
        for i in range (size):
            j = random.randint(0,1)
            if j == 0:
                password_res = password_res + random.choice(string.ascii_letters)
            else :
                password_res = password_res + str(random.randint(0,9))
        return password_res

#password1 = password("spotify",-8) <--- mettre des conditions d'erreurs 
#print(password1.my_password) <----- Appeler la class et non la fonction (sinon class inutile)