---
uid: DevExpress.ExpressApp.View.AllowEdit
name: AllowEdit
type: Property
summary: Provides access to a collection of reason/value pairs used to make a [](xref:DevExpress.ExpressApp.View) read-only/editable.
syntax:
  content: public BoolList AllowEdit { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Utils.BoolList
    description: A [](xref:DevExpress.ExpressApp.Utils.BoolList) object that represents a collection of key/value elements.
seealso: []
---

The example below demonstrates how to make all [Detail Views](xref:112611#detail-view) in an application read-only.

# [C#](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp;
// ...
public class MakeDetailViewsReadOnlyController : ViewController<DetailView> {
    protected override void OnActivated() {
        base.OnActivated();
        View.AllowEdit["ReadOnly"] = false;
    }
}
```
***

There can be various reasons to make a View read-only or editable. So, a View has the **AllowEdit** collection, whose elements represent a pair of string and Boolean values. The string value specifies a reason and the Boolean value specifies whether to make the View editable for this reason. A View is considered read-only if at least one of the **AllowEdit** collection elements contains a **false** value.

The read-only state of a Detail View and List View is characterized by the following:

* **Detail View**
    
    All Property Editors are created in read-only mode.
* **List View**
    
    Inplace editing is not allowed.

To determine whether a View is currently read-only, use the **AllowEdit** property in a conditional expression. Alternatively, use the [BoolList.ResultValue](xref:DevExpress.ExpressApp.Utils.BoolList.ResultValue) property of the object returned by **AllowEdit**.

# [C#](#tab/tabid-csharp)

```csharp
View myView;
//...
BoolList editableList = myView.AllowEdit;
if (editableList) {
    //...
}
```
***

To make an editable View read-only, use the [BoolList.SetItemValue](xref:DevExpress.ExpressApp.Utils.BoolList.SetItemValue(System.String,System.Boolean)) method of the **BoolList** object returned by this property. Pass the reason for making the View read-only as the first parameter, and **false** or a Boolean expression as the second parameter. Alternatively, you can use the **[_key_]** operator of the **BoolList** object returned by the **AllowEdit** property, to get or set the specified key's value.

# [C#](#tab/tabid-csharp)

```csharp
View myView;
//...
BoolList editableList = myView.AllowEdit;
editableList["myKey"] = false;
```
***

To make a read-only View editable, use the [BoolList.RemoveItem](xref:DevExpress.ExpressApp.Utils.BoolList.RemoveItem(System.String)) method of the **BoolList** object returned by this property. Pass the key (reason) of the item with the **false** value.  Call this method as many times as there are items with the **false** value. Alternatively, you can call the [BoolList.SetItemValue](xref:DevExpress.ExpressApp.Utils.BoolList.SetItemValue(System.String,System.Boolean)) method by passing the key, which has **false** as a value, and **true** as a new value for it.

# [C#](#tab/tabid-csharp)

```csharp
View myView;
//...
BoolList editableList = myView.AllowEdit;
editableList["disablingKey"] = true;
```
***

# [C#](#tab/tabid-csharp)

```csharp
public class MyController : ViewController {
   private void UpdateViewStateEventHandler(object sender, EventArgs e) {
      View.AllowEdit.SetItemValue("CurrentUser", SecuritySystem.CurrentUser.FirstName == "Sam");
   }
   protected override void OnActivated() {
      base.OnActivated();
      View.CurrentObjectChanged += UpdateViewStateEventHandler;
   }
}
```
***

When a View's read-only state is changed, the [View.AllowEditChanged](xref:DevExpress.ExpressApp.View.AllowEditChanged) event is raised.