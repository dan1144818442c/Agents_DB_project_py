import Enums
class agent:
    def __init__(self , code_name , realName , location , status , missionsCompelted, id  = None):
        self.codeName  = code_name
        self.realName  = realName
        self.location  = location
        self.status  = status
        self.missionsCompleted  = missionsCompelted
        self.id = id

    @staticmethod
    def chek_status(status):
        try:
            return Enums.AgentStatus(status)
        except:
            # ךהדפיס שהוגדר DEFAULT STATUS
            return Enums.AgentStatus.DEFAULT


