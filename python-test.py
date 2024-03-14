class PythonTest:
    def __init__(self, name):
        self.name = name

    def get_name(self, bom: dict) -> dict:

        return bom
    

if __name__ == '__main__':
    py = PythonTest("Avi")
    bom = {
        "name": "Avi",
        "age": 29
    }

    assert py.get_name(bom) == bom