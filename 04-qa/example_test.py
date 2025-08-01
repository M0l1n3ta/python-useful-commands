import unittest
from utility import make_request

class MyTest(unittest.TestCase):

    def test_search_asteroids_with_sucess(self):
        # Arrange:
        query_parameters = {}
        # Act:
        response = make_request(query_parameters)
        # Assertion:
        assert response.status_code == 200  # Validation of status code
        data = response.json()
        # Assertion of body response content:
        assert len(data) > 0
        assert data["element_count"] == 167
    
    def test_search_asteroids_in_valid_range(self):
        # Arrange:
        params = {"start_date":"2024-09-01","end_date":"2024-09-08"}
        #Act:
        response = make_request(params)
        #Assertion:
        assert response.status_code == 200  # Validation of status code  
        data = response.json()  
        # Assertion of body response content:  
        assert len(data) > 0  
        assert data["element_count"] == 178

if __name__ == '__main__':
    unittest.main()