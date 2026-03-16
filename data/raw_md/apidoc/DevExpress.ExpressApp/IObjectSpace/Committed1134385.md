---
uid: DevExpress.ExpressApp.IObjectSpace.Committed
name: Committed
type: Event
summary: Occurs after persistent object changes are stored in the database.
syntax:
  content: event EventHandler Committed
seealso:
- linkId: DevExpress.ExpressApp.IObjectSpace.ObjectSaved
- linkId: DevExpress.ExpressApp.IObjectSpace.CustomCommitChanges
---
The **Committed** event is raised after the [IObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.IObjectSpace.CommitChanges) method call.

[!include[<Committed>](~/templates/do-commit-remark.md)]

[!include[<27-29><33-35>](~/templates/os_committing_committed_customcommitchanges_reloaded.md)]
