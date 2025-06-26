import DAL.DAL_AGENT_MENU
def show_menu():
    print("\n=== Agent Management System ===")
    print("1. Show all agents")
    print("2. Add a new agent")
    print("3. Update agent")
    print("4. Delete agent")
    print("5. Find agent by ID")
    print("6. Search agents by criteria")
    print("0. Exit")


@staticmethod
def show_agents(agents_list):
    for agent in agents_list:
        print("\n--- Agent Details ---")
        for key, val in agent.items():
            print(f"{key}: {val}")



def show_and_get_colom_name():

    print("id", "codeName", "realName", "location", "status", "missionsCompleted")
    choice = input()
    while choice not in [ "id", "codeName", "realName", "location", "status", "missionsCompleted"]:
        print("must enter one from this")
        print("id ,code_name , realName , location , status , missionsCompelted")
        choice = input()
    return  choice

def menu():
    while True:
        show_menu()
        choice = input()
        if choice == "1":
           resulot =  DAL.DAL_AGENT_MENU.agent_dal.get_all_agent()
           show_agents(resulot)
        elif choice == "2":
            DAL.DAL_AGENT_MENU.agent_dal.add_agent()
        elif choice == "4":

            choice , details = get_from_user_by_colom()
            DAL.DAL_AGENT_MENU.agent_dal.remove_agent(choice,details)

def get_from_user_by_colom():
    choice = show_and_get_colom_name()
    details = input(f"enter  which {choice} ")
    return (choice,details)