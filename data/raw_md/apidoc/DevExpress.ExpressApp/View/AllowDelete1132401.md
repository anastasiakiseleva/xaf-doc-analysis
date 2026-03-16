---
uid: DevExpress.ExpressApp.View.AllowDelete
name: AllowDelete
type: Property
summary: Provides access to a collection of reason/value pairs used to allow or prohibit deletion of objects via a [](xref:DevExpress.ExpressApp.View).
syntax:
  content: public BoolList AllowDelete { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Utils.BoolList
    description: A [](xref:DevExpress.ExpressApp.Utils.BoolList) object that represents a collection of key/value elements.
seealso: []
---
There can be various reasons to allow or prohibit deletion of objects via a View. So, a View has the **AllowDelete** collection, whose elements represent a pair of string and Boolean values. The string value specifies a reason and the Boolean value specifies whether to allow deletion of objects. Objects cannot be deleted if at least one of the **AllowDelete** collection elements contains a **false** value.

When deletion of objects is prohibited, the **Delete** Action is not available. To determine whether object deletion is allowed for a View, use the **AllowDelete** property in a conditional expression. Alternatively, use the [BoolList.ResultValue](xref:DevExpress.ExpressApp.Utils.BoolList.ResultValue) property of the object returned by **AllowDelete**.

# [C#](#tab/tabid-csharp)

```csharp
View myView;
//...
BoolList deletableList = myView.AllowDelete;
if (deletableList) {
    //...
}
```
***

To prohibit deletion of objects, use the [BoolList.SetItemValue](xref:DevExpress.ExpressApp.Utils.BoolList.SetItemValue(System.String,System.Boolean)) method of the **BoolList** object returned by this property. Pass the prohibition reason as the first parameter, and **false** or a Boolean expression as the second parameter. Alternatively, you can use the **[_key_]** operator of the **BoolList** object returned by the **AllowDelete** property, to get or set the specified key's value.

# [C#](#tab/tabid-csharp)

```csharp
View myView;
//...
BoolList deletableList = myView.AllowDelete;
deletableList["myKey"] = false;
```
***

To allow objects to be deleted, use the [BoolList.RemoveItem](xref:DevExpress.ExpressApp.Utils.BoolList.RemoveItem(System.String)) method of the **BoolList** object returned by this property. Pass the key (reason) of the item with the **false** value.  Call this method as many times as there are items with the **false** value. Alternatively, you can call the [BoolList.SetItemValue](xref:DevExpress.ExpressApp.Utils.BoolList.SetItemValue(System.String,System.Boolean)) method by passing the key, which has **false** as a value, and **true** as a new value for it.

# [C#](#tab/tabid-csharp)

```csharp
View myView;
//...
BoolList deletableList = myView.AllowDelete;
deletableList["disablingKey"] = true;
```
***

# [C#](#tab/tabid-csharp)

```csharp
public class MyController : ViewController {
   private void UpdateViewStateEventHandler(object sender, EventArgs e) {
      View..SetItemValue(
          "CurrentUser", SecuritySystem.CurrentUser.FirstName == "Sam");
   }
   protected override void OnActivated() {
      base.OnActivated();
      View.CurrentObjectChanged += UpdateViewStateEventHandler;
   }
}
```
***

When a View's **AllowDelete** state is changed, the [View.AllowDeleteChanged](xref:DevExpress.ExpressApp.View.AllowDeleteChanged) event is raised.