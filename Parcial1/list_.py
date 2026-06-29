

from typing import Any, Optional


class List(list):

    __CRITERION_FUNCTION = {}

    def add_criterion (self, criterion_key: str, criterion_function: function) -> None:
        self.__CRITERION_FUNCTION[criterion_key] = criterion_function



    def show (self) -> None:
        for element in self:
            print(element)

    # def search(self, search_value: Any):
    #     for element in self:
    #         if element == search_value:
    #             return True
    #     return False

    def search(self, search_value: Any, criterion:str = None)-> Optional[int]:
        # La lista debe estar ordenada previamente por el criterio de búsqueda para que esta función funcione correctamente
        self.sort_by_criterion(key_criterion=criterion)
        search_criterion = self.__CRITERION_FUNCTION.get(criterion)

        start = 0
        end = len(self) - 1
        middle = (start + end) // 2

        while start <= end:

            if search_criterion is None and not isinstance(search_value, (int, float, str, bool)):
                print("No se pudo determinar criterio de busqueda")
                return None

            value = self[middle]
            criterion_value = search_criterion(value) if search_criterion else value

            if criterion_value == search_value:
                return middle
            elif criterion_value < search_value:
                start = middle + 1
            else:
                end = middle - 1

            middle = (start + end) // 2
    
    def size(self) -> int:
        return len(self)
    
    def delete_value(self, value, criterion=None) -> Optional[Any]:
        
        index = self.search(value, criterion)
        
        return self.pop(index) if index is not None else None

    # ordenar
    def sort_by_criterion(self, key_criterion=None)-> None:
        sort_criterion = self.__CRITERION_FUNCTION.get(key_criterion)
        if sort_criterion:
            self.sort(key=sort_criterion)
        elif self and isinstance(self[0], (int, float, str, bool)):
            self.sort()
        else:
            print("La lista no puede ser ordenada")


#l = List()


# l.append(1)
# l.append(3)
# l.append(0)
# l.append(43)
# l.append(31)
# l.append(13)

# l.sort()

# l.show()

# print(l.size())



