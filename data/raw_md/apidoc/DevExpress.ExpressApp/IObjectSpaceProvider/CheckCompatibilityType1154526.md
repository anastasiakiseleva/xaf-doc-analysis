---
uid: DevExpress.ExpressApp.IObjectSpaceProvider.CheckCompatibilityType
name: CheckCompatibilityType
type: Property
summary: Specifies how the database and application compatibility is checked.
syntax:
  content: CheckCompatibilityType? CheckCompatibilityType { get; set; }
  parameters: []
  return:
    type: System.Nullable{DevExpress.ExpressApp.CheckCompatibilityType}
    description: A `Nullable\<`[](xref:DevExpress.ExpressApp.CheckCompatibilityType)`>` enumeration value specifying how the database and application compatibility is checked.
seealso: []
---
This property allows you to specify the mode individually for each Object Space Provider (in case you u[se multiple databases](https://supportcenter.devexpress.com/ticket/details/e4896/how-to-connect-different-data-models-to-several-databases-within-a-single-application))

`CheckCompatibilityType` is set to `null` and the [XafApplication.CheckCompatibilityType](xref:DevExpress.ExpressApp.XafApplication.CheckCompatibilityType) property value is actually used. Refer to this property description to learn more on available values.
