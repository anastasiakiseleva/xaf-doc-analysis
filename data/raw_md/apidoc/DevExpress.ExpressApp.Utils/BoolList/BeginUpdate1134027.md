---
uid: DevExpress.ExpressApp.Utils.BoolList.BeginUpdate
name: BeginUpdate()
type: Method
summary: Prevents the [](xref:DevExpress.ExpressApp.Utils.BoolList) from being updated until the [BoolList.EndUpdate](xref:DevExpress.ExpressApp.Utils.BoolList.EndUpdate) method is called.
syntax:
  content: public void BeginUpdate()
seealso: []
---
The **BeginUpdate** and [BoolList.EndUpdate](xref:DevExpress.ExpressApp.Utils.BoolList.EndUpdate) methods are designed to implement batch modifications with a **BoolList**. After the **BeginUpdate** method has been called, and until a call to the [BoolList.EndUpdate](xref:DevExpress.ExpressApp.Utils.BoolList.EndUpdate) method, the **BoolList**'s events will not be raised and the [BoolList.ResultValue](xref:DevExpress.ExpressApp.Utils.BoolList.ResultValue) property value will not change. This allows you to prevent excessive updates when changing multiple key values at once. For this purpose, enclose the code that changes multiple keys within calls to these methods. The following code snippet illustrates this.

# [C#](#tab/tabid-csharp)

```csharp
//...
mySimpleAction.Active.BeginUpdate();
mySimpleAction.Active["MyReason1"] = "true";
mySimpleAction.Active["MyReason2"] = "true";
mySimpleAction.Active["MyReason3"] = "true";
//...
mySimpleAction.Active.EndUpdate();
```
***

The **BeginUpdate** and **EndUpdate** methods use an internal counter to implement their functionality. The counter's initial value is **0**. A call to the **BeginUpdate** method increments the counter by one. A call to the **EndUpdate** method decrements the counter by one, and if its new value is zero, a change notification is generated. This means that each call to **BeginUpdate** must be paired with a call to **EndUpdate**. If a call to **BeginUpdate** is made, but without a subsequent corresponding call to **EndUpdate**, or **EndUpdate** is not called because an exception occurred, the **BoolList** will no longer respond to changes. To ensure that **EndUpdate** is always called even if an exception occurs, wrap any calls to these methods in a **try...finally** statement.