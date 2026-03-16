---
uid: DevExpress.ExpressApp.Utils.EnumDescriptor.GetEnumType(System.Type)
name: GetEnumType(Type)
type: Method
summary: Returns the underlying type of a specified enumeration.
syntax:
  content: public static Type GetEnumType(Type type)
  parameters:
  - id: type
    type: System.Type
    description: A [](xref:System.Type) object representing either an enumeration type or a nullable enumeration type.
  return:
    type: System.Type
    description: A [](xref:System.Type) object representing the underlying enumeration type.
seealso: []
---
If a plain enumeration type is passed as the _type_ parameter, the **GetEnumType** method returns this type. If a nullable enumeration type is passed as the _type_ parameter, the **GetEnumType** method returns the type of the underlying plain enumeration.