---
uid: DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.ModifiedObjects
name: ModifiedObjects
type: Property
summary: Returns a collection of objects that are created, modified, or deleted but not committed to the database.
syntax:
  content: public override IList ModifiedObjects { get; }
  parameters: []
  return:
    type: System.Collections.IList
    description: The collection of persistent objects that are added, deleted, or modified but not committed to the database.
seealso: []
---
[!include[BaseObjectSpace.CommitChanges-NoteForMembers](~/templates/BaseObjectSpace.CommitChanges-NoteForMembers.md)]