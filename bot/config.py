import os


class Config:
    API_ID = int(os.environ.get("11333800"))
    API_HASH = os.environ.get("e1b9a48abe756df09de3cc456975b481")
    BOT_TOKEN = os.environ.get("8341647231:AAHdL0nJoSD_IBzQIZOvIojrId802t4SzMs")
    SESSION_NAME = os.environ.get("SESSION_NAME", ":memory:")
    LOG_CHANNEL = int(os.environ.get("-1002410328884"))
    DATABASE_URL = os.environ.get("mongodb+srv://Strange:Strange@cluster0.wpvqktw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    AUTH_USERS = [int(i) for i in os.environ.get("AUTH_USERS", "6505906100").split(" ")]
    MAX_PROCESSES_PER_USER = int(os.environ.get("MAX_PROCESSES_PER_USER", 2))
    MAX_TRIM_DURATION = int(os.environ.get("MAX_TRIM_DURATION", 600))
    TRACK_CHANNEL = int(os.environ.get("TRACK_CHANNEL", False))
    SLOW_SPEED_DELAY = int(os.environ.get("SLOW_SPEED_DELAY", 5))
    HOST = os.environ.get("HOST", "")
    TIMEOUT = int(os.environ.get("TIMEOUT", 60 * 30))
    DEBUG = bool(os.environ.get("DEBUG"))
    WORKER_COUNT = int(os.environ.get("WORKER_COUNT", 20))
    IAM_HEADER = os.environ.get("IAM_HEADER", "")

    COLORS = [
        "white",
        "black",
        "red",
        "blue",
        "green",
        "yellow",
        "orange",
        "purple",
        "brown",
        "gold",
        "silver",
        "pink",
    ]
    FONT_SIZES_NAME = ["Small", "Medium", "Large"]
    FONT_SIZES = [30, 40, 50]
    POSITIONS = [
        "Top Left",
        "Top Center",
        "Top Right",
        "Center Left",
        "Centered",
        "Center Right",
        "Bottom Left",
        "Bottom Center",
        "Bottom Right",
    
