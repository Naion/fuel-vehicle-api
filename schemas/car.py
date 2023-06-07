def carMaker(item) -> dict:
    return{
        "name": item["name"]
    }

def carMakers(cars) -> list:
    return [carMaker(item) for item in cars]

def carModel(item) -> dict:
    return{
        "maker": item["maker"],
        "model": item["model"]
    }

def carModels(cars) -> list:
    return [carModel(item) for item in cars]

def carEntity(item) -> dict:
    return{
        "maker": item["maker"],
        "model": item["model"],
        "gpa": item["gpa"]
    }

def carsEntity(cars) -> list:
    return [carEntity(item) for item in cars]