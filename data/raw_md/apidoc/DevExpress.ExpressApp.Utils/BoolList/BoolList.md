---
uid: DevExpress.ExpressApp.Utils.BoolList
name: BoolList
type: Class
summary: A list of string key/Boolean value pairs, which provides the resulting Boolean value, based on the pair values.
syntax:
  content: 'public class BoolList : ISupportUpdate'
seealso:
- linkId: DevExpress.ExpressApp.Utils.BoolList._members
  altText: BoolList Members
- linkId: DevExpress.ExpressApp.Actions.ActionBase.Active
- linkId: DevExpress.ExpressApp.Controller.Active
- linkId: DevExpress.ExpressApp.Actions.ActionBase.Enabled
- linkId: DevExpress.ExpressApp.View.AllowNew
- linkId: DevExpress.ExpressApp.View.AllowEdit
- linkId: DevExpress.ExpressApp.View.AllowDelete
- linkId: DevExpress.ExpressApp.Editors.PropertyEditor.AllowEdit
---
The **BoolList** class represents a wrapper over a dictionary of string key/Boolean value pairs. A string key names the associated Boolean value. Based on the Boolean values, the **BoolList** determines the resulting value and exposes it via the [BoolList.ResultValue](xref:DevExpress.ExpressApp.Utils.BoolList.ResultValue) property. The resulting value is determined, either by logically multiplying or logically summing the values from the **BoolList**'s collection of key/value pairs. You can specify how the resulting value is determined by specifying the [](xref:DevExpress.ExpressApp.Utils.BoolListOperatorType) _operatorType_ parameter when instantiating a **BoolList** via its [BoolList](xref:DevExpress.ExpressApp.Utils.BoolList.#ctor*) constructor.

**XAF** uses **BoolList**s to provide conditional activation and deactivation of particular features. Consider the following example. Each [Action](xref:112622) has the [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active) property. This property exposes a **BoolList**, working in the [BoolListOperatorType.And](xref:DevExpress.ExpressApp.Utils.BoolListOperatorType.And) mode. When you specify an Action's **Target…** properties, such as [ActionBase.TargetObjectType](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetObjectType), a corresponding key is created in the Action's **Active** **BoolList**. Suppose that you have an Action whose [ActionBase.TargetObjectType](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetObjectType) is set to **Person**. In this instance, the Action's **Active** **BoolList** can look like this:

``Key="Controller active" Value="True"``

``Key="ObjectType" Value="False"``

The first key's value specifies that the Action's [Controller](xref:112621) is active, and so the Action can also be active. The second key's value specifies that the current [View](xref:112611) is not of the **Person** type, so the Action cannot be active. The resulting value of the **Active** **BoolList** is determined by logically multiplying the values from the **BoolList**, which in this example yields **false**. So, the sample Action will not be activated.

The **BoolList** class overrides the [BoolList.Equals](xref:DevExpress.ExpressApp.Utils.BoolList.Equals(System.Object)) method. This allows you to use instances of the **BoolList** class in Boolean expressions, and compare such instances directly to Boolean values. The following code snippet illustrates this.

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

To add a new key/value pair to a **BoolList** or modify an existing one, use the [BoolList.Item](xref:DevExpress.ExpressApp.Utils.BoolList.Item(System.String)) indexer property. Alternatively, you can use the [BoolList.SetItemValue](xref:DevExpress.ExpressApp.Utils.BoolList.SetItemValue(System.String,System.Boolean)) method. To remove an item from a **BoolList**, use the [BoolList.RemoveItem](xref:DevExpress.ExpressApp.Utils.BoolList.RemoveItem(System.String)) method.