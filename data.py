import requests
class Data():
    '''class Data to fetch json of question_data from https://opentdb.com/api.php based on parameters:-->None'''
    
    def __init__(self,amount=10, type='boolean', **kwargs):
        '''setup params value for opentdb api call,call fetch_opentdb_data()'''
        self.opentdb_api_parm = {
            'amount':amount,
            'type':type
        }
        self.opentdb_api_parm.update(kwargs)
        self.question_data = []
        self.fetch_opentdb_data()
        
    def fetch_opentdb_data(self):
        '''get question_data through api call to opentdb passing opentdb_api_parm:-->None'''
        # todo:get questions through opentdb api by passing parameter opentdb_api_parm
        print(f"opentdb api parm:{self.opentdb_api_parm}")
        response = requests.get(url='https://opentdb.com/api.php', params=self.opentdb_api_parm)
        # todo:catch and raise exception for get method
        print(response.raise_for_status())
        # todo:print json response from api call
        # print(f"response.json()['results']:{response.json()['results']}")
        print(f"length of question bank:{len(response.json()['results'])}")
        self.question_data = response.json()['results']