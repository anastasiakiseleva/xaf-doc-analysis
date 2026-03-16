---
uid: DevExpress.ExpressApp.IObjectSpace.CustomCommitChanges
name: CustomCommitChanges
type: Event
summary: Replaces the default commit logic with a custom one.
syntax:
  content: event EventHandler<HandledEventArgs> CustomCommitChanges
seealso:
- linkId: DevExpress.ExpressApp.IObjectSpace.Committing
- linkId: DevExpress.ExpressApp.IObjectSpace.Committed
- linkId: DevExpress.ExpressApp.IObjectSpace.ObjectSaving
- linkId: DevExpress.ExpressApp.IObjectSpace.ObjectSaved
---
The [IObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.IObjectSpace.CommitChanges) method call raises the **CustomCommitChanges** event. Handle this event to specify custom logic to commit persistent object changes. Set the **CompletedEventArgs.Handled** parameter to **true** to indicate that the commit operation is performed.

[!include[<CustomCommitChanges>](~/templates/do-commit-remark.md)]

[!include[<40-45><50-54>](~/templates/os_committing_committed_customcommitchanges_reloaded.md)]