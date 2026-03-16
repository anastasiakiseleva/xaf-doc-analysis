---
uid: DevExpress.ExpressApp.Blazor.Editors.StaticTextViewItem.ComponentModel
name: ComponentModel
type: Property
summary: Returns a `StaticTextComponentModel` descendant that wraps properties and events of a corresponding Static Text [View Item](xref:112612).
syntax:
  content: public StaticTextComponentModel ComponentModel { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Blazor.Components.Models.StaticTextComponentModel
    description: A component model of a Static Text [View Item](xref:112612).
seealso: []
---

To customize the Static Text View Item's underlying component, call the `View.CustomizeViewItemControl` method and obtain the component model (the `ComponentModel` property).

The following code snippet demonstrates how to enable HTML markup in a Static Text component:

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Editors;
using YourApplicationName.Module.BusinessObjects;

namespace YourApplicationName.Blazor.Server.Controllers;
public partial class MyStaticCustomizeController : ObjectViewController<DetailView, Employee> {
    protected override void OnActivated() {
        base.OnActivated();
        View.CustomizeViewItemControl<StaticTextViewItem>(this, SetStaticItem, "MyStatic");
    }
    private void SetStaticItem(StaticTextViewItem staticText) {
        staticText.ComponentModel.UseMarkupString = true;
    }
}
```