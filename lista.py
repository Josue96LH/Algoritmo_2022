def criterio_comparacion(value, criterio):
    if isinstance(value, (int, str, bool)):
        return value
    else:
        dic_atributos = value.__dict__
        if criterio in dic_atributos:
            return dic_atributos[criterio]
        else:
            print('no se puede ordenar por este criterio')


class Lista():

    def __init__(self):
        self.__elements = []

    def insert(self, value, criterio=None):
        # print('criterio de insercion', criterio)
        if len(self.__elements) == 0 or criterio_comparacion(value, criterio) >= criterio_comparacion(self.__elements[-1], criterio):
            self.__elements.append(value)
        elif criterio_comparacion(value, criterio) < criterio_comparacion(self.__elements[0], criterio):
            self.__elements.insert(0, value)
        else:
            index = 1
            while criterio_comparacion(value, criterio) >= criterio_comparacion(self.__elements[index], criterio):
                index += 1
            self.__elements.insert(index, value)

    def search(self, search_value, criterio=None):
        position = None
        first = 0
        last = self.size() - 1
        while (first <= last and position == None):
            middle = (first + last) // 2
            if search_value == criterio_comparacion(self.__elements[middle], criterio):
                position = middle
            elif search_value > criterio_comparacion(self.__elements[middle], criterio):
                first = middle + 1
            else:
                last = middle - 1
        return position

    def search_r(self, search_value, first, last, criterio=None):
        middle = (first + last) // 2
        if first > last:
            return None
        elif search_value == criterio_comparacion(self.__elements[middle], criterio):
            return middle
        elif search_value > criterio_comparacion(self.__elements[middle], criterio):
            return self.search_r(search_value, middle+1, last, criterio)
        else:
            return self.search_r(search_value, first, middle-1, criterio)

    def delete(self, value, criterio=None):
        return_value = None
        pos = self.search(value, criterio)
        if pos is not None:
            return_value = self.__elements.pop(pos)
        return return_value

    def size(self):
        return len(self.__elements)

    def barrido(self):
        for value in self.__elements:
            print(value)

    def order_by(self, criterio=None, reverse=False):
        dic_atributos = self.__elements[0].__dict__
        if criterio in dic_atributos:
            def func_criterio(valor):
                return valor.__dict__[criterio]

            self.__elements.sort(key=func_criterio, reverse=reverse)
        else:
            print('no se puede ordenar por este criterio')

    def get_element_by_index(self, index):
        return_value = None
        if index >= 0 and index < self.size():
            return_value = self.__elements[index]
        return return_value

    def set_value(self, value, new_value, criterio=None):
        pos = self.search(value, criterio)
        if pos is not None:
            value = self.delete(value)
            self.insert(new_value, criterio)

    def barrido_anio_buscado(self, anio_buscado):
        print(f'Lista --------{anio_buscado}--------')
        for value in self.__elements:
            if value.anio == anio_buscado:
                print(value)

    def barrido_pjBus(self):
        print('Lista deseado ----------------')
        for value in self.__elements:
            if (value.nombre == 'ahsoka tano' or value.nombre == 'kit fisto'):
                print(value)

    def barrido_aprendices(self):
        print('Lista aprendices Yoda ----------------')
        for value in self.__elements:
            if (value.nombMaestro == 'yoda'):
                print(value.nombre)
        print()
        print('Lista aprendices Luke Skywalker ----------------')
        for value in self.__elements:
            if (value.nombMaestro == 'luke skywalker'):
                print(value.nombre)

    def barrido_hum_twi(self):
        print('Lista human / twi lek ----------------')
        for value in self.__elements:
            if (value.especie == 'human' or value.especie == "twi'lek"):
                print(value)

    def barrido_jedis_a(self):
        print('Lista inician con A ----------------')
        for value in self.__elements:
            if (value.nombre[0] == 'a'):
                print(value)

    def barrido_sables(self):
        print('Lista jedis con multiples sables ----------------')
        for value in self.__elements:
            if (len(value.colorSables) > 1):
                print(value)

    def barrido_sables_aov(self):
        print('Lista sables AoV----------------')
        for value in self.__elements:
            for valor in value.colorSables:
                if valor == 'yellow' or valor == 'purple':
                    print(value)

    def barrido_aprendices_2(self):
        print('Lista aprendices Qui-Gon Jin ----------------')
        for value in self.__elements:
            for valor in value.nombMaestro:
                if (valor == 'qui-gon jin'):
                    print(value)
        print()
        print('Lista aprendices Mace Windu ----------------')
        for value in self.__elements:
            for valor in value.nombMaestro:
                if (valor == 'mace windu'):
                    print(value)
        print('No tiene padawans')
