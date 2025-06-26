import AGENT.class_agent
import DAL.DAL_agenst_db as dal
import AGENT.static_agent_func
class agent_dal:
    @staticmethod
    def get_all_agent():
        sql_quari = "SELECT * FROM agents"
        return dal.MainDAL.execute(sql_quari)
    @staticmethod
    def add_agent():
        secret_name ,name ,  loctaion , status , missionsComplete = AGENT.static_agent_func.agent_func.get_input_for_agent()
        new_agent =  AGENT.class_agent.agent(secret_name , name,loctaion,status,missionsComplete)
        sql = "INSERT INTO agents (codeName, realName, location, status, missionsCompleted) VALUES (%s, %s, %s, %s, %s)"
        values = (new_agent.codeName, new_agent.realName, new_agent.location, new_agent.status.value, new_agent.missionsCompleted)
        dal.MainDAL.execute(sql, values)
        print("add  agent sucssefualy")

    @staticmethod
    def remove_agent(by, details):
        sql = f"DELETE FROM agents WHERE {by} = %s"
        dal.MainDAL.execute(sql, (details,))
        print("Remove successfully")


    # def update_s

