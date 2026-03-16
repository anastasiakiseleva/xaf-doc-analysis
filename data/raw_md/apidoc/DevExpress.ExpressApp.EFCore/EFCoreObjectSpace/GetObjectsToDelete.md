---
uid: DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.GetObjectsToDelete(System.Boolean)
name: GetObjectsToDelete(Boolean)
type: Method
summary: Returns a collection of persistent objects marked as deleted in a transaction that currently is in progress.
syntax:
  content: public override ICollection GetObjectsToDelete(bool includeParent)
  parameters:
  - id: includeParent
    type: System.Boolean
    description: This parameter does not affect the result. It is added to provide compatibility with [IObjectSpace.GetObjectsToDelete(Boolean)](xref:DevExpress.ExpressApp.IObjectSpace.GetObjectsToDelete(System.Boolean)).
  return:
    type: System.Collections.ICollection
    description: A collection of persistent objects marked as deleted in a transaction that is currently in progress.
seealso: []
---
[!include[BaseObjectSpace.CommitChanges-NoteForMembers](~/templates/BaseObjectSpace.CommitChanges-NoteForMembers.md)]