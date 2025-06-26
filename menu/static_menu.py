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
            id = int(input("enter id "))
            DAL.DAL_AGENT_MENU.agent_dal.remone_agent_by_id(id)


