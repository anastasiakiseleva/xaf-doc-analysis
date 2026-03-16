---
uid: DevExpress.ExpressApp.Editors.ListEditor.ErrorMessages
name: ErrorMessages
type: Property
summary: Provides access to the current [](xref:DevExpress.ExpressApp.Editors.ListEditor)'s error message collection, populated when [Validation Rules](xref:113008) are broken.
syntax:
  content: public ErrorMessages ErrorMessages { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Utils.ErrorMessages
    description: An **ErrorMessages** object which is used to access the messages about currently broken Validation Rules.
seealso: []
---
Validation Rules can be applied to a business class. When these Rules are broken, the **ErrorMessages** collection of the [List Editor](xref:113189) that represents this class' object(s)  is populated with the error messages.

Generally, you do not need to use this property. Although, you may use it in a custom feature for the Validation System.