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
        missionsCompleted  = agent_func.check_and_get_num( input("enter missionsCompelted times "))
        return (secret_name,name,location,status,missionsCompleted)

    @staticmethod
    def check_and_get_num(input_):
        while True:
            try:
                return (int(input_))
            except:
                print(f"must enter a number this:{input_} not a number")
                input_ = input()
