import os
import time
import random
from azure.iot.device import IoTHubDeviceClient
from dotenv import load_dotenv

# Load environment variables from a local .env file (if present)
load_dotenv()

# Retrieve the connection string securely from environment variables
CONNECTION_STRING = os.getenv("AZURE_IOT_CONNECTION_STRING")

# Validate if the connection string is properly set
if not CONNECTION_STRING:
    raise ValueError(
        "Error: AZURE_IOT_CONNECTION_STRING environment variable is not set. "
        "Please check your .env file or system environment variables."
    )

def main():
    # Create an IoT Hub device client instance from the connection string
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    print("Connecting to Azure IoT Hub...")
    client.connect()
    print("Device connected successfully! Starting telemetry transmission (Press Ctrl+C to stop)...")

    # Starting point for temperature to simulate an increasing trend
    current_temperature = 22.0

    try:
        while True:
            # Simulate natural fluctuations + a slow upward trend (ideal for ML/anomaly tests)
            current_temperature += random.uniform(-0.1, 0.3) 
            temperature = round(current_temperature, 2)
            humidity = round(random.uniform(40.0, 65.0), 2)

            # Create the message payload in JSON format
            payload = f'{{"temperature": {temperature}, "humidity": {humidity}}}'

            # Send the telemetry message to Azure IoT Hub
            client.send_message(payload)
            print(f"Telemetry sent -> Temperature: {temperature}°C, Humidity: {humidity}%")

            # Wait 5 seconds before sending the next batch
            time.sleep(5)

    except KeyboardInterrupt:
        print("\nStopping script by user request...")
    finally:
        # Gracefully shut down the client connection
        client.shutdown()
        print("Disconnected from Azure IoT Hub.")

if __name__ == "__main__":
    main()