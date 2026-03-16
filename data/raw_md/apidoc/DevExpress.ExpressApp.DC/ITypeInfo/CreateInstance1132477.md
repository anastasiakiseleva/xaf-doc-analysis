---
uid: DevExpress.ExpressApp.DC.ITypeInfo.CreateInstance(System.Object[])
name: CreateInstance(Object[])
type: Method
summary: Creates an instance of the current type using the constructor that best matches the specified parameters.
syntax:
  content: object CreateInstance(params object[] args)
  parameters:
  - id: args
    type: System.Object[]
    description: An array of arguments that match in number, order, and type, the parameters of the constructor to invoke.
  return:
    type: System.Object
    description: A reference to the newly created object.
seealso: []
---
If an empty array or `null` reference is passed as the **args** parameter, the default constructor is invoked.