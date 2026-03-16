---
uid: DevExpress.ExpressApp.IObjectSpace.IsNewObject(System.Object)
name: IsNewObject(Object)
type: Method
summary: Indicates whether a specified object has been created but has not been saved to the database.
syntax:
  content: bool IsNewObject(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: A object to be tested.
  return:
    type: System.Boolean
    description: '**true** if the specified object has not yet been saved to the database; otherwise, **false**.'
seealso:
- linkId: DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.IsNewObject(System.Object)
  altText: EFCoreObjectSpace.IsNewObject(Object)
- linkId: DevExpress.ExpressApp.Xpo.XPObjectSpace.IsNewObject(System.Object)
  altText: XPObjectSpace.IsNewObject(Object)
---
The objects that are created both directly via the [IObjectSpace.CreateObject](xref:DevExpress.ExpressApp.IObjectSpace.CreateObject(System.Type)) method and by means of built-in [Actions](xref:112622) (for example, the New Action) are not saved to the database immediately. They are saved only when the [IObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.IObjectSpace.CommitChanges) method is called, directly or by means of built-in Actions (for example, the Save Action). 

Until an object created within the current Object Space is not saved to the database, the **IsNewObject** method returns `true`. After saving, the **IsNewObject** method returns `false`. It is presumed that this property must return `false` if the object passed as the parameter is not persistent, or if it does not belong to the current Object Space.