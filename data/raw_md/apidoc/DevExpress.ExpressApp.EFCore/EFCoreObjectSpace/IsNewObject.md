---
uid: DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.IsNewObject(System.Object)
name: IsNewObject(Object)
type: Method
summary: Indicates whether a specified object is created but not saved to the database.
syntax:
  content: public override bool IsNewObject(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: A object this method checks.
  return:
    type: System.Boolean
    description: '**true** if a specified object is created but not saved to the database; otherwise, **false**.'
seealso: []
---
When you use the [BaseObjectSpace.CreateObject](xref:DevExpress.ExpressApp.BaseObjectSpace.CreateObject(System.Type)) method or built-in [Actions](xref:112622) (for example, **New**) to create new objects, these objects are not saved to the database immediately. To save them, call the [BaseObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.BaseObjectSpace.CommitChanges) method or use corresponding built-in Actions (for example, **Save**). The **IsNewObject** method returns **true** until you save an object created within the current Object Space to the database. This method returns **false** after you save this object or if the specified object does not belong to the current Object Space.