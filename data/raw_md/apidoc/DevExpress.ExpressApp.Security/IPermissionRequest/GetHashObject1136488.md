---
uid: DevExpress.ExpressApp.Security.IPermissionRequest.GetHashObject
name: GetHashObject()
type: Method
summary: Returns an object which is unique for each set of [](xref:DevExpress.ExpressApp.Security.IPermissionRequest) object's property values.
syntax:
  content: object GetHashObject()
  return:
    type: System.Object
    description: An object which is unique for each set of Permission Request property values.
seealso:
- linkId: "113384"
---
The **GetHashObject** method implementation should satisfy the following requirements:

* a returned object should be serializable;
* a returned object should be the same for different [](xref:DevExpress.ExpressApp.Security.IPermissionRequest) instances with the same set of property values.

Generally, a combination of Permission Request property values can be used to calculate the unique hash object.

# [C#](#tab/tabid-csharp)

```csharp
public class CustomOperationPermissionRequest : IPermissionRequest {
    public string Operation { get; set; }
    public Type ObjectType { get; private set; }
    public object GetHashObject() {
        return string.Format("{0}-{1}", ObjectType.FullName, Operation);
    }
}
```
***

In the simplest case, when your custom Permission Request exposes no properties, you can return the current object type.

# [C#](#tab/tabid-csharp)

```csharp
public class MyPermissionRequest : IPermissionRequest {
    public object GetHashObject() {
        return this.GetType().FullName;
    }
}
```
***