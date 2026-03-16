---
uid: DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.GetObjectsToSave(System.Boolean)
name: GetObjectsToSave(Boolean)
type: Method
summary: Returns a collection of persistent objects that are added, deleted, or modified in a transaction that is currently in progress.
syntax:
  content: public override ICollection GetObjectsToSave(bool includeParent)
  parameters:
  - id: includeParent
    type: System.Boolean
    description: This parameter does not affect the result. It is added to provide compatibility with [IObjectSpace.GetObjectsToSave(Boolean)](xref:DevExpress.ExpressApp.IObjectSpace.GetObjectsToSave(System.Boolean)).
  return:
    type: System.Collections.ICollection
    description: The collection of persistent objects that are added, deleted, or modified in a transaction that currently is in progress.
seealso: []
---
[!include[BaseObjectSpace.CommitChanges-NoteForMembers](~/templates/BaseObjectSpace.CommitChanges-NoteForMembers.md)]