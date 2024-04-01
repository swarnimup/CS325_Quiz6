from abc import ABC, abstractmethod
from typing import List

# SRP: Separate classes for User, Activity, ActivityMonitor, DataStorage, and Display

class User:
    pass

class Activity(ABC):
    @abstractmethod
    def collect_data(self):
        pass

class WalkActivity(Activity):
    def collect_data(self):
        pass

class SwimActivity(Activity):
    def collect_data(self):
        pass

class ActivityMonitor:
    def __init__(self, activities: List[Activity], data_storage, display):
        self.activities = activities
        self.data_storage = data_storage
        self.display = display

    def monitor_activities(self):
        for activity in self.activities:
            data = activity.collect_data()
            self.data_storage.store_data(data)
            self.display.update(data)

class DataStorage:
    def store_data(self, data):
        pass

class Display:
    def update(self, data):
        pass

# OCP: Leverage the Observer pattern for extensibility

# LSP: Ensure Activity class and its subclasses adhere to the observer pattern's contracts

# ISP: Define separate interfaces for data collection and display if they have distinct concerns

# DIP: Inject dependencies like DataStorage and Display into ActivityMonitor constructor

# Usage
walk_activity = WalkActivity()
swim_activity = SwimActivity()

data_storage = DataStorage()
display = Display()

activities = [walk_activity, swim_activity]
activity_monitor = ActivityMonitor(activities, data_storage, display)

activity_monitor.monitor_activities()
