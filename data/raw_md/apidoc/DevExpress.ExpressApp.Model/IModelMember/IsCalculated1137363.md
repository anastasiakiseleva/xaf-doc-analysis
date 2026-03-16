---
uid: DevExpress.ExpressApp.Model.IModelMember.IsCalculated
name: IsCalculated
type: Property
summary: Specifies whether or not the [custom field](xref:113583) is calculated.
syntax:
  content: |-
    [ModelBrowsable(typeof(ModelMemberVisibilityCalculator))]
    bool IsCalculated { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, when the custom field is calculated; otherwise - **false**.'
seealso: []
---
The **IsCalculated** property is visible in the [Model Editor](xref:112582) for custom fields only.

To define a calculated field, set the **IsCalculated** property to **true** and pass the expression used to compute this field value to the [IModelMember.Expression](xref:DevExpress.ExpressApp.Model.IModelMember.Expression) property.

To define a persistent field, set the **IsCalculated** property to **false**. Note that creation of custom persistent fields is allowed at design time only, by default (the **IsCalculated** property is not editable at runtime). To allow end users to add custom persistent fields at runtime, set the static [ModelMemberReadOnlyCalculator.AllowPersistentCustomProperties](xref:DevExpress.ExpressApp.Model.Core.ModelMemberReadOnlyCalculator.AllowPersistentCustomProperties) property to **true**. To allow updating the database schema after a field is added at runtime, set the [XafApplication.DatabaseUpdateMode](xref:DevExpress.ExpressApp.XafApplication.DatabaseUpdateMode) property to **UpdateDatabaseAlways**. A column mapped to the current field will be added to the database table automatically.

> [!NOTE]
> Generally, persistent fields should be added only at design time. It is a bad practice to allow and users to alter the database schema - allow this only as a last resort.