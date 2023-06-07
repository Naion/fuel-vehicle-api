from fastapi import APIRouter
from config.db import conn
from schemas.car import carMaker, carMakers, carModel, carModels, carEntity, carsEntity

car = APIRouter()

@car.get('/cars')
def car_makers():
    return carMakers(conn.vehicles.car_makers.find())

@car.get('/{name}')
def car_maker(name: str):
    return carMaker(conn.vehicles.car_makers.find_one({"name": name}))

@car.get('/cars/{maker}')
def car_models(maker: str):
    return carModels(conn.vehicles.car_models.find({"maker": maker}))

@car.get('/cars/{maker}/{model}')
def car_Entity(maker: str, model: str):
    return carModel(conn.vehicles.car_models.find_one({"maker": maker, "model": model}))