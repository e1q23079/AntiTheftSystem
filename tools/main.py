import logging
import os
import threading

import uvicorn
from dotenv import load_dotenv
from lib.devices import Devices
from lib.loader import Loader
from server.monitor import monitor_loop
from server.server import app

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


load_dotenv()


DISCORD_WEBHOOK_URL = os.getenv("WEB_HOOK_URL")


def main():
    """
    Main function to start the application.
    """
    logger.info("Loading devices from devices.json...")
    loader = Loader("devices.json")
    json_data = loader.get_devices()
    if json_data is None:
        logger.error("Failed to load devices from devices.json. Please check the file.")
        return
    devices = Devices(json_data)
    logger.info("Devices loaded successfully.")
    logger.info("Starting the server...")
    thread = threading.Thread(
        target=monitor_loop,
        args=(
            DISCORD_WEBHOOK_URL,
            devices,
        ),
        daemon=True,
    )
    thread.start()

    app.state.devices = devices
    uvicorn.run(app=app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    """
    Entry point for the application.
    """
    main()
