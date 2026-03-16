---
uid: DevExpress.ExpressApp.View.AllowNew
name: AllowNew
type: Property
summary: Provides access to a collection of reason/value pairs used to allow or prohibit creation of new objects via a [](xref:DevExpress.ExpressApp.View).
syntax:
  content: public BoolList AllowNew { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Utils.BoolList
    description: A [](xref:DevExpress.ExpressApp.Utils.BoolList) object that represents a collection of key/value elements.
seealso: []
---
There can be various reasons to allow or prohibit creation of new objects via a View. So, a View has the **AllowNew** collection, whose elements represent a pair of string and Boolean values. The string value specifies a reason and the Boolean value specifies whether to allow creation of new objects. New objects cannot be created if at least one of the **AllowNew** collection elements contains a **false** value.

When creation of new objects is prohibited, the **New** Action is not available. To determine whether object creation is allowed for a View, use the **AllowNew** property in a conditional expression. Alternatively, use the [BoolList.ResultValue](xref:DevExpress.ExpressApp.Utils.BoolList.ResultValue) property of the object returned by **AllowNew**.

# [C#](#tab/tabid-csharp)

```csharp
View myView;
//...
BoolList creatableList = myView.AllowNew;
if (creatableList) {
    //...
}
```
***

To prohibit creation of new objects, use the [BoolList.SetItemValue](xref:DevExpress.ExpressApp.Utils.BoolList.SetItemValue(System.String,System.Boolean)) method of the **BoolList** object returned by this property. Pass the prohibition reason as the first parameter, and **false**, or a Boolean expression as the second parameter. Alternatively, you can use the **[_key_]** operator of the **BoolList** object returned by the **AllowNew** property, to get or set the specified key's value.

# [C#](#tab/tabid-csharp)

```csharp
View myView;
//...
BoolList creatableList = myView.AllowNew;
creatableList["myKey"] = false;
```
***

To allow new objects to be created, use the [BoolList.RemoveItem](xref:DevExpress.ExpressApp.Utils.BoolList.RemoveItem(System.String)) method of the **BoolList** object returned by this property. Pass the key (reason) of the item with the **false** value.  Call this method as many times as there are items with the **false** value. Alternatively, you can call the [BoolList.SetItemValue](xref:DevExpress.ExpressApp.Utils.BoolList.SetItemValue(System.String,System.Boolean)) method by passing the key, which has **false** as a value, and **true** as a new value for it.

# [C#](#tab/tabid-csharp)

```csharp
View myView;
//...
BoolList creatableList = myView.AllowNew;
creatableList["disablingKey"] = true;
```
***

# [C#](#tab/tabid-csharp)

```csharp
public class MyController : ViewController {
   private void UpdateViewStateEventHandler(object sender, EventArgs e) {
      View.AllowNew.SetItemValue("CurrentUser", SecuritySystem.CurrentUser.FirstName == "Sam");
   }
   protected override void OnActivated() {
      base.OnActivated();
      View.CurrentObjectChanged += UpdateViewStateEventHandler;
   }
}
```
***

When a View's **AllowNew** state is changed, the [View.AllowNewChanged](xref:DevExpress.ExpressApp.View.AllowNewChanged) event is raised.