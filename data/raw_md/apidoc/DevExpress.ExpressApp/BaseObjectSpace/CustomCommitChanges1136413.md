---
uid: DevExpress.ExpressApp.BaseObjectSpace.CustomCommitChanges
name: CustomCommitChanges
type: Event
summary: Replaces the default process for committing changes made to persistent objects with a custom one.
syntax:
  content: public event EventHandler<HandledEventArgs> CustomCommitChanges
seealso: []
---
The **CustomCommitChanges** event is raised as a result of calling the [BaseObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.BaseObjectSpace.CommitChanges) method. Handle this event to provide a custom process for committing the changes made to the current Object Space's persistent objects. Set the handler's **HandledEventArgs.Handled** parameter to **true**, to indicate that the committing operation has been already performed.

As an alternative to this event, you can override the **DoCommit** method in the **BaseObjectSpace** class' descendant.