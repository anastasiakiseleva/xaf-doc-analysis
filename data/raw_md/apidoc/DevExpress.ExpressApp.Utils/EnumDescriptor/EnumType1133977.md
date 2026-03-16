---
uid: DevExpress.ExpressApp.Utils.EnumDescriptor.EnumType
name: EnumType
type: Property
summary: Specifies the underlying type of the enumeration represented by the [](xref:DevExpress.ExpressApp.Utils.EnumDescriptor).
syntax:
  content: public Type EnumType { get; }
  parameters: []
  return:
    type: System.Type
    description: A [](xref:System.Type) object representing the underlying enumeration type.
seealso: []
---
If the [](xref:DevExpress.ExpressApp.Utils.EnumDescriptor) class was instantiated for a plain enumeration type, the **EnumType** property returns this type. If the **EnumDescriptor** was instantiated for a nullable enumeration type, the **EnumType** property returns the type of the underlying plain enumeration. To check whether the **EnumDescriptor** represents a nullable enumeration type, use the [EnumDescriptor.IsNullable](xref:DevExpress.ExpressApp.Utils.EnumDescriptor.IsNullable) property.