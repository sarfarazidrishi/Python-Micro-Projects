from plyer import notification
import time

if __name__ == "__main__":
    while True:
        notification.notify(
            title="remember you don't have to stop",
            message="""they are ahead of you: don't give up. work hard, don't be distracted. she might be interested. the goal it to.......""",
            # app_icon="Untitled.jpg",
            timeout=5,
        )
        time.sleep(10)