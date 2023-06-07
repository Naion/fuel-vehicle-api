from fastapi import APIRouter
from config.db import conn
from schemas.car import carMaker, carMakers, carModel, carModels, carEntity, carsEntity

car = APIRouter()

@car.get('/{maker}')
def car_maker(maker: str):
    return carMaker(conn.vehicles.car_maker.find({"name": maker}))

@car.get('/cars')
def car_makers():
    return carMakers(conn.vehicles.car_makers.find())

@car.get('/cars/{maker}')
def car_models(maker: str):
    return carModels(conn.vehicles.car_models.find({"maker": maker}))

@car.get('/cars/{maker}_{model}')
def car_Entity(maker: str, model: str):
    return carModel(conn.vehicles.car_models.find({"maker": maker, "model": model}))