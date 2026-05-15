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

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.Data.Filtering
Imports DevExpress.ExpressApp
Imports DevExpress.Persistent.BaseImpl
Imports System
Imports System.Collections.Generic
Imports System.Linq

'...
Public Sub MethodInsideController(ByVal objectSpace As IObjectSpace)
    ' In a ViewController, you can use the View.ObjectSpace property to access the current Object Space
    ' or call the Application.CreateObjectSpace method to create a new Object Space.
    Dim person As Person = objectSpace.FirstOrDefault(Of Person)(Function(p) p.FirstName = "John" AndAlso p.LastName = "Doe")
    If person IsNot Nothing Then
        ' Dim outdatedTasks As IList(Of Task) = objectSpace.GetObjects(Of Task)(CriteriaOperator.Parse("DueDate < ?", DateTime.Now))
        Dim outdatedTasks As IQueryable(Of Task) = objectSpace.GetObjectsQuery(Of Task)().Where(Function(t) t.DueDate < DateTime.Now)
        For Each task As Task In outdatedTasks
            task.AssignedTo = person
        Next
    End If

    objectSpace.CommitChanges()
End Sub
'...

```

***

For more information on ways to access an Object Space in different scenarios, refer to the following help topic: [](xref:113707). To learn about Object Space API, see [Create, Read, Update and Delete Data](xref:113711).