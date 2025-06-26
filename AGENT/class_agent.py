import AGENT.static_agent_func
import Enums
class agent:
    def __init__(self , code_name , realName , location , status , missionsCompelted, id  = None):
        self.codeName  = code_name
        self.realName  = realName
        self.location  = location
        self.status  = agent.check_status( status)
        self.missionsCompleted  = AGENT.static_agent_func.agent_func.check_and_get_num(missionsCompelted)
        self.id = id


    @staticmethod
    def check_status(status):
        if isinstance(status, Enums.AgentStatus):
            return status
        try:
            return Enums.AgentStatus(status)
        except :
            print(" if not from  this status = DEFAULT")
            return Enums.AgentStatus.DEFAULT

    def __str__(self):
        return f"Agent: codeName={self.codeName}, realName={self.realName}, location={self.location}, status={self.status.value}, missionsCompleted={self.missionsCompleted}"