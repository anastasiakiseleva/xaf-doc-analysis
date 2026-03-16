---
uid: DevExpress.ExpressApp.ViewController`1
name: ViewController<ViewType>
type: Class
summary: A base class for generic [View Controllers](xref:112621).
syntax:
  content: 'public abstract class ViewController<ViewType> : ViewController where ViewType : View'
  typeParameters:
  - id: ViewType
    description: 'The XAF View subtype (for example, DetailView, ListView, or DashboardView) that this Controller targets.
'
seealso:
- linkId: DevExpress.ExpressApp.ViewController`1._members
  altText: ViewController<ViewType> Members
---
ViewController\<ViewType\> is the generic version of the [](xref:DevExpress.ExpressApp.ViewController) class. The `ViewType` type parameter specifies the [View](xref:112611) subtype that the Controller targets. XAF assigns ViewType to the [ViewController.TypeOfView](xref:DevExpress.ExpressApp.ViewController.TypeOfView) property, so the Controller is activated only for that View type. The [ViewController.View](xref:DevExpress.ExpressApp.ViewController.View) property is typed as ViewType, so you can access the View without an explicit cast.

The following code snippet demonstrates a custom View Controller derived from the generic **ViewController**.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Blazor;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Editors;
using MainDemo.Module.BusinessObjects;

namespace MainDemo.Blazor.Server.Controllers;

public sealed class EmlployeeListViewController : ObjectViewController<ListView, Employee> {
    protected override void OnViewControlsCreated() {
        base.OnViewControlsCreated();
        if(View.Editor is DxGridListEditor gridListEditor) {
            // ...
        }
    }
}
```
***

[!include[coderush-templates-actions-controllers](~/templates/coderush-templates-actions-controllers.md)]

Visual Studio Designer does not support generic components and cannot be used to design generic Controllers. As a workaround, declare an intermediate non-generic base class that derives from a generic Controller and is decorated with the [DesignerCategoryAttribute](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.designercategoryattribute). Then derive your custom Controller from that intermediate class. The following code snippet illustrates this approach.

# [C#](#tab/tabid-csharp)

```csharp
using System.ComponentModel;
using DevExpress.Blazor;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Editors;
using MainDemo.Module.BusinessObjects;

namespace MainDemo.Blazor.Server.Controllers;

[DesignerCategory("Component")]
public abstract class MyIntermediateListViewController : ObjectViewController<ListView, Employee> {
    //...
}

public sealed class MyViewController : MyIntermediateListViewController {
    //...
}
```
***
