---
uid: DevExpress.ExpressApp.Utils.BoolList.ResultValue
name: ResultValue
type: Property
summary: Specifies the resulting value of the [](xref:DevExpress.ExpressApp.Utils.BoolList).
syntax:
  content: public bool ResultValue { get; }
  parameters: []
  return:
    type: System.Boolean
    description: A Boolean value representing the resulting value of the **BoolList**.
seealso: []
---
The **ResultValue** property specifies the resulting value of the **BoolList**, which is based on the values from the **BoolList**'s collection of key/value pairs. The resulting value is determined based on the [](xref:DevExpress.ExpressApp.Utils.BoolListOperatorType) mode specified via the [BoolList](xref:DevExpress.ExpressApp.Utils.BoolList.#ctor*) constructor's _operatorType_ parameter. When the [BoolListOperatorType.And](xref:DevExpress.ExpressApp.Utils.BoolListOperatorType.And) mode is used, the resulting value of a **BoolList** is determined by logically multiplying all the values from the **BoolList**'s collection of key/value pairs. When the [BoolListOperatorType.Or](xref:DevExpress.ExpressApp.Utils.BoolListOperatorType.Or) mode is used, the resulting value of a **BoolList** is determined by logically summing all the values from the **BoolList**'s collection of key/value pairs.

Generally, there is no need to use the **ResultValue** property as **BoolList** overrides the [BoolList.Equals](xref:DevExpress.ExpressApp.Utils.BoolList.Equals(System.Object)) method. This allows you to use instances of the **BoolList** class in Boolean expressions, and compare such instances directly to Boolean values. The following code snippet illustrates this.

# [C#](#tab/tabid-csharp)

```csharp
BoolList myList = new BoolList();
myList["myKey"] = true;
//...
if(myList) {
    //...
}
```
***

For a general description of the **BoolList** class, refer to the [](xref:DevExpress.ExpressApp.Utils.BoolList) class description.