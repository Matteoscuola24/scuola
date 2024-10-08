class Orario:
    
    def __init__(self):
        self.lunes = {
            '1ra': 'ing',
            '2na': 'ale',
            '3ra': 'mat',
            '4ta': 'plas',
            '5ta': 'F.Q.',
            '6ta': 'tut'
        }
        self.martes = {
            '1ra': 'tec',
            '2na': 'G.H.',
            '3ra': 'F.Q.',
            '4ta': 'mat',
            '5ta': 'plas',
            '6ta': 'cas'
        }
        self.miercoles = {
            '1ra': 'G.H.',
            '2na': 'tec',
            '3ra': 'cat',
            '4ta': 'F.Q.',
            '5ta': 'cas',
            '6ta': 'ang'
        }
        self.jueves = {
            '1ra': 'mat',
            '2na': 'A.E.',
            '3ra': 'cas',
            '4ta': 'E.F.',
            '5ta': 'cat',
            '6ta': 'ale'
        }
        self.viernes = {
            '1ra': 'G.H.',
            '2na': 'cat',
            '3ra': 'E.F.',
            '4ta': 'ang',
            '5ta': 'tec',
            '6ta': 'plas'
        }
    
    def ora(self):
        dia = input('de que dia quieres saber la hora')
        
        if dia == 'lunes':
            hora = input('de que ora quieres saber el orario, ej. 1ra, 2na...')
            if hora == '1ra':
                print(self.lunes['1ra'])
            elif hora == '2na':
                print(self.lunes['2na'])
            elif hora == '3ra':
                print(self.lunes['3ra']) 
            elif hora == '4ta':
                print(self.lunes['4ta']) 
            elif hora == '5ta':
                print(self.lunes['5ta']) 
            elif hora == '6ta':
                print(self.lunes['6ta']) 
            else:
                print('hora no valida')
        elif dia == 'martes':
            hora = input('de que ora quieres saber el orario, ej. 1ra, 2na...')
            if hora == '1ra':
                print(self.martes['1ra'])
            elif hora == '2na':
                print(self.martes['2na'])
            elif hora == '3ra':
                print(self.martes['3ra']) 
            elif hora == '4ta':
                print(self.martes['4ta']) 
            elif hora == '5ta':
                print(self.martes['5ta']) 
            elif hora == '6ta':
                print(self.martes['6ta']) 
            else:
                print('hora no valida')
        elif dia == 'miercoles':
            hora = input('de que ora quieres saber el orario, ej. 1ra, 2na...')
            if hora == '1ra':
                print(self.miercoles['1ra'])
            elif hora == '2na':
                print(self.miercoles['2na'])
            elif hora == '3ra':
                print(self.miercoles['3ra']) 
            elif hora == '4ta':
                print(self.miercoles['4ta']) 
            elif hora == '5ta':
                print(self.miercoles['5ta']) 
            elif hora == '6ta':
                print(self.miercoles['6ta']) 
            else:
                print('hora no valida')
        elif dia == 'jueves':
            hora = input('de que ora quieres saber el orario, ej. 1ra, 2na...')
            if hora == '1ra':
                print(self.jueves['1ra'])
            elif hora == '2na':
                print(self.jueves['2na'])
            elif hora == '3ra':
                print(self.jueves['3ra']) 
            elif hora == '4ta':
                print(self.jueves['4ta']) 
            elif hora == '5ta':
                print(self.jueves['5ta']) 
            elif hora == '6ta':
                print(self.jueves['6ta']) 
            else:
                print('hora no valida')
        elif dia == 'viernes':
            hora = input('de que ora quieres saber el orario, ej. 1ra, 2na...')
            if hora == '1ra':
                print(self.viernes['1ra'])
            elif hora == '2na':
                print(self.viernes['2na'])
            elif hora == '3ra':
                print(self.viernes['3ra']) 
            elif hora == '4ta':
                print(self.viernes['4ta']) 
            elif hora == '5ta':
                print(self.viernes['5ta']) 
            elif hora == '6ta':
                print(self.viernes['6ta']) 
            else:
                print('hora no valida')
        else:
            print('este dia no hay cole')
                
            
horario = Orario()
horario.ora()
    
