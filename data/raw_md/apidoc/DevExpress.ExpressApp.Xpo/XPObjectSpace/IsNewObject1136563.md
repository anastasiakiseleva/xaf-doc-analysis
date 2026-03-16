---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.IsNewObject(System.Object)
name: IsNewObject(Object)
type: Method
summary: Indicates whether a specified object has been created but has not been saved to the database.
syntax:
  content: public override bool IsNewObject(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: A object to be tested.
  return:
    type: System.Boolean
    description: '**true** if the specified object has not been yet saved to the database; otherwise, **false**.'
seealso: []
---
The objects that are created both directly via the [BaseObjectSpace.CreateObject](xref:DevExpress.ExpressApp.BaseObjectSpace.CreateObject(System.Type)) method and by means of built-in [Actions](xref:112622) (e.g. the New Action) are not saved to the database immediately. They are saved only when the [BaseObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.BaseObjectSpace.CommitChanges) method is called, directly or by means of the built-in Actions (e.g. the Save Action). Until an object created within the current Object Space is not saved to the database, the **IsNewObject** method returns **true**. After saving, the **IsNewObject** method returns **false**. In addition, it returns **false**, if the object passed as the parameter is not persistent, or if it does not belong to the current Object Space.