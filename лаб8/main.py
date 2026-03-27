class Calendar:
    def __init__(self):
        self.events = []

    def add_event(self, time, title):
        new_event = {"time": time, "title": title}
        self.events.append(new_event)
        
        self.events.sort(key=lambda x: x["time"])
        print(f"Note '{title}' added on {time}.")

    def edit_event(self, index, new_time, new_title):
        try:
            if 0 <= index < len(self.events):
                old_title = self.events[index]["title"]
                self.events[index] = {"time": new_time, "title": new_title}
                self.events.sort(key=lambda x: x["time"]) 
                print(f"Note '{old_title}' changed on '{new_title}' ({new_time}).")
            else:
                print("Error: Note with this key already exists")
        except IndexError:
            print("Error: wrong index")

    def show_calendar(self):
        print("\n--- Calendar ---")
        if not self.events:
            print("No events")
        else:
            for i, event in enumerate(self.events):
                print(f"{i}. [{event['time']}] - {event['title']}")

def main():
    my_calendar = Calendar()

    my_calendar.add_event("12:00", "Afternoon")
    my_calendar.add_event("09:00", "Morning") 
    my_calendar.add_event("18:00", "Chill")

    my_calendar.show_calendar()

    print("Editing note 1")
    my_calendar.edit_event(1, "13:00", "Zoom meeting")

    my_calendar.show_calendar()

if __name__ == "__main__":
    main()