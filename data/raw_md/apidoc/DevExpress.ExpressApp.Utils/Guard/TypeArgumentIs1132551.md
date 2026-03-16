---
uid: DevExpress.ExpressApp.Utils.Guard.TypeArgumentIs(System.Type,System.Type,System.String)
name: TypeArgumentIs(Type, Type, String)
type: Method
summary: Ensures that an argument has a specific type.
syntax:
  content: public static void TypeArgumentIs(Type expectedType, Type passedType, string argumentName)
  parameters:
  - id: expectedType
    type: System.Type
    description: A [](xref:System.Type) object representing the expected type of the argument.
  - id: passedType
    type: System.Type
    description: A [](xref:System.Type) object representing the actual type of the argument.
  - id: argumentName
    type: System.String
    description: A string holding the name of the argument to check.
seealso: []
---
If the specified argument has a different type, an exception is thrown.