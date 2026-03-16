---
uid: DevExpress.ExpressApp.BaseObjectSpace.CommitChanges
name: CommitChanges()
type: Method
summary: Saves all the changes made to the persistent objects belonging to the current Object Space to the database.
syntax:
  content: public void CommitChanges()
seealso: []
---
> [!TIP]
> See [IObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.IObjectSpace.CommitChanges) for a code example.

When working with persistent objects, the changes that you make are not saved immediately. Each object change is tracked. To save all the tracked changes, the **CommitChanges** method is called. This method calls a protected virtual **DoCommit** method, which must be implemented in the **BaseObjectSpace** class' descendants.

After the **CommitChanges** method is executed, the track list is empty and the [BaseObjectSpace.IsModified](xref:DevExpress.ExpressApp.BaseObjectSpace.IsModified) property is set to **false**. This raises the [BaseObjectSpace.ModifiedChanged](xref:DevExpress.ExpressApp.BaseObjectSpace.ModifiedChanged) event.

In default scenarios, this method is automatically called. But all custom manipulations that you perform with persistent objects must be saved manually via this method.

The following events related to this method are available:

* [BaseObjectSpace.Committing](xref:DevExpress.ExpressApp.BaseObjectSpace.Committing)
    
    Handle this event to prevent the commit operation performed by the **CommitChanges** method. For this purpose, set the handler's **CancelEventArgs.Cancel** parameter to **true**.
* [BaseObjectSpace.CustomCommitChanges](xref:DevExpress.ExpressApp.BaseObjectSpace.CustomCommitChanges)
    
    To perform a custom commit instead of a default one, handle the [BaseObjectSpace.CustomCommitChanges](xref:DevExpress.ExpressApp.BaseObjectSpace.CustomCommitChanges) event. Set the **HandledEventArgs.Handled** property to **true** to indicate that the commit operation has been already performed.
* [BaseObjectSpace.Committed](xref:DevExpress.ExpressApp.BaseObjectSpace.Committed)
    
    To perform custom actions after committing object changes, handle the [BaseObjectSpace.Committed](xref:DevExpress.ExpressApp.BaseObjectSpace.Committed) event.

> [!NOTE]
> An Object Space is supposed to commit only the objects that were created with its help. Otherwise, an exception must be raised. This must be implemented in the protected virtual **CheckLocking** method of the **BaseObjectSpace** class's descendants.