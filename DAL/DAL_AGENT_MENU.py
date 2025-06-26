import AGENT.class_agent
import  DAL_agenst_db as dal
import AGENT.static_agent_func
class agent_dal:
    @staticmethod
    def get_all_agent():
        sql_quari = "SELECT * FROM agents"
        return dal.MainDAL.execute(sql_quari)
    @staticmethod
    def add_agent():
        new_agent =  AGENT.class_agent.agent(AGENT.static_agent_func.agent_func.get_input_for_agent())
        sql = f"INSERT INTO agents (codeName, realName, location, status, missionsCompleted) VALUES ({new_agent.codeName}, {new_agent.realName}, {new_agent.location}, {new_agent.status}, {new_agent.missionsCompleted});"
        dal.MainDAL.execute(sql)
        print("add  agent sucssefualy")

agent_dal.add_agent()
print(agent_dal.get_all_agent())
