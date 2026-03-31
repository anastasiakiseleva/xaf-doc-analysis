---
uid: "402983"
title: Configure a Many-to-Many Relationship
seealso:
  - linkId: "112701"
  - linkId: "112654"
---
# Configure a Many-to-Many Relationship

This lesson explains how to create a Many-to-Many relationship between two entities and how XAF generates the UI for such relationships.

> [!NOTE]
> Before you proceed, take a moment to review the previous lessons:
> * [](xref:402981)
> * [](xref:404256)

## Step-by-Step Instructions

1. In the _MySolution.Module\Business Objects_ folder, create the `DemoTask` class. Replace the generated class declaration with the code sample below:

   ```csharp
   using DevExpress.ExpressApp.Model;
   using DevExpress.Persistent.Base;
   using DevExpress.Persistent.BaseImpl.EF;
   using DevExpress.ExpressApp.DC;
   using System.Collections.ObjectModel;

   namespace MySolution.Module.BusinessObjects {
       [DefaultClassOptions]
       //Use this attribute to define the name of the objects of this type in the user interface.
       [ModelDefault("Caption", "Task")]
       public class DemoTask : BaseObject {
           public virtual DateTime? DateCompleted { get; set; }

           public virtual String Subject { get; set; }

           [FieldSize(FieldSizeAttribute.Unlimited)]
           public virtual String Description { get; set; }

           public virtual DateTime? DueDate { get; set; }

           public virtual DateTime? StartDate { get; set; }

           public virtual int PercentCompleted { get; set; }

           private TaskStatus status;

           public virtual TaskStatus Status {
               get { return status; }
               set {
                   status = value;
                   if (isLoaded) {
                       if (value == TaskStatus.Completed) {
                           DateCompleted = DateTime.Now;
                       }
                       else {
                           DateCompleted = null;
                       }
                   }
               }
           }

           [Action(ImageName = "State_Task_Completed")]
           public void MarkCompleted() {
               Status = TaskStatus.Completed;
           }

           private bool isLoaded = false;
           public override void OnLoaded() {
               isLoaded = true;
           }

        }
        public enum TaskStatus {
            [ImageName("State_Task_NotStarted")]
            NotStarted,
            [ImageName("State_Task_InProgress")]
            InProgress,
            [ImageName("State_Task_WaitingForSomeoneElse")]
            WaitingForSomeoneElse,
            [ImageName("State_Task_Deferred")]
            Deferred,
            [ImageName("State_Task_Completed")]
            Completed
        }
   }
   ```

2. Add the `Employees` collection property to the `DemoTask` class. This way, you define the first part of the relationship between the `DemoTask` and `Employee` entities:
    
    ```csharp{2,10}
    // ...
    using System.Collections.ObjectModel;

    namespace MySolution.Module.BusinessObjects {
        [DefaultClassOptions]
        //Use this attribute to define the name of the objects of this type in the user interface.
        [ModelDefault("Caption", "Task")]
        public class DemoTask : BaseObject {
            // ...
            public virtual IList<Employee> Employees { get; set; } = new ObservableCollection<Employee>();

        }
        // ...
    }
    ```
    [`ModelDefault`]: xref:DevExpress.ExpressApp.Model.ModelDefaultAttribute


3. Add the `Tasks` collection to the `Employee` class implementation:
    
    ```csharp{2,7}
    // ...
    using System.Collections.ObjectModel;
    //...
    public class Employee : BaseObject {
        public Employee() {
            //...
            public virtual IList<DemoTask> DemoTasks { get; set; } = new ObservableCollection<DemoTask>();
        }
        //...
    }
    ```

    This declaration of the `Tasks` collection property completes the relationship. Now the classes reference each other. 

4. Go to the _MySolution.Module\MySolutionDbContext_ file and add a DbSet of the `Task` type:

     ```csharp
    public class MySolutionEFCoreDbContext : DbContext {
        //...
        public DbSet<DemoTask> DemoTasks { get; set; }

    }
    ```    

5. Run the application. 
  
    In the **Employee** detail view, the application displays the following elements:
    
    * A list of assigned tasks.
    * The **New** button — allows users to add a new assigned task.
    * The **Link** button — allows users to assign the current employee an existing task.
    
   ASP.NET Core Blazor
   
   :   ![|ASP.NET Core Blazor Collection Property in the UI|](~/images/btutor_bmdefcore_lesson5_contact_tasks.png)

   Windows Forms

   :   ![Windows Forms Collection Property in the UI](~/images/employee-task-winforms.png)
    
   You can find the same UI in the **Tasks** detail view.

   ASP.NET Core Blazor
    
   :   ![|ASP.NET Core Blazor Collection Property in the UI|](~/images/btutor_bmdefcore_lesson5_task_conntacts.png)

   Windows Forms

   :   ![Windows Forms Collection Property in the UI](~/images/task-employee-winforms.png)

## Next Lesson

[](xref:402978)
