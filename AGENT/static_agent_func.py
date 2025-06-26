import Enums

import Enums

class agent_func:
    @staticmethod
    def get_input_for_agent():
        name = input("enter name")
        secret_name = input("enter secret name")
        location  = input( "enter location")
        Enums.AgentStatus.show_agenr_status()
        status  = input("enter status from this (Default if not from this)" )
        missionsCompleted  = int(input("enter missionsCompelted times "))
        return (secret_name,name,location,status,missionsCompleted)
    
    @staticmethod
    def check_and_get_num(input):
        while True:
            try:
                return (int(input))
            except:
                print(f"must enter a number this:{input} not a number")
