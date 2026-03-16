---
uid: DevExpress.ExpressApp.Model.Core.ModelMemberReadOnlyCalculator.AllowPersistentCustomProperties
name: AllowPersistentCustomProperties
type: Property
summary: Specifies whether or not creating [custom persistent fields](xref:113583) at runtime is allowed.
syntax:
  content: public static bool AllowPersistentCustomProperties { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, when creating custom persistent fields at runtime is allowed; otherwise - **false**.'
seealso: []
---
By default, creation of custom persistent fields is allowed only at design time (the [IModelMember.IsCalculated](xref:DevExpress.ExpressApp.Model.IModelMember.IsCalculated) property is readonly and set to true by default at runtime). To allow end users to add custom persistent fields at runtime, set the **AllowPersistentCustomProperties** property to **true**. To allow updating the database schema at runtime, set the [XafApplication.DatabaseUpdateMode](xref:DevExpress.ExpressApp.XafApplication.DatabaseUpdateMode) property to [DatabaseUpdateMode.UpdateDatabaseAlways](xref:DevExpress.ExpressApp.DatabaseUpdateMode.UpdateDatabaseAlways). A column mapped to the current field will be added to the database table automatically.
> [!NOTE]
> Generally, persistent fields are supposed to be added only at design time. It is a bad practice to allow end users to alter the database schema - allow this only as a last resort.