---
uid: DevExpress.ExpressApp.Actions.ActionBase.BeginUpdate
name: BeginUpdate()
type: Method
summary: Prevents an [Action](xref:112622) from being updated until the [ActionBase.EndUpdate](xref:DevExpress.ExpressApp.Actions.ActionBase.EndUpdate) method is called.
syntax:
  content: public void BeginUpdate()
seealso: []
---
The **BeginUpdate** and [ActionBase.EndUpdate](xref:DevExpress.ExpressApp.Actions.ActionBase.EndUpdate) methods are designed to implement batch modifications with Actions. This allows you to prevent excessive updates when changing multiple settings at once. For this purpose, enclose the code that changes the properties within calls to these methods.

The **BeginUpdate** and **EndUpdate** methods use an internal counter to implement their functionality. The counter's initial value is **0**. The current lock count is returned by the `ActionBase.LockCount` property. A call to the **BeginUpdate** method increments the counter by one. A call to the **EndUpdate** method decrements the counter by one, and if its new value is zero, a change notification is generated. This means that each call to **BeginUpdate** must be paired with a call to **EndUpdate**. If a call to **BeginUpdate** is made but without a corresponding call to **EndUpdate** afterwards or **EndUpdate** is not called because an exception occurred, the **Action** will no longer respond to changes. To ensure that **EndUpdate** is always called even if an exception occurs, wrap any calls to these methods in a **try...finally** statement.