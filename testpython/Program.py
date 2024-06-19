from task import Task
from individualtask import IndividualTask
from repeatedtask import RepeatedTask

# from Task import difficulty
class Program:

    def main():

        print("Please select activity type.")
        print("1. Individual Task")
        print("2. Repeated Task")
        task_type = input("Selection: \n")
        
        title = input("Title: ")
        description = input("Task description: ")
        
        # Requirements
        print("Enter task requirements.")
        requirements = []
        req_next = ""
        count = 0
        while req_next.lower() != "next":
            
            count += 1
            req_next = input(f"{count}. ")
            if req_next != "next":
                requirements.append(req_next)
        #TODO remove the 'next' line in terminal
        assert requirements[len(requirements) - 1] != "next"
        
        #TODO get task difficulty

        #TODO
        if task_type == 1:
            #TODO fill out
            indv_task = IndividualTask(title, )
        if task_type == 2:
            #TODO get frequency
            rep_task = RepeatedTask(title, )


        # # Testing base (Task) class
        # my_list = ["Unload clean dishes.", "Load dirty dishes."]
        # newTask = Task("Dishes", 4, my_list, "Do the dishes.")
        # newTask.Get_Task_Description()

        # newTask.Complete()
        # newTask.Get_Task_Description()

        # # Testing sub (IndividualTask) class
        # my_list = ["Fold socks.", "Put socks in drawer."]
        # individual_task = IndividualTask("Laundry", 1, my_list, "Finish laundry")
        # individual_task.Get_Task_Description()

        # individual_task.Complete()
        # individual_task.Get_Task_Description()
        # if individual_task.isdone == True:
        #     individual_task.Combat(False, "d8", 1)
        #     print(individual_task.Get_Combat_Results())

        # #TODO Test Child classes

    if __name__ == "__main__":
        main()