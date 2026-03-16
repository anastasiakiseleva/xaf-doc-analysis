---
uid: DevExpress.Persistent.BaseImpl.EF.ModelDifference.UserName
name: UserName
type: Property
summary: Gets the name of a user who owns the current [](xref:DevExpress.Persistent.BaseImpl.EF.ModelDifference) object.
syntax:
  content: |-
    [NotMapped]
    public string UserName { get; }
  parameters: []
  return:
    type: System.String
    description: A string which is the name of a user who owns the current model differences.
seealso: []
---
This property value is calculated from the [ModelDifference.UserId](xref:DevExpress.Persistent.BaseImpl.EF.ModelDifference.UserId). When the **UserId** is not specified and the current [](xref:DevExpress.Persistent.BaseImpl.EF.ModelDifference) object specifies the model differences layer shared by all users (administrator model differences), then this property is set to "Shared Model Difference". This text is loaded from the localizable value in the Application Model at **Localization** | **Texts** | **SharedModelDifferenceName**.