from fastapi import FastAPI, Request
from lib.devices import Devices
from lib.ip import get_client_ip

app = FastAPI()


@app.get("/api/v1/check")
async def root(request: Request):
    client_ip = get_client_ip(request)
    devices: Devices = app.state.devices
    devices.update_device_status(client_ip, True)
    return {"status": True}


@app.get("/api/v1/get/devices")
async def get_devices():
    devices: Devices = app.state.devices
    return {"devices": devices.get_devices()}
