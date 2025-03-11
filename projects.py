import pandas as pd
import os
from tasks import *
from notify import project_created_email, project_deleted_email

def finder_DB_projects(cuser):
    project_filename = f"{cuser['Username']}P.csv"
    if os.path.exists(project_filename):
        db_projects = pd.read_csv(project_filename)
        return db_projects
    else:
        db_projects = pd.DataFrame(columns=[
            "Project_Name", "Project_Description", "Project_Manager", "Project_Colaborators", 
            "Project_Dini", "Project_Tini", "Project_Dend", "Project_Tend", "Project_Tasks"
        ])
        db_projects.to_csv(project_filename, index=False)
        return db_projects

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

class Project:
    def __init__(self):
        self.project_Name = ""
        self.project_Description = ""
        self.project_Manager = ""
        self.project_Colaborators = set()  
        self.project_Dini = ""
        self.project_Tini = ""
        self.project_Dend = ""
        self.project_Tend = ""
        self.project_tasks = []

    def add_project(self, db_user, db_project, db_task, cuser):
        print("Add a project!")
        while True:
            self.project_Name = str(input("Project Name: "))
            if self.project_Name not in db_project["Project_Name"].values:
                break
            else:
                print("This project already exists, try another name.")
        
        self.project_Description = str(input("Project Description: "))
        self.project_Manager = cuser["Username"]
        self.project_Dini = str(input("Project Date Initial: "))
        self.project_Tini = str(input("Project Time Initial: "))
        self.project_Dend = str(input("Project Date End: "))
        self.project_Tend = str(input("Project Time End: "))
        
        print("How many tasks do you want to add to the project?")
        qtd_tasks = int(input())
        
        for i in range(qtd_tasks):
            task = choice_task(db_task, db_user, cuser)
            dicio_task = {
                "Task_Name": task["Task_Name"].iloc[0],
                "Task_Priority": task["Task_Priority"].iloc[0],
                "Task_Status": task["Task_Status"].iloc[0],
                "Task_Manager": task["Task_Manager"].iloc[0],
                "Task_Collaborators": task["Task_Colaborators"].iloc[0] if isinstance(task["Task_Colaborators"].iloc[0], str) else "",
                "Task_Type": task["Task_Type"].iloc[0],
            }
            self.project_tasks.append(dicio_task)
            
            if not pd.isna(task["Task_Colaborators"].iloc[0]) and isinstance(task["Task_Colaborators"].iloc[0], str):
                colaborators_list = task["Task_Colaborators"].iloc[0].split(", ")
                self.project_Colaborators.update(colaborators_list)
        
        collaborators_str = ", ".join(self.project_Colaborators)
        tasks_str = str(self.project_tasks)
        
        temp_DB = pd.DataFrame({
            "Project_Name": [self.project_Name],
            "Project_Description": [self.project_Description],
            "Project_Manager": [self.project_Manager],
            "Project_Colaborators": [collaborators_str],
            "Project_Dini": [self.project_Dini],
            "Project_Tini": [self.project_Tini],
            "Project_Dend": [self.project_Dend],
            "Project_Tend": [self.project_Tend],
            "Project_Tasks": [tasks_str]
        })
        
        db_project = pd.concat([db_project, temp_DB], ignore_index=True)
        db_project.to_csv(f"{cuser['Username']}P.csv", index=False)
        
        # Adicionar as tarefas ao banco de dados do gerente
        db_task = pd.concat([db_task, pd.DataFrame(self.project_tasks)], ignore_index=True)
        db_task.to_csv(f"{cuser['Username']}T.csv", index=False)
        
        for collaborator in self.project_Colaborators:
            if collaborator in db_user["Username"].values:
                collaborator_email = db_user[db_user["Username"] == collaborator]["Email"].iloc[0]
                collaborator_name = db_user[db_user["Username"] == collaborator]["Name"].iloc[0]
                collaborator_surname = db_user[db_user["Username"] == collaborator]["Surname"].iloc[0]
                project_created_email(collaborator_email, collaborator_name, collaborator_surname, self.project_Name)
        
        print("Project added successfully!")
        input("Press Enter to continue...")
        clear_terminal()
        
        return db_project

    def delete_project(self, db_project, cuser, db_user):
        print("Delete a project!")
        project_name = input("Type the name of the project you want to delete: ")

        
        if project_name in db_project["Project_Name"].values:
            
            project_to_delete = db_project[db_project["Project_Name"] == project_name].iloc[0]

            
            tasks_str = project_to_delete["Project_Tasks"]
            tasks_list = eval(tasks_str)  

            
            for task in tasks_list:
                
                collaborators = task["Task_Collaborators"].split(", ")

                
                for collaborator in collaborators:
                    collaborator_tasks_file = f"{collaborator}T.csv"
                    if os.path.exists(collaborator_tasks_file):
                        db_collaborator_tasks = pd.read_csv(collaborator_tasks_file)
                        db_collaborator_tasks = db_collaborator_tasks[db_collaborator_tasks["Task_Name"] != task["Task_Name"]]
                        db_collaborator_tasks.to_csv(collaborator_tasks_file, index=False)

            
            collaborators = project_to_delete["Project_Colaborators"].split(", ")
            for collaborator in collaborators:
                collaborator_email = db_user[db_user["Username"] == collaborator]["Email"].iloc[0]
                collaborator_name = db_user[db_user["Username"] == collaborator]["Name"].iloc[0]
                collaborator_surname = db_user[db_user["Username"] == collaborator]["Surname"].iloc[0]
                project_deleted_email(collaborator_email, collaborator_name, collaborator_surname, project_name)

            
            db_project = db_project[db_project["Project_Name"] != project_name]
            
            
            db_project.to_csv(f"{cuser['Username']}P.csv", index=False)
            
            print(f"Project '{project_name}' and all associated tasks deleted successfully!")
        else:
            print(f"Project '{project_name}' not found. Try again.")

        input("Press Enter to continue...")
        clear_terminal()
        return db_project