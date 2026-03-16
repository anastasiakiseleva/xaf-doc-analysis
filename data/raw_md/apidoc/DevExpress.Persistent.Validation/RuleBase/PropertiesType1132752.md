---
uid: DevExpress.Persistent.Validation.RuleBase.PropertiesType
name: PropertiesType
type: Property
summary: Specifies the type of the Validation Rule Properties class used by the [Validation Rule](xref:113008).
syntax:
  content: public virtual Type PropertiesType { get; }
  parameters: []
  return:
    type: System.Type
    description: A [](xref:System.Type) object specifying the type of the Validation Rule Properties class used by the Validation Rule. By default, this property returns the [](xref:DevExpress.Persistent.Validation.RuleBaseProperties) type.
seealso: []
---
When inheriting from the **RuleBase** class, if you need to extend the Properties class, override this property to return the custom Properties type. For details, refer to the [Implement Custom Rules](xref:113051) topic.