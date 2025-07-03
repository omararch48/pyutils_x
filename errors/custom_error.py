class CustomError(Exception):
    
    def detail_error(self):
        print('custom error')