---
uid: DevExpress.ExpressApp.Validation.IModelLayoutManagerOptionsValidation.RequiredFieldMark
name: RequiredFieldMark
type: Property
summary: Specifies a string appended to an editor label when there is a validation rule demanding that a property should have a value.
syntax:
  content: |-
    [DefaultValue("")]
    string RequiredFieldMark { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string appended to a Property Editor label when the [](xref:DevExpress.Persistent.Validation.RuleRequiredFieldAttribute) rule is applied.
seealso: []
---
By default, the [Template Kit](xref:405447) sets the **RequiredFieldMark** property to '*' (an asterisk symbol).

![RequiredFieldMark](~/images/requiredfieldmark129432.png)

To change the **RequiredFieldMark** value, run the [Model Editor](xref:112582) and navigate to the **Options** | **LayoutManagerOptions** node.

![LayoutManagerOptions_ME](~/images/layoutmanageroptions_me129433.png)

If the **RequiredFieldMark** property is missing, ensure that the [](xref:DevExpress.ExpressApp.Validation.ValidationModule) is added.