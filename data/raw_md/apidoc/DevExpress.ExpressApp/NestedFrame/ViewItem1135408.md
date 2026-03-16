---
uid: DevExpress.ExpressApp.NestedFrame.ViewItem
name: ViewItem
type: Property
summary: Provides access to the [View Item](xref:112612) that uses the [](xref:DevExpress.ExpressApp.NestedFrame).
syntax:
  content: public ViewItem ViewItem { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Editors.ViewItem
    description: A [](xref:DevExpress.ExpressApp.Editors.ViewItem) that uses the nested Frame.
seealso: []
---
You can use this property to access the parent View and its object from a Controller activated for the nested Frame.

# [C#](#tab/tabid-csharp)

```csharp
public partial class MyViewController : ViewController {
    protected override void OnActivated() {
        base.OnActivated();
        NestedFrame nestedFrame = Frame as NestedFrame;
        if (nestedFrame != null) {
            View parentView = nestedFrame.ViewItem.View;
            Object parentObject = parentView.CurrentObject;
        }
    }
}
```
***