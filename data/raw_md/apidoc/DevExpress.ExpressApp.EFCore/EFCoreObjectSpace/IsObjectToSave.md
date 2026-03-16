---
uid: DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.IsObjectToSave(System.Object)
name: IsObjectToSave(Object)
type: Method
summary: Checks if the specified object is changed and whether or not it should be saved to a database.
syntax:
  content: public override bool IsObjectToSave(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: An object this method checks.
  return:
    type: System.Boolean
    description: '**true** if the specified object is changed and whether or not it should be saved to a database; **false** if the object has not been modified since the last commit.'
seealso: []
---
[!include[BaseObjectSpace.CommitChanges-NoteForMembers](~/templates/BaseObjectSpace.CommitChanges-NoteForMembers.md)]