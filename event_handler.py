import random_generators as rg
import events

import sys, inspect
class event_handler:
    def __init__(self):
        self.event_log = []
        self.shown_logs = []
        self.id = 0

    def new_event_log(self, log_message, requiresinteract = False, event = None):
        self.event_log.append({"event":event, "message":log_message, "interact":requiresinteract, "id":self.id})
        self.id += 1

    def get_unshown(self):
        out = []
        for event in self.event_log:
            if(not event["id"] in self.shown_logs):
                out.append(event)
                self.shown_logs.append(event["id"])
        return out

    def randevent(self):
        classes = []
        for name, obj in inspect.getmembers(events):
            if(inspect.isclass(obj)):
                classes.append(obj)
        
        event = classes[rg.randint(0, len(classes)-1)]()
        
        return event
        