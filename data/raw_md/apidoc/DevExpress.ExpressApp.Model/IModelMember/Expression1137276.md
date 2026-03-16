---
uid: DevExpress.ExpressApp.Model.IModelMember.Expression
name: Expression
type: Property
summary: Specifies an expression used to calculate the [custom field](xref:113583) value.
syntax:
  content: |-
    [ModelBrowsable(typeof(ModelMemberVisibilityCalculator))]
    [Required(typeof(ModelMemberRequiredCalculator))]
    string Expression { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string that is an expression used to calculate the field value.
seealso: []
---
The **Expression** property is visible in the [Model Editor](xref:112582) for custom calculated fields only.

To define a calculated field, set the [IModelMember.IsCalculated](xref:DevExpress.ExpressApp.Model.IModelMember.IsCalculated) property to **true** and pass the  [expression](xref:4928) used to compute this field value to the **Expression** property. Click the ellipsis button located to the right of the property value to invoke the [Expression Editor](xref:6212) dialog. In this editor, you can select functions, operators and operands using the editor controls.