from enum import Enum

class AgentStatus(Enum):
    ACTIVE = "Active"
    INJURED = "Injured"
    MISSING = "Missing"
    RETIRED = "Retired"
    DEFAULT =  "Default Status"
    @staticmethod
    def show_agenr_status():
        for s in AgentStatus:
            print(s , end=" , ")
