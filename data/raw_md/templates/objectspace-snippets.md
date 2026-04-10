# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Data.Filtering;
using DevExpress.ExpressApp;
using DevExpress.Persistent.BaseImpl;
using System;
using System.Collections.Generic;
using System.Linq;

//...
public void MethodInsideController(IObjectSpace objectSpace) {
    // In a ViewController, you can use the View.ObjectSpace property to access the current Object Space
    // or call the Application.CreateObjectSpace method to create a new Object Space.
    Person person = objectSpace.FirstOrDefault<Person>(p => p.FirstName == "John" && p.LastName == "Doe");
    if(person != null) {
        // IList<Task> outdatedTasks = objectSpace.GetObjects<Task>(CriteriaOperator.Parse("DueDate < ?", DateTime.Now));
        IQueryable<Task> outdatedTasks = objectSpace.GetObjectsQuery<Task>().Where(t => t.DueDate < DateTime.Now);
        foreach(Task task in outdatedTasks) {
            task.AssignedTo = person;
        }
    }
    objectSpace.CommitChanges();
}
//...
```
***

For more information on ways to access an Object Space in different scenarios, refer to the following help topic: [](xref:113707). To learn about Object Space API, see [Create, Read, Update and Delete Data](xref:113711).