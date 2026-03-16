---
uid: DevExpress.ExpressApp.BaseObjectSpace.Committed
name: Committed
type: Event
summary: Raised after saving changes made to persistent objects belonging to the current Object Space to the database.
syntax:
  content: public event EventHandler Committed
seealso:
- linkId: DevExpress.ExpressApp.BaseObjectSpace.Committing
- linkId: DevExpress.ExpressApp.BaseObjectSpace.CustomCommitChanges
---
The **Committed** event is raised after saving persistent object changes to the database as a result of calling the [BaseObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.BaseObjectSpace.CommitChanges) method.