---
uid: "403631"
title: 'Resolve SessionMixingException: "The object that has been passed belongs to another ObjectSpace. (An error with number 1021 has occurred.)"'
owner: Eugenia Simonova
---
# Resolve SessionMixingException: "The object that has been passed belongs to another ObjectSpace. (An error with number 1021 has occurred.)"

## Scenario

A [View Controller](xref:112621#view-controllers) contains the _AddTaskAction_ [SimpleAction](xref:DevExpress.ExpressApp.Actions.SimpleAction) that implements the following logic:
# [C#](#tab/tabid-csharp)
 
```csharp{5}
private void AddTaskAction_Execute(Object sender, SimpleActionExecuteEventArgs e){  
    IObjectSpace objectSpace = Application.CreateObjectSpace(typeof(Contact));  
    Contact contact = objectSpace.CreateObject<Contact>();  
    Task task = (Task)View.CurrentObject;  
    contact.Tasks.Add(task);  
    e.ShowViewParameters.CreatedView = Application.CreateDetailView(objectSpace, contact, true);  
}
```
***

When XAF executes the _AddTaskAction_ action, the **Session Mixing Exception** is raised:
` _An error with number 1021 has occurred. Error message: The object that has been passed belongs to another ObjectSpace…_`
## Explanation

The XPO [Session/UnitOfWork](xref:DevExpress.Xpo.Session) or XAF [Object Space](xref:113707) is a separate data context. (ObjectSpace wraps the Session/UnitOfWork.) The **Session Mixing Exception** occurs if you try to create a link between two objects from different Sessions or Object Spaces, for example:

* Assign an object to a reference property of an object from another Session (Object Space);
* Add objects from different Sessions (Object Spaces) to one collection;
* Display objects from one Session (Object Space) in a View created in another Session or Object Space.

The code above raises the **Session Mixing Exception** in the _AddTaskAction_Execute_ method on an attempt to add a new _Task_ to the _Contact.Tasks_ collection. The exception is thrown because the _Contact_ object is created in a new ObjectSpace, while the _Task_ instance belongs to the current View Object Space.

## Solutions
### Get An Existing Object from Another Data Context
To avoid the **Session Mixing Exception**, manipulate all related objects within the same data context (the same Session or Object Space).

#### XPO

To get an object from one data context in another data context, perform the steps below:

* Call the [Session.GetKeyValue](xref:DevExpress.Xpo.Session.GetKeyValue(System.Object)) method to get the object ID. 
 
* Use the **GetObjectByKey** or **FindObject** method to get a single saved object from a database.
# [C#](#tab/tabid-csharp)
 
```csharp
object taskKey = ((Task)View.CurrentObject).Session.GetKeyValue(View.CurrentObject);
contact.Tasks.Add(session.GetObjectByKey<Task>(taskKey));
```
***

See the following topic for more information: [Query and Shape Data (XPO)](xref:2034).

#### XAF

In XAF applications, you can use the **IObjectSpace.GetObject** method that accepts an object from another data context. The following example shows how to use the **IObjectSpace.GetObject** method to load an existing _Task_ object (the current View Object Space) to a newly created Object Space.

# [C#](#tab/tabid-csharp)
 
```csharp{5}
private void AddTaskAction_Execute(Object sender, SimpleActionExecuteEventArgs e){  
    IObjectSpace objectSpace = Application.CreateObjectSpace(typeof(Contact));  
    Contact contact = objectSpace.CreateObject<Contact>();  
    Task task = (Task)View.CurrentObject;  
    contact.Tasks.Add(objectSpace.GetObject(task));  
    e.ShowViewParameters.CreatedView = Application.CreateDetailView(objectSpace, contact, true);
}
```
***
See the following topic for details: [Create, Read, Update and Delete Data (XAF)](xref:113711).
### Get A Newly Created Object from Another Data Context

Newly created and unsaved objects cannot be obtained from a database. Use the following techniques to get unsaved objects:

* Load related objects in the new object data context. Use the [View.ObjectSpace](xref:DevExpress.ExpressApp.View.ObjectSpace) property to get the new object data context.

* Create a nested Session (Object Space) that allows you to transfer unsaved objects between a nested data context and its parent. Refer to the following articles for more information:
    -  [Nested Units of Work (XPO)](xref:DevExpress.Xpo.NestedUnitOfWork)
    -  [XPObjectSpace.CreateNestedObjectSpace (XAF)](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.CreateNestedObjectSpace)