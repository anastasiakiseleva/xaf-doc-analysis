---
uid: DevExpress.ExpressApp.IModelDifference.UserName
name: UserName
type: Property
summary: Gets the name of a user who owns the current [](xref:DevExpress.ExpressApp.IModelDifference) object.
syntax:
  content: string UserName { get; }
  parameters: []
  return:
    type: System.String
    description: A string which is the name of a user who owns the current model differences.
seealso:
- linkId: "403527"
---
In classes that implement [](xref:DevExpress.ExpressApp.IModelDifference), this property value is calculated from the [IModelDifference.UserId](xref:DevExpress.ExpressApp.IModelDifference.UserId). When the **UserId** is not specified and the current [](xref:DevExpress.ExpressApp.IModelDifference) object specifies the model differences layer shared by all users (administrator model differences), then this property is set to "Shared Model Difference". This text is loaded from the localizable value in the Application Model at **Localization** | **Texts** | **SharedModelDifferenceName**.