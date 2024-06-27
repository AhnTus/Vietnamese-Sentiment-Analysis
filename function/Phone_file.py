class Phone:
    def __init__(self, id=None, phone_name=None, specifications=None, photo=None):
        self._id = id
        self._phone_name = phone_name
        self._photo = photo
        self._specifications = self.parse_specifications(specifications)


    def parse_specifications(self, specifications):
        if specifications !=None:
            specs_list = specifications.strip('[]').split(', ') 
            specs_dict = {
                'CAMERA': specs_list[0],
                'RAM': specs_list[1],
                'Bộ nhớ': specs_list[2],
                'Pin': specs_list[3],
                'Hãng': specs_list[4]
            }
            return specs_dict

    @property
    def getId(self):
        return self._id

    @property
    def getPhoneName(self):
        return self._phone_name

    @property
    def getSpecifications(self):
        return self._specifications

    @property
    def getPhoto(self):
        return self._photo
