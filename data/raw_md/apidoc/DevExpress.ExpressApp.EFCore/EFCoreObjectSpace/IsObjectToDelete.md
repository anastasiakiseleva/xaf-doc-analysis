---
uid: DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.IsObjectToDelete(System.Object)
name: IsObjectToDelete(Object)
type: Method
summary: Checks whether or not the specified object is marked as deleted but still exists in the database.
syntax:
  content: public override bool IsObjectToDelete(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: The persistent object this method checks.
  return:
    type: System.Boolean
    description: '**true**, if the specified object is marked as deleted but still exists in the database; otherwise, **false**.'
seealso: []
---
[!include[BaseObjectSpace.CommitChanges-NoteForMembers](~/templates/BaseObjectSpace.CommitChanges-NoteForMembers.md)]