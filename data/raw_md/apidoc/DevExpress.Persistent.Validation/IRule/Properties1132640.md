---
uid: DevExpress.Persistent.Validation.IRule.Properties
name: Properties
type: Property
summary: Represents the Validation Rule's properties exported to the [Application Model](xref:112580).
syntax:
  content: IRuleBaseProperties Properties { get; }
  parameters: []
  return:
    type: DevExpress.Persistent.Validation.IRuleBaseProperties
    description: An [](xref:DevExpress.Persistent.Validation.IRuleBaseProperties) object which represents the Validation Rule's properties exported to the Application Model.
seealso: []
---
Information on the Validation Rules declared in the application is saved to the [Application Model](xref:112580)'s [](xref:DevExpress.ExpressApp.Validation.IModelValidationRules) node. Each rule has a corresponding node. These nodes expose properties specifying values for the rules' properties. When implementing the [](xref:DevExpress.Persistent.Validation.IRule) interface, pass the required Validation Rule Properties class' instance via the **Properties** property.